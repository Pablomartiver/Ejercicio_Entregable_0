FROM python:3.9.12
COPY ./Maggie_Level.py /app/
COPY ./Docker.txt /app/

WORKDIR /app/
RUN mkdir General
RUN mkdir Homer
RUN mkdir Lisa
RUN pip3 install -r ./Docker.txt


CMD ["python", "Maggie_Level.py"]
