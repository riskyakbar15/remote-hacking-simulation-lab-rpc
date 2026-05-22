from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
import time

TARGETS = {
    "node-1": {
        "ports": [
            {"port": 22, "service": "SSH", "status": "open"},
            {"port": 80, "service": "HTTP", "status": "open"},
            {"port": 443, "service": "HTTPS", "status": "open"},
        ],
        "vulnerabilities": ["Weak SSH Password", "Outdated Web Server"],
        "credential": {"username": "admin", "password": "12345"}
    },
    "node-2": {
        "ports": [
            {"port": 21, "service": "FTP", "status": "open"},
            {"port": 3306, "service": "MySQL", "status": "open"},
        ],
        "vulnerabilities": ["Anonymous FTP Enabled", "Weak Database Password"],
        "credential": {"username": "root", "password": "admin"}
    },
    "node-3": {
        "ports": [
            {"port": 8080, "service": "Web Server", "status": "open"},
        ],
        "vulnerabilities": ["Default Web Configuration"],
        "credential": {"username": "user", "password": "password"}
    },
}

LOGS = []

def add_log(action, target, status):
    LOGS.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "target": target,
        "status": status
    })

def ScanPort(target):
    time.sleep(1)

    if target not in TARGETS:
        add_log("ScanPort", target, "failed")
        return {"success": False, "message": "Target tidak ditemukan", "ports": []}

    add_log("ScanPort", target, "success")
    return {
        "success": True,
        "message": "Scan port berhasil",
        "target": target,
        "ports": TARGETS[target]["ports"]
    }

def BruteForceLogin(username, password, target):
    time.sleep(1)

    if target not in TARGETS:
        add_log("BruteForceLogin", target, "failed")
        return {"success": False, "message": "Target tidak ditemukan"}

    credential = TARGETS[target]["credential"]

    if username == credential["username"] and password == credential["password"]:
        add_log("BruteForceLogin", target, "success")
        return {"success": True, "message": "Simulasi login berhasil"}

    add_log("BruteForceLogin", target, "failed")
    return {"success": False, "message": "Simulasi login gagal"}

def CheckVulnerability(target):
    time.sleep(1)

    if target not in TARGETS:
        add_log("CheckVulnerability", target, "failed")
        return {"success": False, "message": "Target tidak ditemukan", "vulnerabilities": []}

    add_log("CheckVulnerability", target, "success")
    return {
        "success": True,
        "message": "Pengecekan vulnerability berhasil",
        "target": target,
        "vulnerabilities": TARGETS[target]["vulnerabilities"]
    }

def GetAttackLogs():
    return LOGS

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

server.register_function(ScanPort, "ScanPort")
server.register_function(BruteForceLogin, "BruteForceLogin")
server.register_function(CheckVulnerability, "CheckVulnerability")
server.register_function(GetAttackLogs, "GetAttackLogs")

print("RPC Server berjalan di http://localhost:8000")
print("Menunggu request dari client...")

server.serve_forever()