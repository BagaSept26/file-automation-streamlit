# Ini library utama untuk buat UI web
import streamlit as st
import os # untuk operasi file sistem seperti rename, list directory
import shutil # untuk oerasi file level tinggi seperti copy, move, remove tree
import zipfile #kompres dan ektrasi zip
from PyPDF2 import PdfReader
from io import BytesIO

#conf halaman
st.set_page_config(layout="wide", page_title="AI File Automation Tool", page_icon="🤖")

#func
def create_zip_in_memory(files_data):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file_info in files_data:
            zip_file.writestr(file_info['name'], file_info['data'])
        zip_buffer.seek(0)
        return zip_buffer

# --- UI Aplikasi --
st.title("🤖 AI File Automation Tool")
st.write("Solusi untuk manajemen file, Rename, Sort, compress, dan ektrak teks dari PDF dengan mudah")

#sidebar nav
st.sidebar.title("Fitur Tersedia")
feature_options = ["🏠 Halaman Utama", "🔄 Rename Files", "🗂️ Sort Files", "📦 Compress Files", "📄 Extract Text from PDF"]
selected_feature = st.sidebar.selectbox("Pilih Fitur:", feature_options)

# --- Logika untuk tiap fitur --
if selected_feature == "🏠 Halaman Utama":
    st.header("Selamat Datang")
    st.markdown("""
    Tool ini dirancang untuk membantu mengelola file dengan lebih efisien.
    Gunakan menu di sidebar kiri untuk memilih fitur yang dibutuhkan.
    
    **Fitur yang tersedia:**
    - **Rename Files:** Ubah nama banyak file sekaligus dengan pola tertentu.
    - **Sort Files:** Kelompokan file  ke dalam folder berdasarkan kriteria (misalnya, ekstensi)
    - **Compress Files:** Kompres file menjadi format ZIP untuk menghemat ruang atau memudahkan pengiriman
    - **Extract Text from PDF:** Ambil teks dari file PDF.
    
    Semoga bermanfaat!
    """)

elif selected_feature == "🔄 Rename Files":
    st.header("🔄 Rename Files")
    st.write("Upload file yang ingin anda rename.")

    uploaded_files = st.file_uploader("Pilih file...", accept_multiple_files=True, key="rename_uploader")

    if uploaded_files:
        st.subheader("Opsi Rename:")
        col1, col2 = st.columns(2)
        with col1:
            prefix = st.text_input("Tambahkan Prefix (opsional):", key="rename_prefix")
            suffix = st.text_input("Tambahkan Suffix (optional):", key="rename_suffix")
            with col2:
                use_numbering = st.checkbox("Tambahkan Nomor urut", value=True, key="rename_numbering")
                start_number = st.number_input("Mulai Nomor Dari:", min_value=1, value=1, step=1, disabled=not use_numbering, key="rename_start_num")
            if st.button("Proses Rename Files", key="rename_button"):
                renamed_files_data = [] #menyimpan data yang akan di zip

                for i, uploaded_files in enumerate(uploaded_files):
                    original_name = uploaded_files.name
                    base, ext = os.path.splitext(original_name)

                    new_name_parts = []
                    if prefix:
                        new_name_parts.append(prefix)
                    new_name_parts.append(base) #bagian nama asli tanpa ekstensi

                    if suffix:
                        new_name_parts.append(suffix)
                    if use_numbering:
                        new_name_parts.append(f"_{start_number + i:03d}") #format nomor
                    new_name = "".join(new_name_parts) + ext

                    #simpan nama baru dan daya byte-nya untuk di-zip
                    renamed_files_data.append({"name": new_name, "data": uploaded_file.getvalue()})
                    st.write(f"'{original_name}'akan direname menjadi '{new_name}'")

                if renamed_files_data:
                    zip_buffer = create_zip_in_memory(renamed_files_data)
                    st.download_button(
                        label="📥 Download Renamed Files (ZIP)",
                        data=zip_buffer,
                        file_name="renamed_files.zip",
                        mime="application/zip",
                        key="download_renamed"
                    ) 
                    st.success("File berhasil diproses dan siap di-download sebagai ZIP!")

elif selected_feature == "🗂️ Sort Files":
    st.header("🗂️ Sort Files")
    st.write("Upload file yang anda ingin sort berdasrkan ekstensinya.")

    uploaded_files = st.file_uploader("Pilih file...", accept_multiple_files=True, key="sort_upploader")

    if uploaded_files:
        if st.button("Proses Sort Files", key="sort-button"):
            sorted_files_data = [] #menyimpan file yang akan dizip ddengan struktur foder
            # st.write("Memproses File...") #feeback sementara

            for uploaded_file in uploaded_files:
                original_name = uploaded_file.name
                #dapatkan ekstensi, hilakngkan titik di depan jika ada
                _, ext = os.path.splitext(original_name)
                folder_name = ext[1:].lower() if ext else "no_extension"

                #path di dalam zip akan menjadi 'nama_folder_ekstensi/ nama_file_asli
                zip_path = os.path.join(folder_name, original_name)
                sorted_files_data.append({"name": zip_path, "data": uploaded_file.getvalue()})
                st.write(f"'{original_name}' akan ditempatkan di folder '{folder_name}'")
            
            if sorted_files_data:
                zip_buffer = create_zip_in_memory(sorted_files_data)
                st.download_button(
                    label="📥 Download Sorted Files (ZIP)",
                    data=zip_buffer,
                    file_name="sorted_files.zip",
                    mime="application/zip",
                    key="download_sorted"
                )
                st.success("File berhasil disortir dan siap di-download sebagai ZIP!")

elif selected_feature == "📦 Compress Files":
    st.header("📦 Compress Files")
    st.write("Uplaod fiile yang anda ingin kompres menjadi satu file zip")

    uploaded_files = st.file_uploader("Pilih file..", accept_multiple_files=True, key="compress_zip_name")

    if uploaded_files:
        if st.button("Proses Kompresi", key="compress_button"):
            files_to_compress_data = []
            # st.write("memproses file..") #feeback

            for uploaded_file in uploaded_files:
                files_to_compress_data.append({"name": uploaded_file.name, "data": uploaded_file.getvalue()})
                st.write(f"Menambahkan '{uploaded_file.name}' ke arrsip.")

                if files_to_compress_data:
                    zip_buffer=create_zip_in_memory(files_to_compress_data)
                    st.download_button(
                        label=f"📥 Download {zip_file_name}",
                        data=zip_buffer,
                        file_name=zip_file_name if zip_file_name.endswith(".zip") else zip_file_name + ".zip",
                        mime="application/zip",
                        key="downlad_compressed"
                    )
                    st.success("File berhasil dikompres da siap di download!")

elif selected_feature == "📄 Extract Text from PDF":
    st.header("📄 Extract Text from PDF")
    st.write("Upload satu file PDF untuk diekstrak teksnya.")

    #untuk ekstraksi teks, hanya 1 file PDF saja
    uploaded_pdf = st.file_uploader("Pilih file PDF..", type=["pdf"], accept_multiple_files=False, key="pdf_uploader")

    if uploaded_pdf:
        if st.button("Proses Ekstraksi Teks", key="extract_button"):
            #st.write("Mengekstak teks...") #feefback

            try:
                pdf_reader = PdfReader(uploaded_pdf)
                extracted_text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    extracted_text += page.extract_text()

                if extracted_text.strip(): #cekk apakah ada teks yang diekstrak
                    st.subheader("Teks yang Dieksrak:")
                    st.text_area("Isi Teks:", extracted_text, height=300, key="extracted_text_area")

                    #tomblol download
                    st.download_button(
                        label="📥 Download Teks (.txt)",
                        data=extracted_text.encode('utf-8'),
                        file_name=f"{os.path.splitext(uploaded_pdf.name)[0]}_extracted.txt",
                        mime="text/plain",
                        key="download_text"
                    )
                    st.success("Teks berhasil diekstrak!")
                else:
                    st.warning("Tidak ada teks yang bisa di ekstrak dari PDF ini atau PDF mungkin berbasis gambar.")

            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses PDF: {e}")
                #jiks PDF terenkripsi dan PyPDF2 tidak bisa membukanya tanpa password.

#Footer
st.sidebar.markdown("---")
st.sidebar.info("Dibuat dengan ❤️ menggunakan Streamlit.")
st.sidebar.markdown("[Lihat kode di Github](https://github.com/BagaSept26/file-automation-streamlit)")