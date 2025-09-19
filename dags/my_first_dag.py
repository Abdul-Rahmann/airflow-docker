from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'sam',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='my_first_dag_v2',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2025, 9, 18),
    schedule="@daily"
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo This is the first task'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo This is the second task, will be running after task1'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo This is the third task, will be running after task2'
    )

    # task1 >> task2
    #
    # task1 >> task3

    # task1.set_downstream(task2)
    task1 >> [task2, task3]