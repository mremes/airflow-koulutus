from weatherbit.api.historical import fetch_hourly_data
from weatherbit.parsing.historical import parse_weather, parse_temperature
import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
from airflow.models import Variable

args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(day=20, month=11, year=2018),
}

with DAG(dag_id='weather_dag', default_args=args) as dag:
    cities = Variable.get('weatherbit_cities').split(',')
    api_key = Variable.get('weatherbit_api_key')

    def get_filename_by_type_and_city(filetype, city):
        return '{}_{}'.format(filetype, city) + '_{{ ds_nodash }}.csv'

    drop_files = BashOperator(task_id='drop_files',
                              bash_command='cd $AIRFLOW_HOME && rm *_{{ ds_nodash }}.csv')

    for city in cities:
        historical_target = get_filename_by_type_and_city('historical', city)
        weather_target = get_filename_by_type_and_city('weather', city)
        temperature_target = get_filename_by_type_and_city('temperature', city)

        # Operator for fetching historical weather data data
        templated_kwargs = dict(target=historical_target,
                                start_date='{{ ds }}',
                                end_date='{{ tomorrow_ds }}')

        op_kwargs = dict(city=city,
                         api_key=api_key)

        fetch_weather_data = PythonOperator(
            task_id='weather_task_for_{}'.format(city),
            pool='weatherbit_api',
            python_callable=fetch_hourly_data,
            provide_context=True,
            templates_dict=templated_kwargs,
            op_kwargs=op_kwargs
        )

        # Operator for parsing weather data
        templated_kwargs = dict(source=historical_target,
                                target=weather_target)

        parse_weather_op = PythonOperator(task_id='parse_weather_{}'.format(city),
                                          python_callable=parse_weather,
                                          provide_context=True,
                                          templates_dict=templated_kwargs)

        # Operator for parsing temperature data
        templated_kwargs = dict(source=historical_target,
                                target=temperature_target)

        parse_temperature_op = PythonOperator(task_id='parse_temperature_{}'.format(city),
                                              python_callable=parse_temperature,
                                              provide_context=True,
                                              templates_dict=templated_kwargs)

        parsing_tasks = [parse_weather_op, parse_temperature_op]
        fetch_weather_data >> parsing_tasks

        for parsing_task in parsing_tasks:
            target = parsing_task.templates_dict['target']
            filetogcs = FileToGoogleCloudStorageOperator(task_id='{}_to_gcs'.format(parsing_task.task_id),
                                                         src=target,
                                                         dst=target,
                                                         bucket='airflow_training_weather_data',
                                                         mime_type='text/csv')
            parsing_task >> filetogcs
            filetogcs >> drop_files




