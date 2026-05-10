from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="fwa_modernization_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="0 5 * * *",
    catchup=False,
    tags=["healthcare", "fwa", "tableau", "warehouse"],
) as dag:
    generate_data = BashOperator(task_id="generate_synthetic_data", bash_command="python pipelines/python/generate_all_synthetic_data.py --claims 5000")
    bronze_to_silver = BashOperator(task_id="bronze_to_silver", bash_command="python pipelines/python/etl/bronze_to_silver.py")
    silver_to_gold = BashOperator(task_id="silver_to_gold", bash_command="python pipelines/python/etl/silver_to_gold.py")
    score_providers = BashOperator(task_id="provider_risk_scoring", bash_command="python pipelines/python/scoring/provider_risk_scoring.py")
    dq_tests = BashOperator(task_id="data_quality_tests", bash_command="pytest tests/data_quality tests/unit")
    refresh_tableau = BashOperator(task_id="refresh_tableau_extracts", bash_command="echo 'Call Tableau REST API refresh here'")

    generate_data >> bronze_to_silver >> silver_to_gold >> score_providers >> dq_tests >> refresh_tableau
