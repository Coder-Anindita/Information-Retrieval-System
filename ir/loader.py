"""1. Document loading: reads every .txt file in the corpus folder."""
import os


def load_documents(folder):
    docs = {}
    for name in sorted(os.listdir(folder)):
        if name.endswith(".txt"):
            with open(os.path.join(folder, name), encoding="utf-8") as f:
                docs[name] = f.read()
    return docs
