# Filing retrieval comparison

An analyst needs to find evidence across filing text, tables and disclosed relationships.

| ID | Requirement | Acceptance criterion |
| --- | --- | --- |
| REQ-01 | Corpus integrity | GIVEN duplicate chunk IDs or an edge with a missing source WHEN loading THEN reject the corpus. |
| REQ-02 | Provenance | GIVEN a matching table chunk WHEN retrieved THEN return the filing, page and element type. |
| REQ-03 | Graph expansion | GIVEN a question naming an entity WHEN graph retrieval runs THEN return evidence from a one-hop neighbor. |
| REQ-04 | Hybrid retrieval | GIVEN two ranked lists WHEN fused THEN evidence that appears in both receives both rank contributions. |
