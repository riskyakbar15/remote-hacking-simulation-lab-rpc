from xmlrpc.client import ServerProxy, Fault, ProtocolError

server = ServerProxy("http://localhost:8000", allow_none=True)

print("=== Remote Hacking Simulation Lab RPC ===")
print("Target tersedia: node-1, node-2, node-3")

target = input("Masukkan target yang ingin di-scan: ")

try:
    result = server.scan(target)

    print("\n=== Hasil Scan ===")
    print("Target :", result["target"])
    print("Waktu  :", result["time"])
    print("Status :", result["message"])

    if result["success"]:
        print("\nPort terbuka:")
        for port in result["ports"]:
            print(f"- {port['port']} / {port['service']} / {port['status']}")
    else:
        print("Tidak ada data port.")

except ConnectionRefusedError:
    print("\nGagal terhubung ke server.")
    print("Pastikan server.py sudah dijalankan terlebih dahulu.")

except Fault as error:
    print("\nTerjadi kesalahan pada RPC server:")
    print(error)

except ProtocolError as error:
    print("\nTerjadi kesalahan protokol:")
    print(error)