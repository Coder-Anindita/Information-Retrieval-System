"""7. Frontend GUI (Flask web app)."""
import os
from flask import Flask, render_template, request

from ir.loader import load_documents
from ir.indexer import build_index
from ir.wildcard import build_kgram_index
from ir.query import QueryProcessor

BASE = os.path.dirname(os.path.abspath(__file__))
docs = load_documents(os.path.join(BASE, "corpus"))
index = build_index(docs)
qp = QueryProcessor(index, build_kgram_index(index.keys()), docs.keys())

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    query = request.form.get("query", "").strip()
    output = ""
    if query:
        hits, expanded = qp.search(query)
        lines = [f"Query: {query}"]
        for term, matches in expanded.items():
            lines.append(f"Wildcard '{term}' -> {', '.join(matches)}")
        lines.append(f"{len(hits)} document(s) found\n")
        for d in hits:
            lines.append(f"[{d}]\n  {docs[d].strip()}\n")
        output = "\n".join(lines)
    return render_template("index.html", query=query, output=output, n=len(docs), v=len(index))


if __name__ == "__main__":
    app.run(debug=True)
