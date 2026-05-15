from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
import time

TARGETS = {
    "node-1": [
        {"port": 22, "service": "SSH", "status": "open"},
        {"port": 80, "service": "HTTP", "status": "open"},
        {"port": 443, "service": "HTTPS", "status": "open"},
    ],
    "node-2": [
        {"port": 21, "service": "FTP", "status": "open"},
        {"port": 3306, "service": "MySQL", "status": "open"},
    ],
    "node-3": [
        {"port": 8080, "service": "Web Server", "status": "open"},
    ],
}

def scan(target):
    time.sleep(1)

    if target not in TARGETS:
        return {
            "success": False,
            "message": "Target tidak ditemukan",
            "target": target,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ports": []
        }

    return {
        "success": True,
        "message": "Scan simulasi berhasil",
        "target": target,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ports": TARGETS[target]
    }

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_function(scan, "scan")

print("RPC Server berjalan di http://localhost:8000")
print("Menunggu request scan dari client...")

server.serve_forever()