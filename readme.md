
py -m venv .venv

.\.venv\Scripts\Activate.ps1

uvicorn main:app --reload

"git push <remote> <source>:<destination>"
