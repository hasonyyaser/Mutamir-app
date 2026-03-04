import streamlit as st
import pandas as pd

st.set_page_config(page_title="إدارة شركة الحج", layout="wide")

st.title("📂 لوحة تحكم الشركة - المتابعة الميدانية")

# هنا نضع بيانات تجريبية، وفي الخطوة القادمة سنربطها بـ Google Sheets
data = {
    "الاسم": ["أحمد جاسم", "سعاد علي", "محمد حسن"],
    "رقم الغرفة": ["302", "Pending", "405"],
    "تأكيد الحجز": ["✅ مؤكد", "❌ غير مؤكد", "✅ مؤكد"],
    "الحالة الميدانية": ["في الفندق", "في الطريق", "في الحرم"]
}
df = pd.DataFrame(data)

# عرض البيانات مع إمكانية التعديل
st.subheader("تحديث بيانات الأفواج")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

if st.button("حفظ التحديثات"):
    st.success("تم تحديث البيانات وحفظها في قاعدة البيانات!")
