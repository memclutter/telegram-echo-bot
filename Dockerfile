FROM python:3.6-alpine
RUN mkdir -p /usr/local/src/
COPY . /usr/local/src/
RUN pip install --upgrade pip \
 && pip install -r /usr/local/src/requirements.txt
CMD python /usr/local/src/main.py
