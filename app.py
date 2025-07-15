import streamlit as st
import os

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Chatbot Pengelola Keuangan Pribadi",
    page_icon="💰",
    layout="wide", 
    initial_sidebar_state="collapsed" # Opsional, jika tidak ada sidebar
)

# --- Informasi Bot Anda ---
# Ganti dengan username bot Telegram Anda yang sebenarnya
TELEGRAM_BOT_USERNAME = "duitect_bot" 
TELEGRAM_BOT_LINK = f"https://t.me/duitect_bot"

# --- Bagian Header ---
st.markdown(
    """
    <style>
    .header-section {
        background-color: #3498db; /* Biru cerah */
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
        text-decoration: none; /* Pastikan tidak ada underline */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .btn-telegram:hover {
        background-color: #27ae60; /* Hijau lebih gelap saat hover */
        color: white; /* Pastikan teks tetap putih saat hover */
        text-decoration: none;
    }
    .bot-username-text {
        margin-top: 15px;
        font-size: 0.9em;
        opacity: 0.8;
    }
    
    div[data-testid="stHeader"] + div[data-testid="stVerticalBlock"] div[data-testid="stMarkdownContainer"] h2 {
        margin-bottom: 2rem; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    st.code("beli kopi 25000")

with col2:
    st.subheader("Scan Struk Otomatis")
    st.write("Cukup foto struk belanja Anda, kirim ke bot, dan biarkan kami yang mencatatnya!")
    # Placeholder untuk gambar struk. Anda perlu menyimpan gambar ini di folder yang sama
    # dengan app.py di GitHub/Replit, lalu ganti 'path/to/gambar_contoh_struk_upload.png'
    # dengan nama file gambar Anda.
    # Contoh: st.image("contoh_struk_upload.png", caption="Contoh Unggah Struk", use_column_width=True)
    st.image("6303195331487189232.jpg", caption="Contoh Unggah Struk", use_container_width=True)
    st.markdown("Kirim gambar ini dengan *caption*: `catat struk`")


with col3:
    st.subheader("Laporan Instan")
    st.write("Dapatkan ringkasan pengeluaran harian, mingguan, bulanan, atau per kategori kapan saja.")
    st.code("laporan bulanan")
    st.code("laporan belanja")


# --- Bagian Cara Menggunakan ---
st.header("💡 Bagaimana Cara Menggunakan?")

st.markdown("""
<style>
.step-card {
    background-color: #f9f9f9;
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
    color: #2c3e50;
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-card">
    <span class="step-number-circle">1</span> <span class="step-title">Temukan Bot Kami</span>
    <p>Untuk mengakses bot: <code>Buka aplikasi Telegram Anda dan cari @duitect_bot di kolom pencarian.</code></p>
</div>
<div class="step-card">
    <span class="step-number-circle">2</span> <span class="step-title">Mulai Percakapan</span>
    <p>Ketik <code>hi</code> atau <code>halo</code> untuk memulai interaksi pertama Anda dengan bot.</p>
</div>
<div class="step-card">
    <span class="step-number-circle">3</span> <span class="step-title">Catat Pengeluaran</span>
    <p>Ketikkan pengeluaran Anda seperti contoh: <code>beli makan siang 30000</code> Atau kirimkan foto struk belanja Anda dengan <i>caption</i> <b>"catat struk"</b></p>
</div>
<div class="step-card">
    <span class="step-number-circle">4</span> <span class="step-title">Dapatkan Laporan</span>
    <p>Tanyakan laporan keuangan yang Anda inginkan, contoh: <code>laporan harian</code> atau <code>laporan listrik</code></p>
</div>
""", unsafe_allow_html=True)


# --- Bagian FAQ ---
st.header("❓ Pertanyaan Umum (FAQ)")

with st.expander("Apakah data keuangan saya aman?"):
    st.write("Ya, data keuangan Anda disimpan dengan aman di database dan tidak dibagikan kepada pihak ketiga. Kami memprioritaskan keamanan dan privasi data Anda.")

with st.expander("Bisakah saya menghapus data pengeluaran saya?"):
    st.write("Tentu, Anda bisa mengetik perintah `hapus pengeluaran` di chatbot untuk menghapus semua data transaksi yang telah Anda catat.")

with st.expander("Apa yang harus saya lakukan jika bot tidak merespons?"):
    st.write(f"Pastikan Anda memiliki koneksi internet yang stabil. Jika bot tetap tidak merespons, coba ketik `reset` atau `bantuan` untuk melihat perintah yang tersedia. Jika masalah berlanjut, silakan hubungi kami di jeanetugas@gmail.com.")


# --- Bagian Footer ---
st.markdown("---") # Garis pembatas
st.markdown(
    """
    <div style="text-align: center; padding: 20px; font-size: 0.9em; color: #555;">
        <p>&copy; 2025 Chatbot Pengelola Keuangan Pribadi. Hak cipta dilindungi undang-undang.</p>
        <p>Hubungi kami: [Email Anda] | <a href="link-ke-kebijakan-privasi-anda.html" target="_blank" style="color: #3498db;">Kebijakan Privasi</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
