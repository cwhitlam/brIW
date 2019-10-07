FROM python:latest

COPY . /

RUN pip3 install -r /requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3", "-m", "src.website.app"]

