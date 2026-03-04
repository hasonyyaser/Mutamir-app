import streamlit as st

st.set_page_config(page_title="دليل المعتمر", layout="centered")

# تنسيق الأزرار كما طلبته (ألوان واضحة)
st.markdown("""
    <style>
    div.stButton > button:first-child { background-color: #15803d !important; color: white !important; height: 100px; width: 100%; font-size: 22px !important; border-radius: 15px; }
    div.stButton + div.stButton > button { background-color: #b91c1c !important; color: white !important; height: 100px; width: 100%; font-size: 22px !important; border-radius: 15px; }
    .room-box { background-color: #ffffff; padding: 20px; border-radius: 15px; border: 2px solid #1e293b; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("🕋 مساعدك في المدينة")

# عرض رقم الغرفة (يُسحب من قاعدة البيانات بناءً على رقم هاتف المعتمر لاحقاً)
st.markdown("""
    <div class='room-box'>
        <h3 style='margin:0;'>رقم غرفتك</h3>
        <h1 style='color: #1e3a8a; margin:10px;'>302</h1>
        <p style='color: green;'>✅ تم تأكيد حجز الفندق</p>
    </div>
""", unsafe_allow_html=True)

if st.button("📍 موقع الفندق (الخريطة)"):
    st.info("جاري فتح الخريطة...")

if st.button("⚠️ أنا تائه.. اطلب مساعدة"):
    st.error("تم إرسال موقعك للمندوب")
