from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'sam',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

@dag(
    dag_id='hello_world_etl_dag_v2',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2025, 9, 18),
    schedule="@daily")
def hello_world_etl():
    print("Hello World!")

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Samuel',
            'last_name': 'Adetsi'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(firstname, lastname, age):
        print(f"Hello! my name is {firstname} {lastname} and I am {age} years old.")

    name_dict = get_name()
    age = get_age()
    greet(name_dict['first_name'], name_dict['last_name'], age)

greet_dag = hello_world_etl()
