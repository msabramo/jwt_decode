FROM python:3-alpine

RUN pip install PyJWT

WORKDIR /usr/src/app
ADD jwt-decode.py /usr/src/app

ENTRYPOINT ["python", "jwt-decode.py"]
