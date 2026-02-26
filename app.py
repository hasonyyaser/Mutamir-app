import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="منصة إرشاد المعتمر", layout="wide")

# القائمة الجانبية
page = st.sidebar.selectbox("اختر الواجهة", ["لوحة تحكم الشركة", "واجهة المعتمر (تجربة)"])

if page == "لوحة تحكم الشركة":
    st.title("🕋 إدارة الأفواج - المدينة المنورة")
    col1, col2 = st.columns(2)
    col1.metric("الأفواج النشطة", "3")
    col2.metric("حالات التيهان", "0")
    
    st.subheader("📊 المتابعة الميدانية")
    # هنا سنربط Google Sheets لاحقاً
    data = {"الاسم": ["أحمد جاسم", "سعاد علي"], "الحالة": ["في الفندق", "في الحرم"]}
    st.table(pd.DataFrame(data))

else:
    # --- واجهة المعتمر بتنسيق ألوان جديد وواضح ---
    st.markdown("<h1 style='text-align: center;'>🕋 دليل الزائر العراقي</h1>", unsafe_allow_html=True)
    
    # تنسيق الأزرار (ألوان واضحة ونصوص بارزة)
    st.markdown("""
        <style>
        /* زر الفندق - أخضر غامق وكتابة بيضاء */
        div.stButton > button:first-child {
            background-color: #059669 !important;
            color: white !important;
            height: 120px;
            width: 100%;
            font-size: 28px !important;
            font-weight: bold;
            border-radius: 15px;
            border: 2px solid #065f46;
            margin-bottom: 20px;
        }
        /* زر الطوارئ - أحمر فاقع وكتابة بيضاء */
        div.stButton + div.stButton > button {
            background-color: #dc2626 !important;
            color: white !important;
            height: 120px;
            width: 100%;
            font-size: 28px !important;
            font-weight: bold;
            border-radius: 15px;
            border: 2px solid #991b1b;
        }
        /* تحسين مظهر الصفحة */
        .stApp {
            background-color: #f8fafc;
        }
        </style>
    """, unsafe_allow_html=True)

    st.write("---")
    
    # الزر الأول (سيظهر باللون الأخضر)
    if st.button("📍 اندلني فندقي (الخريطة)"):
        st.info("جاري فتح الخريطة...")
        
    # الزر الثاني (سيظهر باللون الأحمر)
    if st.button("⚠️ أنا تائه.. اطلب مساعدة"):
        st.error("تم إرسال موقعك.. ابقَ في مكانك")

    st.write("---")
    with st.expander("📞 أرقام الطوارئ"):
        st.write("المندوب: 05xxxxxxx")
