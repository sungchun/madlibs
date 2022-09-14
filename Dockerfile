FROM python:3.10.7-slim
ARG USERID=1001

RUN pip install pip==22.2.2
RUN pip install poetry==1.2.0

RUN useradd -u $USERID -m projuser
USER projectuser
WORKDIR /src

COPY --chown=projuser:projuser pyproject.toml .
COPY --chown=projuser:projuser poetry.lock .

RUN poetry install

COPY --chown=projuser:projuser README.md .
COPY --chown=projuser:projuser app/ .
COPY --chown=projuser:projuser tests/ .

ENTRYPOINT [ "poetry shell", "app/populate_tables.py" ]
