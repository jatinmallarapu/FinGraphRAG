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

On the bundled two-document fixture, querying `Northwind` returned chunk `a` in lexical mode and chunks `a` and `b` in both graph and hybrid modes. Chunk `b` describes the supplier's assembly-site dependency without mentioning Northwind. This demonstrates the relationship path the comparison is designed to test at larger scale.

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
