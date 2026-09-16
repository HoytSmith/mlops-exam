# Create your own docker file here
FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app 

RUN uv sync --frozen --no-cache

RUN --mount=type=secret,id=SECRET,env=SECRET

ENV PORT=8000
EXPOSE ${PORT}

LABEL maintainer=hoyt.smith@itvitaelearning.nl

CMD ["uv", "run", "fastapi", "run"]