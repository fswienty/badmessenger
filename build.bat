@ECHO OFF
TITLE badmessenger build utility
ECHO ============================
ECHO BEGIN BUILD
ECHO ============================
:: use pyinstaller to build the program
:: --key=fj4j76od2km5if05
pyinstaller --onefile --add-data ".\\src\\messenger\\client_credentials.json;messenger" -y src\\badmessenger.py
ECHO ============================
ECHO BUILD FINISHED
ECHO ============================
PAUSE