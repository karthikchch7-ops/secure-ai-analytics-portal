FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir streamlit requests
COPY dashboard /app/dashboard
WORKDIR /app/dashboard
EXPOSE 8501
CMD ["streamlit","run","app.py","--server.port","8501","--server.address","0.0.0.0"]
