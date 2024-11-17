FROM python:3.12-slim-bookworm


WORKDIR /sport_calendar


# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc \
                        libpq-dev \
                        postgresql-client \
    && apt-get clean

# Copy project files
COPY requirements.txt .
COPY ./scripts/entrypoint.sh /entrypoint.sh
COPY ./sport_calendar .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
