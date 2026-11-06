"""5. Query processing: Boolean AND / OR / NOT (implicit AND between terms)."""
from .tokenizer import tokenize
from .normalizer import normalize
from .wildcard import expand


class QueryProcessor:
    def __init__(self, index, kgram_index, all_docs):
        self.index = index
        self.kgrams = kgram_index
        self.all_docs = set(all_docs)

    def postings(self, term):
        if "*" in term:
            matches = expand(term, self.kgrams, self.index.keys())
            return set().union(*(self.index[t] for t in matches)) if matches else set(), matches
        return set(self.index.get(term, [])), []

    def search(self, query):
        result, op, negate, expanded = None, "AND", False, {}
        for tok in tokenize(query):
            upper = tok.upper()
            if upper in ("AND", "OR"):
                op = upper
                continue
            if upper == "NOT":
                negate = True
                continue
            term = normalize(tok)
            docs, matches = self.postings(term)
            if matches:
                expanded[term] = matches
            if negate:
                docs, negate = self.all_docs - docs, False
            if result is None:
                result = docs
            elif op == "AND":
                result &= docs
            else:
                result |= docs
            op = "AND"
        return sorted(result or []), expanded
