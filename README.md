# WELCOME TO EDW PROJECT

### EDW is a simple ETL that interacts with the EDW (European Data Warehouse) to fetch thr required

### How it works
####  At a high level this project connects to the EDW through sftp client, accesses the files that contain the required data, gets the data and loads it into the CARDO database for further operations.

### Setup
#### Dependencies
This project is mainly written in pure python using Apache Airflow as the scheduler for the pipelines
In order for this project to be setup you need:
- **Python 3.6, 3.7, 3.8, 3.9**
- **Apache-Airflow** https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html


### Setup
####       If your system's default python is other than the ones mentioned above consider installing another version of python
####       You can do this using pyenv https://github.com/pyenv/pyenv
