# 🧾 ArenaVS Multi-Akun Task Completer 
https://launchpad.arenavs.com/?start=b9213742-f599-49fa-a9ae-8dc06ff79c14

Script Python ini digunakan untuk **menyelesaikan semua task ArenaVS** secara otomatis menggunakan **banyak akun** dari file `wallets.txt`.

---

## ⚙️ Fitur

- ✅ Multi-akun dari `wallets.txt`
- ✍️ Mengerjakan semua `task_id` yang sudah ditentukan
- 🗂️ Memisahkan hasil ke:
  - `completed_tasks.txt` → task berhasil
  - `failed_tasks.txt` → task gagal
- ✂️ Token ditampilkan sebagian (demi keamanan)
- 🛑 Aman jika dihentikan dengan `Ctrl+C` (`KeyboardInterrupt`)

---

## 📁 Struktur File

### 1. `wallets.txt`

Isi file ini dengan token JWT satu per baris, **tanpa prefix `Bearer`**.

Contoh:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token_akun_1...
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token_akun_2...
```

---

## ▶️ Cara Menjalankan

Jalankan dengan Python 3:

```bash
python main.py
```

---

## 🧯 Jika Muncul `❌` (Gagal Menyelesaikan Task)

Output seperti ini:

```
❌ [eyJhbGciOi...] Follow GPT360 on X
❌ [eyJhbGciOi...] Join ArenaVS Discord
```

Berarti kamu **belum melakukan aksi yang diminta**, misalnya:

- Belum follow akun X (Twitter)
- Belum join Discord
- Belum subscribe Telegram
- Belum retweet/like

### ✅ Solusinya:

1. Buka link task secara manual dan lakukan aksi tersebut (follow, join, dst)
2. Setelah semua selesai, **jalankan kembali `main.py`**
3. Jika berhasil, task akan pindah ke `✅ completed_tasks.txt`

---

## 📂 Output

### `completed_tasks.txt`
Berisi daftar task yang berhasil dikerjakan:
```
TOKEN: eyJhbGciOi... TASK: Follow GPT360 on X
```

### `failed_tasks.txt`
Berisi task yang gagal dikerjakan:
```
TOKEN: eyJhbGciOi... TASK: Join GPT360 Discord
```

---

## 💡 Tips

- Jalankan berkali-kali setelah menyelesaikan manual task
- Jangan edit token jika tidak yakin
- Gunakan hanya untuk akun kamu sendiri

---

## 📜 Lisensi

Script ini bersifat open & bebas digunakan untuk edukasi dan keperluan pribadi.  
Harap digunakan dengan etika dan tanggung jawab.
