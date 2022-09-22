FROM python:3.10.7-slim
ARG USERID=1001

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
      bash \
      curl \
      g++ \
      libpcre3 \
      libpcre3-dev \
      libpq-dev \
      python3-dev \
      && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pip==22.2.2
RUN pip install poetry==1.2.1

RUN useradd -u $USERID -m projuser
USER projuser
RUN mkdir /home/projuser/src
RUN  chown projuser:projuser /home/projuser/src
WORKDIR /home/projuser/src

COPY --chown=projuser:projuser pyproject.toml .
COPY --chown=projuser:projuser poetry.lock .

RUN poetry config virtualenvs.in-project true
RUN poetry install

COPY --chown=projuser:projuser app ./app
COPY --chown=projuser:projuser tests ./tests
COPY --chown=projuser:projuser run.py .
COPY --chown=projuser:projuser migrations ./migrations

EXPOSE 5000
ENTRYPOINT ["poetry", "run"]
CMD flask run --host=0.0.0.0 --port=5000

