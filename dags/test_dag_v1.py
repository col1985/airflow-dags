from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'testing ...',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'test_dag_v1',
    default_args=default_args,
    description='A simple DAG to test git-sync and execution',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['testing'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='verify_environment',
        bash_command='echo "Running in Airflow Cluster: $HOSTNAME"',
    )

    t1 >> t2