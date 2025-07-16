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
TELEGRAM_BOT_USERNAME = "dutect_bot"
TELEGRAM_BOT_LINK = f"https://t.me/{TELEGRAM_BOT_USERNAME}"

# --- CSS Kustom Global dan Perbaikan Tampilan ---
st.markdown(
    """
    <style>
    /* Mengatasi Streamlit default padding untuk layout wide */
    .st-emotion-cache-z5fcl4 { /* Ini adalah class name untuk Streamlit main container */
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Memastikan warna teks terlihat di dark/light mode */
    h1, h2, h3, h4, h5, h6, p, li, div, code, span, a {
        color: var(--text-color); /* Menggunakan variabel warna teks default Streamlit */
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
    /* Pastikan paragraf di dalam kolom terlihat */
    [data-testid="column"] p {
        color: var(--text-color);
    }
    .st-emotion-cache-1iy5a4c { /* Ini adalah class name untuk subheader (contoh "Pencatatan Cepat") */
        margin-bottom: 0.5rem;
    }
    /* Mengatur style st.code blocks */
    .stCodeBlock { /* Ini adalah class name untuk st.code block */
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
        background-color: var(--secondary-background-color);
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px; /* Jarak antar step card */
        color: var(--text-color); /* Memastikan teks di card terlihat */
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
        color: var(--text-color);
        vertical-align: middle;
    }
    /* Memperbaiki warna teks untuk link di bagian cara menggunakan */
    .step-card a {
        color: #3498db !important; /* Warna biru untuk link username bot */
    }
    /* Memastikan teks paragraf di dalam step-card terlihat */
    .step-card p {
        color: var(--text-color) !important;
        margin-top: 10px; /* Jarak antara judul langkah dan paragraf */
    }

    /* Styles untuk FAQ */
    .st-emotion-cache-1ecpmsa p { /* Class untuk paragraf di dalam expander */
        color: var(--text-color) !important;
    }

    /* Footer */
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
    st.code("beli kopi 25000", language="python") # Menambahkan language="python"

with col2:
    st.subheader("Scan Struk Otomatis")
    st.write("Cukup foto struk belanja Anda, kirim ke bot, dan biarkan kami yang mencatatnya!")
    # REVISI PENTING: Ganti placeholder ini dengan path relatif ke gambar Anda
    # yang sudah DIEDIT (dipotong & diresize agar tidak terlalu besar) dan diupload ke GitHub.
    st.image("https://via.placeholder.com/400x250?text=Gambar+Contoh+Struk+Anda", caption="Contoh Unggah Struk (Ganti Gambar Ini!)", use_container_width=True)
    st.markdown("Kirim gambar ini dengan *caption*: `catat struk`")


with col3:
    st.subheader("Laporan Instan")
    st.write("Dapatkan ringkasan pengeluaran harian, mingguan, bulanan, atau per kategori kapan saja.")
    st.code("laporan bulanan", language="python") # Menambahkan language="python"
    st.code("kategori hari", language="python") # Menambahkan language="python"


# --- Bagian Cara Menggunakan ---
st.header("💡 Bagaimana Cara Menggunakan?")

# Definisikan fungsi helper untuk membuat step-card
# Ini akan membuat kode lebih rapi dan bisa digunakan berulang
def create_step_card(step_number, title, content_func):
    st.markdown(f"""
    <div class="step-card">
        <span class="step-number-circle">{step_number}</span> <span class="step-title">{title}</span>
    </div>
    """, unsafe_allow_html=True)
    # Gunakan st.container() untuk menampung konten yang akan dirender oleh content_func
    # Ini penting agar st.write/st.code di dalam content_func tidak 'meluber' keluar div
    with st.container():
        content_func()


# Langkah 1: Temukan Bot Kami
create_step_card(
    1, "Temukan Bot Kami",
    lambda: st.write(f"Buka aplikasi Telegram Anda dan cari <a href=\"{TELEGRAM_BOT_LINK}\" target=\"_blank\">@{TELEGRAM_BOT_USERNAME}</a> di kolom pencarian.", unsafe_allow_html=True)
)

# Langkah 2: Mulai Percakapan
create_step_card(
    2, "Mulai Percakapan",
    lambda: (
        st.write("Ketik <code>hi</code> atau <code>halo</code> untuk memulai interaksi pertama Anda dengan bot.", unsafe_allow_html=True),
        # Jika Anda ingin mereka sebagai blok kode terpisah seperti di gambar yang Anda berikan
        st.code("hi", language="text"),
        st.code("halo", language="text")
    )
)

# Langkah 3: Catat Pengeluaran
create_step_card(
    3, "Catat Pengeluaran",
    lambda: (
        st.write("Ketikkan pengeluaran Anda seperti contoh:", unsafe_allow_html=True),
        st.code("beli makan siang 30000", language="python"),
        st.write("Atau kirimkan foto struk belanja Anda dengan <i>caption</i> <b>\"catat struk\"</b>.", unsafe_allow_html=True)
    )
)

# Langkah 4: Dapatkan Laporan
create_step_card(
    4, "Dapatkan Laporan",
    lambda: (
        st.write("Tanyakan laporan keuangan yang Anda inginkan, contoh:", unsafe_allow_html=True),
        st.code("laporan harian", language="python"),
        st.code("laporan listrik", language="python")
    )
)


# --- Bagian FAQ ---
st.header("❓ Pertanyaan Umum (FAQ)")

with st.expander("Apakah data keuangan saya aman?"):
    st.write("Ya, data keuangan Anda disimpan dengan aman di database dan tidak dibagikan kepada pihak ketiga. Kami memprioritaskan keamanan dan privasi data Anda.")

with st.expander("Bisakah saya menghapus data pengeluaran saya?"):
    st.write("Tentu, Anda bisa mengetik perintah `hapus pengeluaran` di chatbot untuk menghapus semua data transaksi yang telah Anda catat.")

with st.expander("Apa yang harus saya lakukan jika bot tidak merespons?"):
    st.write(f"Pastikan Anda memiliki koneksi internet yang stabil. Jika bot tetap tidak merespons, coba ketik `reset` atau `bantuan` untuk melihat perintah yang tersedia. Jika masalah berlanjut, silakan hubungi kami di jeanetugas@gmail.com.")


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
