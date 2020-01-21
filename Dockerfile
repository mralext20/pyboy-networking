FROM mralext20/pyboy:alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
