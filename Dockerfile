FROM python:3.12.3-bookworm

WORKDIR /potato_disease
 
COPY ./requirements-docker.txt .
 
RUN pip install --upgrade -r /potato_disease/requirements-docker.txt
 
COPY ./api ./api

CMD ["python", "api/main-tf-serving.py"]
