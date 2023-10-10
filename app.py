from flask import Flask, jsonify
import json
import subprocess

app = Flask(__name__)

@app.route("/")
def list():
    try:
        result = subprocess.run(['kubectl', 'get', 'pods','--all-namespaces','-o', 'jsonpath="{.items[*].spec.containers[*].image}"'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')

        result = result.split(" ")
        response = {
            "status": 200,
            "data": result
        }

        return jsonify(response)
    except Exception as e:
        result = {
            "status": 500,
            "data": [],
            "error": str(e)
        }
        return jsonify(result)
 
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)