FROM python:3.10

WORKDIR /app-graf
COPY requirements.txt /app-graf/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app-graf/requirements.txt

COPY . /app-graf

CMD bash -c "while true; do sleep 1; done"
