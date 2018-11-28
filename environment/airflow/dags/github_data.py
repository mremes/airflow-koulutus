import os
import datetime
from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.bigquery_check_operator import BigQueryCheckOperator

args = {
    'owner': 'matti',
    'start_date': datetime.datetime(day=20, month=11, year=2018),
}

template_path = '{}/{}'.format(os.environ['AIRFLOW_HOME'], 'dags/sql')

with DAG(dag_id='github_dag', default_args=args, template_searchpath=template_path) as dag:
    github_commits = BigQueryOperator(task_id='github_commits',
                                      sql='github_users_aggregate.sql',
                                      use_legacy_sql=False,
                                      write_disposition='WRITE_TRUNCATE',
                                      destination_dataset_table='github.commits${{ ds_nodash }}')
    test__check_commit_sums_match_with_raw_data = BigQueryCheckOperator(task_id='TEST_commit_sums_match',
                                                                        sql='github_users_check_commit_sums.sql',
                                                                        use_legacy_sql=False)
    github_commits >> test__check_commit_sums_match_with_raw_data
