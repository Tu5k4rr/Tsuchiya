FROM python:3.8.7-buster

#creating directory for app
WORKDIR /bot

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /bot/



CMD [ "python3", "bot.py" ]
