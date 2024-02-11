python -m venv env
call env/scripts/activate
pip install pyinstaller
pyinstaller --onefile  --console main.py
cmd