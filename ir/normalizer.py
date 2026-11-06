"""3. Text normalization / case folding."""


def normalize(token):
    return token.lower().replace("-", "")


def normalize_all(tokens):
    return [t for t in (normalize(x) for x in tokens) if t]
