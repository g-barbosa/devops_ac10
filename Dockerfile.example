FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r app/requirements.txt
EXPOSE 5000
CMD ["python", "app/com/faculdadeimpacta/calculadora/app_web_start.py"]
