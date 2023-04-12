FROM python:3.9-slim AS builder
RUN python -m pip install pdm
RUN pdm config python.use_venv false

COPY pyproject.toml pdm.lock /project/
WORKDIR /project
RUN pdm install --prod --no-lock --no-editable

FROM python:3.9-slim AS bot
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    sqlite3 \
    libfribidi0 \
    libraqm0 && \
    apt-get autoclean -y && \
    apt-get autoremove -y

ENV PYTHONPATH=/project/pkgs

COPY src/ /project/pkgs/

COPY --from=builder /project/__pypackages__/3.9/lib /project/pkgs
WORKDIR /project
ENTRYPOINT [ "python", "-m", "latentbot" ]
