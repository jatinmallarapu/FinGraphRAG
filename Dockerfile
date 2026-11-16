# Ship the fingraphrag CLI and its reproducible example as a nonroot image.
FROM python:3.11-slim
WORKDIR /app
COPY README.md pyproject.toml fingraphrag.py ./
COPY examples/ examples/
RUN python -m pip install --no-cache-dir .
USER 10001
CMD ["python","fingraphrag.py","Northwind","--mode","hybrid"]
