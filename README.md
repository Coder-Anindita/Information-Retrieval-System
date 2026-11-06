# Information-Retrieval-System

A simple Boolean document retrieval system with wildcard support (WSM assignment).

## Modules
| Module | Purpose |
|---|---|
| `ir/loader.py` | Document loading |
| `ir/tokenizer.py` | Tokenization |
| `ir/normalizer.py` | Text normalization / case folding |
| `ir/indexer.py` | Inverted index construction |
| `ir/query.py` | Query processing (AND, OR, NOT) |
| `ir/wildcard.py` | Wildcard processing (bigram index) |
| `app.py` + `templates/index.html` | Frontend GUI (Flask) |

`corpus/` holds 20 text documents.

## Run
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Example queries
`retrieval`, `comp*`, `*tion`, `search OR crawler`, `index AND NOT wildcard`
