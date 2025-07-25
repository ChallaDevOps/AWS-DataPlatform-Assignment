FROM python:3.9
WORKDIR /app 

COPY python_script.py .
COPY sample.txt .

RUN pip install boto3

CMD ["python", "python_script.py"]
