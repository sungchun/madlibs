FROM python:3.10.7-slim
ARG USERID=1001

RUN pip install pip==22.2.2
RUN pip install poetry==1.1.13

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


EXPOSE 5000
ENTRYPOINT ["poetry", "run"]
CMD flask run --host=0.0.0.0 --port=5000

