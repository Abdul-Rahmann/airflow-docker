from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'sam',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_cron_expression',
    default_args=default_args,
    description='This is a bash operator dag',
    start_date=datetime(2025, 9, 1),
    schedule='0 0 * * *',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1_cron',
        bash_command='echo dags with cron expression!'
    )

    task1