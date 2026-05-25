# Remote Hacking Simulation Lab RPC

Proyek ini merupakan implementasi sederhana **Remote Procedure Call (RPC)** menggunakan Python untuk mata kuliah **Sistem Terdistribusi**. Sistem ini dibuat sebagai simulasi laboratorium keamanan jaringan dengan berbagai fitur simulasi seperti **port scanning**, **brute force login**, dan **vulnerability checking**.

> Catatan: Proyek ini tidak melakukan aksi peretasan atau scanning jaringan secara nyata. Semua data target dan hasil simulasi bersifat statis (dummy) agar aman digunakan untuk pembelajaran konsep RPC.

## Deskripsi Proyek

**Remote Hacking Simulation Lab RPC** adalah aplikasi berbasis client-server yang mendemonstrasikan bagaimana client dapat memanggil berbagai fungsi keamanan yang berjalan di server secara remote menggunakan protokol XML-RPC.

Terdapat dua versi dalam proyek ini:

1. **Versi Utama (`server.py` & `client.py`)**: Memiliki fitur lengkap dengan menu interaktif.
2. **Versi Sederhana (`serverOneService.py` & `clientOneService.py`)**: Hanya memiliki satu fungsi (scan port) untuk pemahaman dasar.

## Tujuan Proyek

Tujuan dari proyek ini adalah:

- Mengimplementasikan konsep Remote Procedure Call pada sistem terdistribusi.
- Menunjukkan komunikasi antara client dan server menggunakan RPC.
- Membuat simulasi aktivitas keamanan jaringan secara aman.
- Memahami proses request dan response dalam sistem client-server.

## Fitur

Fitur-fitur utama yang tersedia pada versi lengkap:

1. **Scan Port**: Simulasi pemindaian port terbuka pada target tertentu (node-1, node-2, node-3).
2. **Brute Force Login Simulation**: Simulasi percobaan login dengan username dan password pada target.
3. **Check Vulnerability**: Melihat kerentanan yang ada pada target berdasarkan basis data simulasi di server.
4. **Get Attack Logs**: Mengambil catatan aktivitas (log) yang telah dilakukan selama sesi berjalan.

## Teknologi yang Digunakan

Proyek ini menggunakan:

- Python 3
- XML-RPC
- Library bawaan Python:
  - `xmlrpc.server`
  - `xmlrpc.client`
  - `datetime`
  - `time`

Karena menggunakan library bawaan Python, proyek ini tidak membutuhkan instalasi package tambahan.

## Struktur Proyek

```text
remote-hacking-simulation-lab-rpc/
│
├── server.py               # (Utama) Server dengan fitur lengkap
├── client.py               # (Utama) Client dengan menu interaktif
├── serverOneService.py      # (Simpel) Server dengan satu layanan scan
├── clientOneService.py      # (Simpel) Client untuk satu layanan scan
└── README.md               # Dokumentasi proyek
```

## Alur Sistem

Alur kerja sistem (Versi Utama) adalah sebagai berikut:

```text
Client (Menu)
  |
  | Pilih Aksi (1-4)
  v
RPC Server (server.py)
  |
  | Mengeksekusi fungsi:
  | - ScanPort(target)
  | - BruteForceLogin(u, p, target)
  | - CheckVulnerability(target)
  | - GetAttackLogs()
  v
Data Simulasi (Target & Logs)
  |
  | Mengirim respons (JSON/Struct)
  v
Client menampilkan visualisasi hasil
```

Penjelasan singkat:

1. User menjalankan `client.py`.
2. User memilih aksi dari menu (misal: Scan Port).
3. Client meminta input tambahan (misal: target `node-1`).
4. Client memanggil fungsi yang sesuai pada server melalui protokol XML-RPC.
5. Server memproses permintaan dan mengembalikan data terstruktur.
6. Client menampilkan hasil simulasi ke terminal.

## Cara Menjalankan Proyek

### 1. Persiapan

Pastikan Anda sudah menginstal Python 3. Clone atau buat folder proyek dan pastikan file berikut tersedia:

- `server.py`
- `client.py`

### 2. Jalankan Server

Buka terminal pertama, lalu jalankan:

```bash
python server.py
```

Output jika berhasil:

```text
RPC Server berjalan di http://localhost:8000
Menunggu request dari client...
```

### 3. Jalankan Client

Buka terminal kedua, lalu jalankan:

```bash
python client.py
```

Anda akan disuguhkan menu interaktif untuk melakukan simulasi hacking.

### 4. Opsional: Versi Satu Layanan

Jika ingin mencoba versi yang lebih sederhana, gunakan:

- Terminal 1: `python serverOneService.py`
- Terminal 2: `python clientOneService.py`

## Contoh Output (Versi Utama)

### Simulasi Scan Port

```text
=== Hasil Scan Port ===
Status: Scan port berhasil
Target: node-1
Port terbuka:
- 22 / SSH / open
- 80 / HTTP / open
- 443 / HTTPS / open
```

### Simulasi Log Aktivitas

```text
=== Attack Logs ===
- 2026-05-25 10:00:01 | ScanPort | node-1 | success
- 2026-05-25 10:00:15 | BruteForceLogin | node-2 | failed
```

## Penjelasan Konsep RPC

RPC atau **Remote Procedure Call** adalah mekanisme yang memungkinkan sebuah program memanggil fungsi atau prosedur yang berjalan di komputer atau proses lain seolah-olah fungsi tersebut berada di program lokal.

Pada proyek ini, fungsi `ScanPort()` berada di server. Namun, client dapat memanggil fungsi tersebut menggunakan:

```python
result = server.ScanPort(target)
```

Meskipun terlihat seperti pemanggilan fungsi biasa, sebenarnya fungsi tersebut dijalankan di server melalui komunikasi jaringan.

## Bagian RPC pada Program

Pada server, fungsi-fungsi didaftarkan agar bisa diakses oleh client:

```python
server.register_function(ScanPort, "ScanPort")
server.register_function(BruteForceLogin, "BruteForceLogin")
```

Pada client, fungsi tersebut dipanggil melalui objek `ServerProxy`:

```python
result = server.ScanPort(target)
result = server.BruteForceLogin(username, password, target)
```

```python
server = ServerProxy("http://localhost:8000", allow_none=True)
result = server.ScanPort(target)
```

Inilah bagian utama yang menunjukkan implementasi RPC pada proyek ini.

## Batasan Proyek

Proyek ini memiliki beberapa batasan:

- Data target dan port bersifat statis (dummy) di dalam kode server.
- Tidak melakukan scanning jaringan nyata.
- Belum menggunakan database untuk menyimpan log atau data target secara permanen.
- Masih berupa aplikasi berbasis terminal (CLI).
- Komunikasi RPC masih dikonfigurasi pada localhost (namun dapat dikembangkan ke jaringan nyata).

## Aspek Keamanan dan Etika

Proyek ini dibuat hanya untuk tujuan pembelajaran. Sistem tidak dirancang untuk melakukan aktivitas hacking, scanning jaringan publik, eksploitasi celah keamanan, atau pengambilan data sensitif.

Seluruh hasil scan merupakan data simulasi yang telah ditentukan di dalam kode server.

---

Made With ❤️ By [riskyakbar15](https://github.com/riskyakbar15) For Education.
