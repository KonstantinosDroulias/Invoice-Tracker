FROM python:3.13-slim

# System deps: netcat for DB health-check, Node/npm for Tailwind CSS build
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python deps first (layer-cached unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App source
COPY . .

# Make scripts executable
RUN chmod +x entrypoint.sh build.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
