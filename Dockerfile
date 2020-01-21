FROM mralext20/pyboy:alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
RUN chmod +x ./docker-entry-point.sh
WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]
