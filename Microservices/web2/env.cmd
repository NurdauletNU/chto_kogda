python -m venv env
call env/scripts/activate
pip install fastapi
pip install aiohttp
pip install uvicorn
uvicorn main:app --reload --port=8002


cmd