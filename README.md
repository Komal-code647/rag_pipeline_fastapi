rag-fastapi-app/
│
├── app/
│   ├── main.py
│   ├── rag_pipeline.py
│
├── data/
│   └── chatdoctor.json
│   └── format_dataset.csv
│
├── requirements.txt
├── .env (ignore this file in git)
├── .gitignore
└── .github/
    └── workflows/
        └── ci.yml

## CI/CD Setup

The application uses lazy loading for the RAG pipeline to avoid model downloads during import tests. The HuggingFace model is loaded only when the `/ask` endpoint is called.

### GitHub Actions CI

To ensure the CI passes the import test, add the following step to download the required model:

```yaml
- name: Download HuggingFace model
  run: |
    pip install huggingface_hub
    huggingface-cli download sentence-transformers/all-MiniLM-L6-v2 --local-dir ~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2
```

This prevents `LocalEntryNotFoundError` during CI runs.
 