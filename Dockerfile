FROM python:3.11

COPY . ./app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -r test-requirements.txt

CMD ["pytest", "tests/"]
