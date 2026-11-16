"""Compare sparse, graph, and fused retrieval while retaining filing provenance."""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Literal, TypedDict

Mode = Literal["lexical", "graph", "hybrid"]


class Chunk(TypedDict):
    id: str
    filing: str
    page: int
    element: str
    text: str


class Edge(TypedDict):
    left: str
    right: str
    source: str


def terms(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", value.casefold()))


def fuse(*rankings: list[str]) -> list[str]:
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        # A repeated ID within one retriever should contribute only once.
        for rank, identifier in enumerate(dict.fromkeys(ranking), 1):
            scores[identifier] += 1 / (60 + rank)
    return sorted(scores, key=lambda identifier: (-scores[identifier], identifier))


class Index:
    def __init__(self, chunks: list[Chunk], edges: list[Edge]) -> None:
        self.chunks = {chunk["id"]: chunk for chunk in chunks}
        if len(self.chunks) != len(chunks):
            raise ValueError("Duplicate chunk IDs")
        if any(edge["source"] not in self.chunks for edge in edges):
            raise ValueError("Edge has no source chunk")
        self.edges = edges
        self.lexicon = {key: terms(chunk["text"]) for key, chunk in self.chunks.items()}

    def query(self, question: str, mode: Mode = "hybrid", limit: int = 5) -> list[Chunk]:
        query = terms(question)
        lexical = sorted(self.lexicon, key=lambda key: (-len(query & self.lexicon[key]), key))
        lexical = [key for key in lexical if query & self.lexicon[key]]
        seeds = {
            name
            for edge in self.edges
            for name in (edge["left"], edge["right"])
            if terms(name) <= query and terms(name)
        }
        neighbors = {
            name
            for edge in self.edges
            if {edge["left"], edge["right"]} & seeds
            for name in (edge["left"], edge["right"])
        } - seeds
        ranked_edges = sorted(
            self.edges,
            key=lambda edge: (-int(bool({edge["left"], edge["right"]} & seeds)), edge["source"]),
        )
        graph = list(
            dict.fromkeys(
                edge["source"]
                for edge in ranked_edges
                if {edge["left"], edge["right"]} & (seeds | neighbors)
            )
        )
        ranked = {"lexical": lexical, "graph": graph, "hybrid": fuse(lexical, graph)}[mode]
        return [self.chunks[key] for key in ranked[:limit]]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question")
    parser.add_argument("--mode", choices=["lexical", "graph", "hybrid"], default="hybrid")
    parser.add_argument("--corpus", type=Path, default=Path("examples/filings.json"))
    args = parser.parse_args()
    data = json.loads(args.corpus.read_text(encoding="utf-8"))
    print(
        json.dumps(Index(data["chunks"], data["edges"]).query(args.question, args.mode), indent=2)
    )


if __name__ == "__main__":
    main()
