# Базовый образ, который тоже состоит из слоев
FROM python:3.8

# Новый слой
WORKDIR /code
# Новый слой
COPY requirements.txt .
# Новый слой
RUN pip install -r requirements.txt
# Новый слой
COPY run.py .

# Новый слой
CMD flask run -h 0.0.0.0 -p 80
