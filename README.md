# AI File Automation Tool (Streamlit)

Sebuah tool berbasis web yang dibangun menggunakan Streamlit untuk membantu otomatisasi tugas-tugas manajemen file umum. Proyek ini dibuat sebagai bagian dari portofolio untuk menunjukkan kemampuan dalam pengembangan aplikasi Python dan penggunaan Streamlit.

## Fitur

-   **Rename Files**: Mengubah nama banyak file secara batch dengan opsi prefix, suffix, dan penomoran otomatis.
-   **Sort Files**: Mengelompokkan file ke dalam folder berdasarkan ekstensinya. Output berupa file ZIP.
-   **Compress Files**: Mengompres beberapa file menjadi satu arsip ZIP.
-   **Extract Text from PDF**: Mengekstrak konten teks dari file PDF.

## Teknologi yang Digunakan

-   **Python**: Bahasa pemrograman utama.
-   **Streamlit**: Framework untuk membangun aplikasi web interaktif.
-   **PyPDF2**: Library untuk manipulasi PDF (ekstraksi teks).
-   **Git & GitHub**: Untuk version control dan hosting kode.
-   **Gitpod**: Untuk lingkungan pengembangan berbasis cloud.
-   **Hugging Face Spaces**: Untuk deployment aplikasi.

## Cara Menjalankan Lokal (misalnya dengan Gitpod)

1.  Clone repository ini atau buka langsung di Gitpod.
2.  Pastikan Python 3.8+ terinstal.
3.  Buat virtual environment (opsional tapi direkomendasikan):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Jalankan aplikasi Streamlit:
    ```bash
    streamlit run app.py
    ```
6.  Buka browser dan navigasi ke URL yang ditampilkan (biasanya `http://localhost:8501`).

## Deployment

Aplikasi ini di-deploy dan dapat diakses melalui Hugging Face Spaces:
[https://huggingface.co/spaces/bagaseptian/ai-file-automation]

## Kontribusi

Saran dan kontribusi selalu diterima! Silakan buat issue atau pull request.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).