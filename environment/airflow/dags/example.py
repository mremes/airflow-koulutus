import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'matti',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='example',
    default_args=args,
    schedule_interval='0 0 * * *'
)

run_me_first = BashOperator(
    task_id='run_me_first',
    bash_command='echo "Let\'s start!"',
    dag=dag,
)

run_me_last = DummyOperator(
    task_id='run_me_last',
    dag=dag,
)

for i in range(3):
    task = BashOperator(
        task_id='i_am_{}_in_the_loop'.format(str(i)),
        bash_command='echo "I am task number {}." && sleep 1'.format(str(i)),
        dag=dag,
    )
    run_me_first >> task
    task >> run_me_last