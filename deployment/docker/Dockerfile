FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "pipelines/python/generate_all_synthetic_data.py", "--claims", "1000"]
