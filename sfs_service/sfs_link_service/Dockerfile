#!/bin/sh
FROM python:latest
ADD app.py .
ADD models.py .
ADD requirements.txt .
ADD static /static
ADD templates/ /templates 
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]