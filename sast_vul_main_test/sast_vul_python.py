# sast_vul_python.py
import os
from flask import Flask, request

app = Flask(__name__)

@app.get("/run")
def run():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

if __name__ == "__main__":
    app.run()