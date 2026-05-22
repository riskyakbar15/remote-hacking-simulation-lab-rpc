from xmlrpc.client import ServerProxy

server = ServerProxy("http://localhost:8000", allow_none=True)

def menu():
    print("\n=== Remote Hacking Simulation Lab RPC ===")
    print("Target tersedia: node-1, node-2, node-3")
    print("1. Scan Port")
    print("2. Brute Force Login Simulation")
    print("3. Check Vulnerability")
    print("4. Get Attack Logs")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        target = input("Masukkan target: ")
        result = server.ScanPort(target)

        print("\n=== Hasil Scan Port ===")
        print("Status:", result["message"])

        if result["success"]:
            print("Target:", result["target"])
            print("Port terbuka:")
            for port in result["ports"]:
                print(f"- {port['port']} / {port['service']} / {port['status']}")

    elif pilihan == "2":
        target = input("Masukkan target: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        result = server.BruteForceLogin(username, password, target)

        print("\n=== Hasil Brute Force Simulation ===")
        print("Status:", result["message"])

    elif pilihan == "3":
        target = input("Masukkan target: ")
        result = server.CheckVulnerability(target)

        print("\n=== Hasil Vulnerability Check ===")
        print("Status:", result["message"])

        if result["success"]:
            print("Target:", result["target"])
            print("Vulnerability ditemukan:")
            for vuln in result["vulnerabilities"]:
                print(f"- {vuln}")

    elif pilihan == "4":
        logs = server.GetAttackLogs()

        print("\n=== Attack Logs ===")

        if len(logs) == 0:
            print("Belum ada log.")
        else:
            for log in logs:
                print(f"- {log['time']} | {log['action']} | {log['target']} | {log['status']}")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")