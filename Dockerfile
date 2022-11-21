FROM python:3.10-slim

RUN apt update && apt -y install libpq-dev build-essential

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "djangostripe.wsgi:application", "--bind", "0:8000"]
