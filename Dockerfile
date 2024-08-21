FROM python:3.10.0

RUN apt-get update -y && \
    apt-get install python3-opencv -y

WORKDIR /main

COPY . /main

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "main.py"]
