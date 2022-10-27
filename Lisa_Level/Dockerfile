FROM python:3.9.12

COPY ./Lisa_Level.py /app/
COPY ./Docker.txt /app/

WORKDIR /app/
RUN pip3 install -r ./Docker.txt 

CMD ["python", "Lisa_Level.py"]
