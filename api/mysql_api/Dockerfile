FROM python

COPY . ./api
RUN pip install fastapi uvicorn
CMD ["uvicorn", "db_api:app", "--host", "0.0.0.0:8000"]