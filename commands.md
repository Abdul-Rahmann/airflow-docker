[//]: # (Downloading docker-compose file)
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.6/docker-compose.yaml'

Setting up airflow-docker
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html


[//]: # (Getting username and password)

 cat docker-compose.yaml | grep -i =A5 -B5 "user\|password\|admin"