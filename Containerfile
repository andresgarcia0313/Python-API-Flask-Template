FROM python:alpine
WORKDIR /app
COPY . .
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000
RUN apk update && apk add git bash
RUN pip install -r requirements.txt
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=5000 --reload & tail -f /dev/null"]