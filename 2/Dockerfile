FROM python:3
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x app.py

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]

