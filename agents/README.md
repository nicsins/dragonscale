# Agents

Open models only. Ollama by default. OpenRouter if `OPENROUTER_API_KEY` is set.

## Use now

From the repo root:

```bash
python -m agents.cli --self-test
python -m agents.cli "write a python function that hashes a string with sha256"
```

`--self-test` does not call a model. It writes `data/selftest.db` and an encrypted profile under `data/profiles/`.

## Routing

| Task starts with / contains | Agent |
|---|---|
| `exec:` or `run:` | executor (Python after the colon is run locally) |
| code, function, python, script, bug | coder |
| anything else | researcher |

Ledger rows are hash-chained in sqlite (`LEDGER_PATH`, default `data/dragonscale.db`).
User notes stay in an encrypted file (`PROFILE_DIR`, default `data/profiles`).

## Env

```
OLLAMA_HOST=http://127.0.0.1:11434
DRAGONSCALE_MODEL=qwen2.5:7b
OPENROUTER_API_KEY=        # optional
OPENROUTER_MODEL=qwen/qwen-2.5-7b-instruct
FORCE_OLLAMA=1             # ignore OpenRouter even if the key is set
LEDGER_PATH=data/dragonscale.db
PROFILE_DIR=data/profiles
DRAGONSCALE_PROFILE_KEY=   # optional Fernet key; otherwise data/profiles/.profile.key
```
