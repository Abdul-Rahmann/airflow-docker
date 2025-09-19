from sched import scheduler

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


defaulter_args = {
    'owner': 'sam',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

def greet(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name',key='last_name')
    print(f"Hello! my name is {first_name} {last_name} and I am {age} years old.")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Samuel')
    ti.xcom_push(key='last_name', value='Adetsi')

with DAG(
    dag_id='my_dag_with_python_operator_v5',
    description='My first dag using python operator',
    default_args=defaulter_args,
    start_date=datetime(2025, 9, 17),
    schedule="@daily",
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': 25}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )

    task2 >> task1