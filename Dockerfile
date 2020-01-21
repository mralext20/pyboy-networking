FROM mralext20/pyboy:alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
RUN chmod +x ./docker-entrypoint.sh
EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]
