FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./

RUN uv sync

COPY . .

CMD [ "uv","run","fastapi","dev","--host","0.0.0.0" ]
