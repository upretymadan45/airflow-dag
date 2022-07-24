from datetime import datetime,timedelta
import time
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator

default_args = {
    'owner':'mm',
    'retries':5,
    'retry_delay' : timedelta(minutes=2)
}

def sayHello():
    api_url = "https://host.docker.internal/api/Demo/GetAll"
    response = requests.get(api_url,verify=False)
    print(response.status_code)
    print(time.time())

def handle_response(response):
    if response.status_code == 200:
        print('received 200 OK')
        return True
    else:
        print('Error')
        return False

with DAG(
    dag_id = 'our_first_dag_16',
    default_args= default_args,
    description= 'this is the first dag i created',
    start_date= datetime(2022,7,23,13,25),
    schedule_interval= '*/5 * * * *'
) as dag: 
    task1 = PythonOperator(
        task_id = 'first_task',
        python_callable= sayHello
    )
    task1
