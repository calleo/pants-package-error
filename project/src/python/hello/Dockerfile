FROM python:3.11.8-bookworm

COPY project.src.python.hello/bin.pex /app/hello.pex

RUN PEX_TOOLS=1 /app/hello.pex venv /app

CMD ["/app/hello.pex"]
