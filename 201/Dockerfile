FROM prefecthq/prefect
COPY requirements.txt /opt/prefect/201/requirements.txt
RUN python -m pip install -r requirements.txt
COPY . /opt/prefect/201/
WORKDIR /opt/prefect/201/

