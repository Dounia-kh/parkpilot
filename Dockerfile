FROM python:3.12-slim

ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}

WORKDIR /app

COPY . .

RUN useradd -m parker && chown -R parker:parker /app

USER parker

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8000/health')"

CMD ["python", "app.py"]