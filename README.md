# aiact-ontology
LLM-assisted pipeline (ChatGPT + RDFLib) to generate an OWL ontology for the EU AI Act.

This repository contains the code, prompts, and artifacts used to generate a hierarchical ontology of the EU Artificial Intelligence Act (Regulation (EU) 2024/1689) using an LLM-assisted pipeline (ChatGPT) and rdflib.

## Repository layout

```
/aiact-ontology-repo/
├── README.md
├── requirements.txt
├── prompts/
│   └── domain_spec_prompt.txt
├── scripts/
│   └── hierarchy_from_rdflib.py
├── data/
├── outputs/
└── appendix/
```

## Quickstart (local)

1. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate     # Windows PowerShell
pip install -r requirements.txt
```

2. Edit `scripts/hierarchy_from_rdflib.py` to set `INPUT_PATH` and `OUTPUT_*` paths and (if needed) expand the `structure` dictionary with the full chapters and articles.

3. Run the hierarchy builder

```bash
python scripts/hierarchy_from_rdflib.py
```

4. The outputs will be written to the `OUTPUT_TTL` and `OUTPUT_OWL` paths configured in the script.

## Prompts

Prompt templates used for LLM calls are in `prompts/domain_spec_prompt.txt` — copy them to your LLM client and replace `{{PLACEHOLDER}}` tokens before running.

## Requirements

Put the following (example) in `requirements.txt`:

```
openai==0.27.0
rdflib==6.4.0
lxml
python-dotenv
```

## Git push example

```bash
git init
git add .
git commit -m "Initial import: hierarchy script + prompts + README"
# create repo on GitHub and then
git remote add origin git@github.com:your-username/aiact-ontology.git
git branch -M main
git push -u origin main
```

## License & contact

Choose a license (e.g., MIT) and add `LICENSE` to the repo. For questions contact: `charikleia.spanou@example.edu` (replace with your email).
