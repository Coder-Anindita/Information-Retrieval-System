"""2. Tokenization: splits raw text into word tokens."""
import re


def tokenize(text):
    # words may contain letters, digits, hyphens; '*' kept for wildcard queries
    return re.findall(r"[A-Za-z0-9*]+(?:-[A-Za-z0-9*]+)*", text)
