FROM python

WORKDIR /app 

COPY S3.py .

RUN pip install boto3 python-dateutil

CMD ["python", "S3.py"]

