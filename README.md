# FinGraphRAG

[![CI](https://github.com/jatinmallarapu/FinGraphRAG/actions/workflows/ci.yml/badge.svg)](https://github.com/jatinmallarapu/FinGraphRAG/actions/workflows/ci.yml)

Compare three evidence retrieval strategies over filing fragments with page-level provenance.

## Architecture

```text
Filing fragments and sourced edges → lexical and graph retrieval → reciprocal rank fusion → ranked passages
```

## Verification

| Scope | What the tests cover |
| --- | --- |
| Local acceptance tests | Corpus checks, provenance, graph expansion, and rank fusion |
| Production benchmark | Pending |

## Quickstart

Python 3.11 or newer.

```sh
python fingraphrag.py "Northwind" --mode hybrid
python -m pip install -e '.[dev]'
make test
```

## Design and data

The supplied corpus uses fictional issuers. It demonstrates the contract without redistributing EDGAR filings.

[Requirements](specs/retrieval/requirements.md) · [Design](specs/retrieval/design.md) · [Tasks](specs/retrieval/tasks.md)

[Architecture decision](docs/adr/0001-local-baseline.md)

## Remaining milestones

EDGAR acquisition, PySpark parsing, image descriptions, vector storage, Neo4j, and the 150-question comparison.
