# Create your own docker file here
FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app 

RUN uv sync --frozen --no-cache

ENV PORT=8000
EXPOSE ${PORT}

LABEL maintainer="email-withheld"

CMD ["uv", "run", "fastapi", "run"]