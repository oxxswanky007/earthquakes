FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY fetch_quakes.py .
RUN adduser -D appuser
USER appuser
CMD ["python", "fetch_quakes.py"]