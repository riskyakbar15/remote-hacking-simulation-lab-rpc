# Remote Hacking Simulation Lab RPC

Proyek ini merupakan implementasi sederhana **Remote Procedure Call (RPC)** menggunakan Python untuk mata kuliah **Sistem Terdistribusi**. Sistem ini dibuat sebagai simulasi laboratorium keamanan jaringan dengan fitur utama berupa **scan target** secara dummy/simulasi.

> Catatan: Proyek ini tidak melakukan scanning jaringan secara nyata. Semua data target dan port bersifat simulasi agar aman digunakan untuk pembelajaran.

## Deskripsi Proyek

**Remote Hacking Simulation Lab RPC** adalah aplikasi sederhana berbasis client-server yang memperlihatkan bagaimana client dapat memanggil fungsi yang berjalan di server menggunakan konsep RPC.

Pada proyek ini, client mengirim nama target ke server. Server kemudian menjalankan fungsi `scan()` dan mengembalikan hasil simulasi berupa daftar port terbuka pada target tersebut.

## Tujuan Proyek

Tujuan dari proyek ini adalah:

- Mengimplementasikan konsep Remote Procedure Call pada sistem terdistribusi.
- Menunjukkan komunikasi antara client dan server menggunakan RPC.
- Membuat simulasi scan target secara aman tanpa melakukan scanning jaringan asli.
- Memahami proses request dan response dalam sistem client-server.

## Fitur

Fitur utama pada proyek ini adalah:

- Scan target secara simulasi.
- Pemanggilan fungsi jarak jauh dari client ke server.
- Data port dummy untuk beberapa target.
- Response dalam bentuk data terstruktur.
- Penanganan target yang tidak ditemukan.

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
├── server.py
├── client.py
└── README.md
```

Keterangan:

- `server.py` berisi kode RPC server dan fungsi scan.
- `client.py` berisi kode client untuk memanggil fungsi scan pada server.
- `README.md` berisi dokumentasi proyek.

## Alur Sistem

Alur kerja sistem adalah sebagai berikut:

```text
Client
  |
  | Memanggil fungsi scan(target)
  v
RPC Server
  |
  | Memproses target
  v
Data Simulasi Port
  |
  | Mengirim hasil scan
  v
Client menampilkan hasil
```

Penjelasan singkat:

1. User menjalankan `client.py`.
2. User memasukkan nama target, misalnya `node-1`.
3. Client memanggil fungsi `scan()` pada server menggunakan RPC.
4. Server memeriksa data target.
5. Server mengembalikan hasil scan simulasi.
6. Client menampilkan hasil scan ke terminal.

## Cara Menjalankan Proyek

### 1. Clone atau Siapkan Folder Proyek

Buat folder proyek:

```bash
mkdir remote-hacking-simulation-lab-rpc
cd remote-hacking-simulation-lab-rpc
```

Masukkan file berikut ke dalam folder tersebut:

```text
server.py
client.py
README.md
```

### 2. Jalankan Server

Buka terminal pertama, lalu jalankan:

```bash
python server.py
```

Jika berhasil, akan muncul output seperti berikut:

```text
RPC Server berjalan di http://localhost:8000
Menunggu request scan dari client...
```

### 3. Jalankan Client

Buka terminal kedua, lalu jalankan:

```bash
python client.py
```

Kemudian masukkan target yang ingin di-scan.

Target yang tersedia:

```text
node-1
node-2
node-3
```

Contoh input:

```text
Masukkan target yang ingin di-scan: node-1
```

## Contoh Output

Jika user memasukkan target `node-1`, maka output yang muncul adalah:

```text
=== Remote Hacking Simulation Lab RPC ===
Target tersedia: node-1, node-2, node-3
Masukkan target yang ingin di-scan: node-1

=== Hasil Scan ===
Target : node-1
Waktu  : 2026-05-15 20:30:12
Status : Scan simulasi berhasil

Port terbuka:
- 22 / SSH / open
- 80 / HTTP / open
- 443 / HTTPS / open
```

Jika target tidak ditemukan, maka output yang muncul adalah:

```text
=== Hasil Scan ===
Target : node-10
Waktu  : 2026-05-15 20:31:45
Status : Target tidak ditemukan
Tidak ada data port.
```

## Penjelasan Konsep RPC

RPC atau **Remote Procedure Call** adalah mekanisme yang memungkinkan sebuah program memanggil fungsi atau prosedur yang berjalan di komputer atau proses lain seolah-olah fungsi tersebut berada di program lokal.

Pada proyek ini, fungsi `scan()` berada di server. Namun, client dapat memanggil fungsi tersebut menggunakan:

```python
result = server.scan(target)
```

Meskipun terlihat seperti pemanggilan fungsi biasa, sebenarnya fungsi tersebut dijalankan di server melalui komunikasi jaringan.

## Bagian RPC pada Program

Pada server, fungsi `scan()` didaftarkan sebagai fungsi RPC:

```python
server.register_function(scan, "scan")
```

Pada client, fungsi tersebut dipanggil melalui objek `ServerProxy`:

```python
server = ServerProxy("http://localhost:8000", allow_none=True)
result = server.scan(target)
```

Inilah bagian utama yang menunjukkan implementasi RPC pada proyek ini.

## Batasan Proyek

Proyek ini memiliki beberapa batasan:

- Hanya mendukung satu fitur, yaitu scan target.
- Data target dan port masih bersifat dummy.
- Tidak melakukan scanning jaringan nyata.
- Belum menggunakan database.
- Belum memiliki tampilan web atau dashboard.
- Komunikasi masih berjalan pada localhost.

## Aspek Keamanan dan Etika

Proyek ini dibuat hanya untuk tujuan pembelajaran. Sistem tidak dirancang untuk melakukan aktivitas hacking, scanning jaringan publik, eksploitasi celah keamanan, atau pengambilan data sensitif.

Seluruh hasil scan merupakan data simulasi yang telah ditentukan di dalam kode server.

---

Made With ❤️ By [riskyakbar15](https://github.com/riskyakbar15) For Education.
