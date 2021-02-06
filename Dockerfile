FROM python:3.8.7-buster

#creating directory for app
WORKDIR /root/testing

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /root/testing



CMD [ "python3", "bot.py" ]
