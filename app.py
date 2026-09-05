import os
from datetime import datetime

import psutil
from flask import Flask, jsonify, render_template


app = Flask(__name__)


def bytes_to_gib(value):
    return round(value / (1024 ** 3), 2)


def percent_status(percent):
    if percent >= 85:
        return "critical"
    if percent >= 70:
        return "warning"
    return "normal"


def get_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    cpu_percent = psutil.cpu_percent(interval=0.2)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": {
            "percent": cpu_percent,
            "cores": psutil.cpu_count(logical=True),
            "status": percent_status(cpu_percent),
        },
        "ram": {
            "percent": memory.percent,
            "used_gib": bytes_to_gib(memory.used),
            "total_gib": bytes_to_gib(memory.total),
            "available_gib": bytes_to_gib(memory.available),
            "status": percent_status(memory.percent),
        },
        "disk": {
            "percent": disk.percent,
            "used_gib": bytes_to_gib(disk.used),
            "total_gib": bytes_to_gib(disk.total),
            "free_gib": bytes_to_gib(disk.free),
            "status": percent_status(disk.percent),
        },
    }


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/metrics")
def metrics():
    return jsonify(get_metrics())


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
