"""4. Inverted index construction: term -> sorted list of doc ids."""
from .tokenizer import tokenize
from .normalizer import normalize_all


def build_index(docs):
    index = {}
    for doc_id, text in docs.items():
        for term in set(normalize_all(tokenize(text.replace("*", " ")))):
            index.setdefault(term, set()).add(doc_id)
    return {term: sorted(ids) for term, ids in index.items()}
