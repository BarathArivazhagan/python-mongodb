FROM python:3.10-alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD ["./main.py"]