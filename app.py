import streamlit as st
import os

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Chatbot Pengelola Keuangan Pribadi",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Informasi Bot Anda ---
TELEGRAM_BOT_USERNAME = "duitect_bot"
TELEGRAM_BOT_LINK = f"https://t.me/duitect_bot"

# --- CSS Kustom Global dan Perbaikan Tampilan ---
st.markdown(
    """
    <style>
    /* Mengatasi Streamlit default padding untuk layout wide */
    .st-emotion-cache-z5fcl4 { /* Ini adalah class name untuk Streamlit main container */
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Memastikan warna teks terlihat di dark/light mode untuk elemen standar */
    /* Aturan umum, akan di-override oleh aturan yang lebih spesifik jika ada */
    body, p, li, div, span, a {
        color: var(--text-color);
    }
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-color);
    }

    /* Styles untuk bagian Header */
    .header-section {
        background-color: #3498db;
        color: white;
        padding: 50px 0;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .header-section h1 {
        color: white;
        font-size: 2.8em;
        margin-bottom: 10px;
    }
    .header-section p {
        font-size: 1.2em;
        margin-bottom: 30px;
        color: white;
    }
    .btn-telegram {
        display: inline-block;
        background-color: #2ecc71;
        color: white;
        padding: 15px 30px;
        border-radius: 8px;
        text-transform: uppercase;
        font-weight: bold;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
        text-decoration: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .btn-telegram:hover {
        background-color: #27ae60;
        color: white;
        text-decoration: none;
    }
    .bot-username-text {
        margin-top: 15px;
        font-size: 0.9em;
        opacity: 0.8;
        color: white;
    }

    /* Styles untuk judul st.header "Fitur Utama Chatbot Kami" */
    div[data-testid="stHeader"] + div[data-testid="stVerticalBlock"] div[data-testid="stMarkdownContainer"] h2 {
        margin-bottom: 2rem;
    }

    /* Styles untuk bagian Fitur Utama (st.columns sudah cukup baik, ini untuk styling internal) */
    .st-emotion-cache-1iy5a4c { /* Class name untuk subheader di Streamlit */
        color: #3498db;
    }
    [data-testid="column"] p {
        color: var(--text-color);
    }
    .st-emotion-cache-1iy5a4c {
        margin-bottom: 0.5rem;
    }
    /* Mengatur style st.code blocks di luar step-card (misal: di Fitur Utama) */
    .stCodeBlock {
        font-size: 0.9em;
        white-space: pre-wrap;
        word-wrap: break-word;
        padding: 10px;
        border-radius: 5px;
        background-color: var(--secondary-background-color);
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }


    /* Styles untuk bagian Cara Menggunakan */
    .step-card {
        background-color: #f0f2f6; /* Latar belakang card putih-abu (seperti gambar) */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .step-number-circle {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #3498db;
        color: white;
        font-weight: bold;
        font-size: 1.2em;
        margin-right: 15px;
    }
    .step-title {
        display: inline-block;
        font-size: 1.3em;
        color: #2c3e50; /* KUNCI PERBAIKAN: Warna gelap eksplisit agar terlihat di background putih-abu */
        vertical-align: middle;
    }

    /* KUNCI PERBAIKAN UNTUK KOTAK HITAM DAN TULISAN PUTIH PADA LANGKAH-LANGKAH */
    .step-card code { /* Menargetkan elemen <code> di dalam step-card */
        display: block; /* Agar setiap contoh pada baris terpisah */
        margin-top: 10px; /* Jarak dari judul langkah atau code sebelumnya */
        margin-bottom: 5px; /* Jarak bawah antar kotak kode (jika ada lebih dari satu) */
        padding: 15px 20px; /* Padding di dalam kotak */
        border-radius: 4px;
        background-color: #000000 !important; /* Latar belakang HITAM */
        color: white !important; /* Teks PUTIH */
        border: 1px solid #1a1a1a !important; /* Border abu-abu sangat gelap (mendekati hitam) */
        font-family: monospace;
        font-size: 1em;
        white-space: pre-wrap; /* Memastikan teks wrap jika panjang */
        word-wrap: break-word; /* Memastikan kata wrap jika panjang */
        text-align: left; /* Teks rata kiri */
    }
    /* Mengatasi potensi masalah margin-bottom pada p tag bawaan jika ada */
    .step-card p {
        margin-bottom: 0 !important; /* Hilangkan margin bawah default p */
    }
    /* Jika ada banyak code di satu step, ini akan mengatur jaraknya */
    .step-card code + code {
        margin-top: 10px !important;
    }

    /* Memastikan link di dalam code tetap putih */
    .step-card code a {
        color: white !important;
        text-decoration: underline;
    }

    /* FAQ Styles */
    .st-emotion-cache-1ecpmsa p {
        color: var(--text-color) !important;
    }

    /* Footer Styles */
    footer {
        background: var(--secondary-background-color);
        color: var(--text-color);
        text-align: center;
        padding: 30px 0;
        font-size: 0.9em;
    }
    footer p {
        margin: 5px 0;
        color: var(--text-color);
    }
    footer a {
        color: #2ecc71;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Bagian Header ---
st.markdown(f"""
<div class="header-section">
    <h1>💰 Asisten Keuangan Pribadi Anda di Telegram!</h1>
    <p>Kelola pengeluaran Anda dengan mudah, cukup lewat chat.</p>
    <a href="{TELEGRAM_BOT_LINK}" target="_blank" class="btn-telegram">Mulai Sekarang di Telegram!</a>
    <p class="bot-username-text">Cari juga kami: @{TELEGRAM_BOT_USERNAME}</p>
</div>
""", unsafe_allow_html=True)


# --- Bagian Fitur Utama ---
st.header("✨ Fitur Utama Chatbot Kami")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Pencatatan Cepat")
    st.write("Catat pengeluaran harian Anda hanya dengan mengirim pesan teks sederhana.")
    st.code("beli kopi 25000", language="python")

with col2:
    st.subheader("Scan Struk Otomatis")
    st.write("Cukup foto struk belanja Anda, kirim ke bot, dan biarkan kami yang mencatatnya!")
    # REVISI PENTING: Ganti placeholder ini dengan path relatif ke gambar Anda
    # yang sudah DIEDIT (dipotong & diresize agar tidak terlalu besar) dan diupload ke GitHub.
    # Contoh: st.image("nama_file_gambar_struk_anda.png", caption="Contoh Unggah Struk", use_container_width=True)
    st.image("6303195331487189232.jpg", caption="Contoh Unggah Struk", use_container_width=True)
    st.markdown("Kirim gambar ini dengan *caption*: `catat struk`")


with col3:
    st.subheader("Laporan Instan")
    st.write("Dapatkan ringkasan pengeluaran harian, mingguan, bulanan, atau per kategori kapan saja.")
    st.code("laporan bulanan", language="python")
    st.code("laporan belanja", language="python")


# --- Bagian Cara Menggunakan ---
st.header("💡 Bagaimana Cara Menggunakan?")

# Langkah 1
st.markdown(f"""
<div class="step-card">
    <span class="step-number-circle">1</span> <span class="step-title">Temukan Bot Kami</span>
    <code style="display: block; margin-top: 15px; margin-bottom: 5px;">Buka aplikasi Telegram Anda dan cari <a href="{TELEGRAM_BOT_LINK}" target="_blank">@{TELEGRAM_BOT_USERNAME}</a> di kolom pencarian.</code>
</div>
""", unsafe_allow_html=True)

# Langkah 2
st.markdown("""
<div class="step-card">
    <span class="step-number-circle">2</span> <span class="step-title">Mulai Percakapan</span>
    <code style="display: block; margin-top: 15px; margin-bottom: 5px;">hi</code>
    <code style="display: block; margin-top: 10px; margin-bottom: 5px;">halo</code>
</div>
""", unsafe_allow_html=True)

# Langkah 3
st.markdown("""
<div class="step-card">
    <span class="step-number-circle">3</span> <span class="step-title">Petunjuk Penggunaan</span>
    <code style="display: block; margin-top: 15px; margin-bottom: 5px;">bantuan</code>
</div>
""", unsafe_allow_html=True)

# Langkah 4
st.markdown("""
<div class="step-card">
    <span class="step-number-circle">4</span> <span class="step-title">Catat Pengeluaran</span>
    <code style="display: block; margin-top: 15px; margin-bottom: 5px;">beli makan siang</code>
    <code style="display: block; margin-top: 10px; margin-bottom: 5px;">kirimkan foto struk belanja dengan <i>caption</i> <b>"catat struk"</code>
</div>
""", unsafe_allow_html=True)

# Langkah 5
st.markdown("""
<div class="step-card">
    <span class="step-number-circle">5</span> <span class="step-title">Dapatkan Laporan</span>
    <code style="display: block; margin-top: 15px; margin-bottom: 5px;">laporan harian</code>
    <code style="display: block; margin-top: 10px; margin-bottom: 5px;">laporan listrik</code>
</div>
""", unsafe_allow_html=True)


# --- Bagian FAQ ---
st.header("❓ Pertanyaan Umum (FAQ)")

with st.expander("Apakah data keuangan saya aman?"):
    st.write("Ya, data keuangan Anda disimpan dengan aman di database dan tidak dibagikan kepada pihak ketiga. Kami memprioritaskan keamanan dan privasi data Anda.")

with st.expander("Bisakah saya menghapus data pengeluaran saya?"):
    st.write("Tentu, Anda bisa mengetik perintah `hapus pengeluaran` di chatbot untuk menghapus semua data transaksi yang telah Anda catat.")

with st.expander("Apa yang harus saya lakukan jika bot tidak merespons?"):
    st.write(f"Pastikan Anda memiliki koneksi internet yang stabil. Jika bot tetap tidak merespons, coba ketik 'bantuan' untuk melihat perintah yang tersedia. Jika masalah berlanjut, silakan hubungi kami di jeanetugas@gmail.com.")


# --- Bagian Footer ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 20px; font-size: 0.9em; color: #555;">
        <p>&copy; 2025 Chatbot Pengelola Keuangan Pribadi. Hak cipta dilindungi undang-undang.</p>
        <p>Hubungi kami: jeanetugas@gmail.com | <a href="link-ke-kebijakan-privasi-anda.html" target="_blank" style="color: #3498db;">Kebijakan Privasi</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
