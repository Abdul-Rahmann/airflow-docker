from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'sam',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_and_backfill_v2',
    default_args=default_args,
    description='This is a bash operator dag',
    start_date=datetime(2025, 9, 1),
    schedule='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo This is a simple bash command!'
    )

    task1