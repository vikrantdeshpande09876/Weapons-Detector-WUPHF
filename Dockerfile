FROM python:slim

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /wuphf-notification-sender

CMD ["python", "app.py"]