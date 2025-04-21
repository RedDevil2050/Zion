# Multi-stage build for Adam Alpha
FROM python:3.10-slim AS builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
RUN useradd --create-home appuser
USER appuser
EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:8501/health || exit 1
CMD ["python3", "run_all.py"]
