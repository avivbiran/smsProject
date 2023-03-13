FROM python:3.8-slim-buster

WORKDIR /app

COPY requierments.txt requierments.txt

RUN pip install -r requirments.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]