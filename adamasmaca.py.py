
import streamlit as st
import random

# Sayfa ayarları
st.set_page_config(page_title="🩸 Adam Asmaca Mobil", page_icon="q" \
"💦", layout="centered")

# Sabit Oyun Verileri
KELIMELER = ["python", "yazilim", "bilgisayar", "kodlama", "klavye", "ekran", "terminal", "piyango", "şöhret", "domestos", "skeç", "disko", "spontane"]

GORSELLER = [
    """```\n   --------\n   |      |\n   |      O\n   |     /|\\\n   |     / \\\n   |\n```""",
    """```\n   --------\n   |      |\n   |      O\n   |     /|\\\n   |     /\n   |\n```""",
    """```\n   --------\n   |      |\n   |      O\n   |     /|\\\n   |\n   |\n```""",
    """```\n   --------\n   |      |\n   |      O\n   |     /|\n   |\n   |\n```""",
    """```\n   --------\n   |      |\n   |      O\n   |      |\n   |\n   |\n```""",
    """```\n   --------\n   |      |\n   |      O\n   |\n   |\n   |\n```""",
    """```\n   --------\n   |      |\n   |\n   |\n   |\n   |\n```"""
]

DALGA_GECMELER = [
    "🤖: O harf kelimede yok! Alfabeyi baştan mı öğrensen? 🤭",
    "🤖: Yanlış tahmin! İp geriliyor, haberin olsun... 🕸️",
    "🤖: Kelimeyi rüyanda görsen daha iyi tahmin ederdin! Hatalı harf! 🛌",
    "🤖: Sallama yeteneğin sıfırmış dostum, o harf yok! 📉"
    "🤖: Eşşek misin Eyüp ,saçmalıyorsun"
]

# Hafızayı Başlatma
if "secilen_kelime" not in st.session_state:
    st.session_state.secilen_kelime = random.choice(KELIMELER)
    st.session_state.bilinen_durum = ["_"] * len(st.session_state.secilen_kelime)
    st.session_state.yanlis_harfler = []
    st.session_state.kalan_can = 6
    st.session_state.mesaj = "🤖 Bilgisayar: 'Yine mi sen EYÜP? Bakalım bu sefer kimi ipten alacaksın!'"
    st.session_state.mesaj_turu = "info"

def oyunu_sifirla():
    st.session_state.secilen_kelime = random.choice(KELIMELER)
    st.session_state.bilinen_durum = ["_"] * len(st.session_state.secilen_kelime)
    st.session_state.yanlis_harfler = []
    st.session_state.kalan_can = 6
    st.session_state.mesaj = "🤖 Bilgisayar: 'Yine mi sen EYÜP? Bakalım bu sefer kimi ipten alacaksın!'"
    st.session_state.mesaj_turu = "info"

# ---- Arayüz Tasarımı ----
st.title("👽 ADAM ASMACA MOBİL 👽")

if st.session_state.mesaj_turu == "info":
    st.info(st.session_state.mesaj)
elif st.session_state.mesaj_turu == "success":
    st.success(st.session_state.mesaj)
elif st.session_state.mesaj_turu == "error":
    st.error(st.session_state.mesaj)

st.subheader(f"❤️ Kalan Canın: {st.session_state.kalan_can}")
st.markdown(GORSELLER[st.session_state.kalan_can])

kelime_gosterimi = " ".join(st.session_state.bilinen_durum).upper()
st.subheader(f"Kelime: {kelime_gosterimi}")

if st.session_state.yanlis_harfler:
    st.write(f"❌ Yanlış Harfler: {', '.join(st.session_state.yanlis_harfler).upper()}")

if st.session_state.kalan_can > 0 and "_" in st.session_state.bilinen_durum:
    tahmin = st.text_input("Bir harf tahmin edin:", max_chars=1).lower()
    
    if st.button("Tahmin Et 🚀"):
        if len(tahmin) != 1 or not tahmin.isalpha():
            st.session_state.mesaj = "🚨 Lütfen sadece TEK BİR HARF girin!"
            st.session_state.mesaj_turu = "info"
            st.rerun()
        elif tahmin in st.session_state.bilinen_durum or tahmin in st.session_state.yanlis_harfler:
            st.session_state.mesaj = "🤔 Bu harfi zaten denemiştin!"
            st.session_state.mesaj_turu = "info"
            st.rerun()
        elif tahmin in st.session_state.secilen_kelime:
            st.session_state.mesaj = "✨ Aferin! Doğru harf. Bilgisayar şokta! 😲"
            st.session_state.mesaj_turu = "success"
            for i in range(len(st.session_state.secilen_kelime)):
                if st.session_state.secilen_kelime[i] == tahmin:
                    st.session_state.bilinen_durum[i] = tahmin
            st.rerun()
        else:
            st.session_state.mesaj = random.choice(DALGA_GECMELER)
            st.session_state.mesaj_turu = "error"
            st.session_state.yanlis_harfler.append(tahmin)
            st.session_state.kalan_can -= 1
            st.rerun()

if "_" not in st.session_state.bilinen_durum:
    st.balloons()
    st.success(f"🥳 TEBRİKLER EYÜP! Kelime: {st.session_state.secilen_kelime.upper()}")
    if st.button("Yeniden Başlat 🔄"):
        oyunu_sifirla()
        st.rerun()
elif st.session_state.kalan_can <= 0:
    st.error(f"💀 OYUN BİTTİ! Kelime: {st.session_state.secilen_kelime.upper()}")
    if st.button("Tekrar Dene 🔄"):
        oyunu_sifirla()
        st.rerun()   