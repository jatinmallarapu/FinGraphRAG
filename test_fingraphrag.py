"""Verify graph expansion and prove retrieval preserves source coordinates."""

import json
from pathlib import Path

import pytest

from fingraphrag import Index, fuse


def fixture() -> dict:
    return json.loads(Path("examples/filings.json").read_text(encoding="utf-8"))


def test_REQ_01_invalid_corpus() -> None:
    data = fixture()
    with pytest.raises(ValueError, match="Duplicate"):
        Index(data["chunks"] * 2, data["edges"])
    with pytest.raises(ValueError, match="no source"):
        Index([], data["edges"])


def test_REQ_02_provenance() -> None:
    data = fixture()
    row = Index(**data).query("Northwind supplier", "lexical")[0]
    assert (row["filing"], row["page"], row["element"]) == ("Fictional Northwind 10-K", 12, "table")


def test_REQ_03_neighbor_evidence() -> None:
    assert [row["id"] for row in Index(**fixture()).query("Northwind", "graph")] == ["a", "b"]


def test_REQ_04_fusion() -> None:
    assert fuse(["a", "b"], ["c", "b"]) == ["b", "a", "c"]
