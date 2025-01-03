FROM python:3.12-slim

WORKDIR /app
# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./
# Устанавливаем Poetry и зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

# установленный в 1, предотвращает создание .pyc файлов
ENV PYTHONDONTWRITEBYTECODE=1
# установленный в 1, отключает буферизацию стандартного вывода
ENV PYTHONUNBUFFERED=1

COPY . .

# запускающая команда в docker-compose.yaml
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

