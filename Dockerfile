FROM --platform=linux/amd64 python:3.9-buster
USER root
RUN mkdir -p /application/src
WORKDIR /application/src
COPY . .
RUN chmod a+rwx /application/src
RUN chmod +x kubectl
RUN mv kubectl /usr/local/bin
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "app.py"]