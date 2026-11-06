"""6. Wildcard processing using a bigram (k=2) index with '$' boundaries."""
import re


def build_kgram_index(vocabulary, k=2):
    kgrams = {}
    for term in vocabulary:
        padded = f"${term}$"
        for i in range(len(padded) - k + 1):
            kgrams.setdefault(padded[i:i + k], set()).add(term)
    return kgrams


def expand(pattern, kgram_index, vocabulary, k=2):
    """Return all vocabulary terms matching a pattern like 'comp*' or '*tion'."""
    grams = set()
    for part in f"${pattern}$".split("*"):
        grams.update(part[i:i + k] for i in range(len(part) - k + 1))
    if grams:
        candidates = set.intersection(*(kgram_index.get(g, set()) for g in grams))
    else:
        candidates = set(vocabulary)  # pattern was just '*'
    regex = re.compile("^" + ".*".join(map(re.escape, pattern.split("*"))) + "$")
    return sorted(t for t in candidates if regex.match(t))  # post-filter false positives
