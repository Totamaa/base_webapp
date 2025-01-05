### STAGE 1: Build ###
FROM python:3.12 AS builder
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


### STAGE 2: Production Environment ###
FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /install /usr/local

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

