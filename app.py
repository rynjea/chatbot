import streamlit as st
import os

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Chatbot Pengelola Keuangan Pribadi",
    page_icon="💰",
    layout="wide",  # Layout lebar untuk mengisi browser
    initial_sidebar_state="collapsed"
)

# --- Informasi Bot Anda ---
TELEGRAM_BOT_USERNAME = "duitect_bot" # Menggunakan username dari gambar Anda
TELEGRAM_BOT_LINK = f"https://t.me/duitect_bot"

# --- CSS Kustom Global dan Perbaikan Tampilan ---
st.markdown(
    """
    <style>
    /* Mengatasi Streamlit default padding untuk layout wide */
    .st-emotion-cache-z5fcl4 { /* Ini adalah class name untuk Streamlit main container */
        padding-left: 2rem; /* Jarak kiri dari pinggir browser */
        padding-right: 2rem; /* Jarak kanan dari pinggir browser */
    }

    /* Memastikan warna teks terlihat di dark/light mode */
    h1, h2, h3, h4, h5, h6, p, li, div, code, span {
        color: var(--text-color); /* Menggunakan variabel warna teks default Streamlit */
    }

    /* Styles untuk bagian Header */
    .header-section {
        background-color: #3498db; /* Biru cerah */
        color: white; /* Teks putih */
        padding: 50px 0;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .header-section h1 {
        color: white; /* Judul header selalu putih */
        font-size: 2.8em;
        margin-bottom: 10px;
    }
    .header-section p {
        font-size: 1.2em;
        margin-bottom: 30px;
        color: white; /* Paragraf header selalu putih */
    }
    .btn-telegram {
        display: inline-block;
        background-color: #2ecc71; /* Hijau cerah */
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
        color: white; /* Pastikan teks ini juga putih */
    }

    /* Styles untuk bagian Fitur Utama (st.columns sudah cukup baik, ini untuk styling internal) */
    .st-emotion-cache-1iy5a4c { /* Class name untuk subheader di Streamlit */
        color: #3498db; /* Warna subheader di bagian fitur (biru cerah) */
    }
    .st-emotion-cache-h4y6x0 p { /* Class untuk paragraf di dalam kolom st.columns */
        color: var(--text-color); /* Pastikan warnanya sesuai tema Streamlit */
    }
    .st-emotion-cache-1iy5a4c { /* Ini adalah class name untuk subheader (contoh "Pencatatan Cepat") */
        margin-bottom: 0.5rem; /* Sedikit mengurangi margin bawah subheader */
    }
    .st-emotion-cache-1nj07o3 pre { /* class name untuk st.code block */
        font-size: 0.9em;
        white-space: pre-wrap; /* Memastikan kode wrapping jika panjang */
        word-wrap: break-word; /* Memastikan kata wrapping jika panjang */
        padding: 10px;
        border-radius: 5px;
        background-color: var(--secondary-background-color); /* Sesuaikan dengan tema Streamlit */
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }

    /* Styles untuk bagian Cara Menggunakan */
    .step-card {
        background-color: var(--secondary-background-color); /* Menggunakan warna background sekunder Streamlit */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: var(--text-color); /* Memastikan teks di card terlihat */
    }
    .step-number-circle {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #3498db; /* Warna biru untuk lingkaran nomor */
        color: white;
        font-weight: bold;
        font-size: 1.2em;
        margin-right: 15px;
    }
    .step-title {
        display: inline-block;
        font-size: 1.3em;
        color: var(--text-color); /* Warna judul langkah */
        vertical-align: middle;
    }
    /* Memperbaiki warna teks untuk username bot di bagian cara menggunakan */
    .step-card a {
        color: #3498db !important; /* Warna biru untuk link username bot */
    }
    .step-card p {
        color: var(--text-color) !important; /* Memastikan teks paragraf terlihat */
    }

    /* Styles untuk FAQ */
    .st-emotion-cache-1ecpmsa p { /* Class untuk paragraf di dalam expander */
        color: var(--text-color) !important; /* Memastikan teks FAQ terlihat */
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
        color: #2ecc71; /* Link di footer hijau */
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
    st.code("beli kopi 25000", language="python") # Menambahkan bahasa untuk syntax highlighting

with col2:
    st.subheader("Scan Struk Otomatis")
    st.write("Cukup foto struk belanja Anda, kirim ke bot, dan biarkan kami yang mencatatnya!")
    # MENGATASI DEPRECATION WARNING: Menggunakan use_container_width=True
    # Ganti "https://via.placeholder.com/300x200?text=Gambar+Contoh+Struk"
    # dengan path relatif gambar Anda jika sudah diupload ke GitHub/Replit.
    st.image("6303195331487189232.jpg", caption="Contoh Unggah Struk", use_container_width=True)
    st.markdown("Kirim gambar ini dengan *caption*: `catat struk`")


with col3:
    st.subheader("Laporan Instan")
    st.write("Dapatkan ringkasan pengeluaran harian, mingguan, bulanan, atau per kategori kapan saja.")
    st.code("laporan bulanan", language="python")
    st.code("laporan belanja", language="python")


# --- Bagian Cara Menggunakan ---
st.header("💡 Bagaimana Cara Menggunakan?")

# Menggunakan st.markdown untuk custom HTML tetap dipertahankan untuk styling card
# MEMPERBAIKI WARNA TEKS UNTUK USERNAME BOT DI SINI dengan style inline
st.markdown(f"""
<div class="step-card">
    <span class="step-number-circle">1</span> <span class="step-title">Temukan Bot Kami</span>
    <p>Buka aplikasi Telegram Anda dan cari *<a href="{TELEGRAM_BOT_LINK}" target="_blank">@{TELEGRAM_BOT_USERNAME}</a>* di kolom pencarian.</p>
</div>
<div class="step-card">
    <span class="step-number-circle">2</span> <span class="step-title">Mulai Percakapan</span>
    <p>Klik tombol "Start" atau ketik <code>/start</code> atau <code>halo</code> untuk memulai interaksi pertama Anda dengan bot.</p>
</div>
<div class="step-card">
    <span class="step-number-circle">3</span> <span class="step-title">Catat Pengeluaran</span>
    <p>Ketikkan pengeluaran Anda seperti contoh: <code>beli makan siang 30000</code> Atau kirimkan foto struk belanja Anda dengan <i>caption</i> <b>"catat struk"</b></p>
</div>
<div class="step-card">
    <span class="step-number-circle">4</span> <span class="step-title">Dapatkan Laporan</span>
    <p>Tanyakan laporan keuangan yang Anda inginkan, contoh: <code>laporan harian</code> atau <code>laporan bayar listrik</code></p>
</div>
""", unsafe_allow_html=True)


# --- Bagian FAQ ---
st.header("❓ Pertanyaan Umum (FAQ)")

with st.expander("Apakah data keuangan saya aman?"):
    st.write("Ya, data keuangan Anda disimpan dengan aman di Neon Database dan tidak dibagikan kepada pihak ketiga. Kami memprioritaskan keamanan dan privasi data Anda.")

with st.expander("Bisakah saya menghapus data pengeluaran saya?"):
    st.write("Tentu, Anda bisa mengetik perintah `hapus pengeluaran` di chatbot untuk menghapus semua data transaksi yang telah Anda catat.")

with st.expander("Apa yang harus saya lakukan jika bot tidak merespons?"):
    st.write(f"Pastikan Anda memiliki koneksi internet yang stabil. Jika bot tetap tidak merespons, coba ketik `reset` atau `bantuan` untuk melihat perintah yang tersedia. Jika masalah berlanjut, silakan hubungi kami di [Email Anda].")


# --- Bagian Footer ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 20px; font-size: 0.9em; color: #555;">
        <p>&copy; 2025 Chatbot Pengelola Keuangan Pribadi. Hak cipta dilindungi undang-undang.</p>
        <p>Hubungi kami: [Email Anda] | <a href="link-ke-kebijakan-privasi-anda.html" target="_blank" style="color: #3498db;">Kebijakan Privasi</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
