FROM python:3.13.7

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt

CMD ["pytest", "tests"]