FROM python:3.12.3-bookworm

WORKDIR /backend

COPY ./requirements.txt .
 
RUN pip install --upgrade -r requirements.txt

COPY ./models .

COPY ./main.py .

CMD ["python", "main.py"]