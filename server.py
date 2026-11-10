from flask import Flask, jsonify, send_from_directory
import psutil
import platform
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        "NEXUS.html"
    )

@app.route("/api/system")
def system_info():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    return jsonify({
        "cpu": psutil.cpu_percent(interval=0.3),
        "memory": memory.percent,
        "ram_total": round(memory.total / (1024**3), 2),
        "ram_used": round(memory.used / (1024**3), 2),
        "disk": disk.percent,
        "hostname": socket.gethostname(),
        "system": platform.system(),
        "processor": platform.processor()
    })

if __name__ == "__main__":
    print("NEXUS SERVER ONLINE")
    print("Acesse: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)