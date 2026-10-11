import streamlit as st
from dh_algorithm import tinh_khoa_cong_khai, tinh_khoa_chung

st.set_page_config(page_title="Diffie-Hellman", layout="centered")

# Ẩn bớt các chi tiết thừa của Streamlit (menu, footer) cho gọn
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
body { font-family: 'Courier New', monospace; }
.block-container { max-width: 640px; padding-top: 3rem; }
h1 { font-weight: 400; font-size: 1.4rem; letter-spacing: 0.05em; }
hr { margin: 1.5rem 0; border-color: #333; }
</style>
""", unsafe_allow_html=True)

st.markdown("## DIFFIE–HELLMAN")
st.caption("mo phong trao doi khoa")

st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    p = st.number_input("p", value=23, min_value=2)
    g = st.number_input("g", value=5, min_value=2)
with c2:
    a = st.number_input("khoa rieng A", value=6, min_value=1)
    b = st.number_input("khoa rieng B", value=15, min_value=1)

st.markdown("---")

if st.button("tinh", use_container_width=True):
    a_pub = tinh_khoa_cong_khai(g, a, p)
    b_pub = tinh_khoa_cong_khai(g, b, p)
    khoa_chung_a = tinh_khoa_chung(b_pub, a, p)
    khoa_chung_b = tinh_khoa_chung(a_pub, b, p)

    st.text(f"A gui cho B   : {a_pub}")
    st.text(f"B gui cho A   : {b_pub}")
    st.markdown("---")
    st.text(f"A tinh duoc   : {khoa_chung_a}")
    st.text(f"B tinh duoc   : {khoa_chung_b}")
    st.markdown("---")

    if khoa_chung_a == khoa_chung_b:
        st.text(f"khop — khoa chung = {khoa_chung_a}")
    else:
        st.text("khong khop")