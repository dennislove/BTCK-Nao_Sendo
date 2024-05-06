FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysql-connector-python
COPY . /app

CMD ["python", "db_api.py"]