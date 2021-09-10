# Pull a base image
FROM python:3.8.2-slim
# Set environment variables
ENV APP_HOME /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=core.settings.prod
# Create a working directory for the django project
WORKDIR ${APP_HOME}

# Copy the project files into the working directory
COPY . .
# Install the requirements to the container
RUN pip install pip --upgrade
RUN pip install pipenv && pipenv install --system --skip-lock --dev
RUN  python manage.py collectstatic --noinput

EXPOSE ${PORT}

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 core.wsgi:application