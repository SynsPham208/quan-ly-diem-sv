import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu 10 sinh viên
data = {
    "Họ và tên": ["An", "Bình", "Chi", "Dũng", "Hà", "Lan", "Minh", "Nam", "Phúc", "Trang"],
    "Chuyên cần": [8.0, 9.0, 7.0, 10.0, 8.0, 6.0, 9.0, 8.0, 7.0, 10.0],
    "Giữa kỳ": [7.5, 8.5, 6.0, 9.0, 7.0, 5.5, 8.0, 6.5, 7.5, 9.5],
    "Cuối kỳ": [8.0, 8.0, 7.0, 8.5, 6.5, 6.0, 9.0, 7.0, 8.0, 9.0]
}
df = pd.DataFrame(data)
df['Tong_ket'] = 0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']

def xep_loai(diem):
    if diem >= 8.5: return "Giỏi"
    elif diem >= 7.0: return "Khá"
    elif diem >= 5.0: return "Trung bình"
    else: return "Yếu"
df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Giao diện Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.write("Bảng điểm 10 sinh viên:")
st.dataframe(df)

st.write(f"Điểm trung bình của lớp: {df['Tong_ket'].mean():.2f}")
st.write(f"Sinh viên cao nhất: {df.loc[df['Tong_ket'].idxmax()]['Họ và tên']}")
st.write(f"Sinh viên thấp nhất: {df.loc[df['Tong_ket'].idxmin()]['Họ và tên']}")
st.write(f"Số sinh viên đạt: {(df['Tong_ket'] >= 5).sum()}")

sv = st.selectbox("Chọn một sinh viên", df['Họ và tên'])
if sv:
    st.write(df[df['Họ và tên'] == sv].iloc[0][['Chuyên cần', 'Giữa kỳ', 'Cuối kỳ', 'Tong_ket', 'Xep_loai']])

fig, ax = plt.subplots()
ax.bar(df['Họ và tên'], df['Tong_ket'])
ax.set_title('Điểm tổng kết của 10 sinh viên')
st.pyplot(fig)

st.markdown("<p style='font-size:12px'>Người tạo: Phạm Hoàng Long - MSSV: 036208017505</p>", unsafe_allow_html=True)