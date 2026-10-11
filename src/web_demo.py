import time
import streamlit as st
from dh_algorithm import tinh_khoa_cong_khai, tinh_khoa_chung

st.set_page_config(page_title="Diffie-Hellman", layout="centered")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

html, body, [data-testid="stAppViewContainer"] {
    background-color: #fafafa !important;
    color: #111 !important;
}
[data-testid="stHeader"] { background-color: #fafafa !important; }

.block-container { max-width: 640px; padding-top: 3rem; }
h1 { font-weight: 400; font-size: 1.4rem; letter-spacing: 0.05em; }
hr { margin: 1.5rem 0; border-color: #ddd; }

/* ô nhập số, chữ trong box */
input, .stNumberInput input {
    background-color: #fff !important;
    color: #111 !important;
    border: 1px solid #ddd !important;
}

/* nút bấm */
.stButton button {
    background-color: #111 !important;
    color: #fff !important;
    border-radius: 8px !important;
    border: none !important;
    transition: transform 0.15s ease, background-color 0.2s ease;
}
.stButton button:hover {
    background-color: #333 !important;
    transform: scale(1.02);
}

/* khung A <-> B có mũi tên chạy */
.flow-box {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 1.5rem 0;
    font-family: monospace;
}
.flow-node {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    background: #fff;
}
.flow-arrow {
    flex: 1;
    height: 2px;
    background: repeating-linear-gradient(
        90deg, #111 0, #111 6px, transparent 6px, transparent 12px
    );
    background-size: 24px 2px;
    animation: slide 0.8s linear infinite;
    margin: 0 0.8rem;
}
@keyframes slide {
    from { background-position: 0 0; }
    to   { background-position: 24px 0; }
}

/* chữ hiện dần */
.fade-in {
    animation: fadein 0.6s ease forwards;
    opacity: 0;
}
@keyframes fadein {
    to { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("## DIFFIE–HELLMAN")
st.caption("Mô phỏng trao đổi khóa")
st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    p = st.number_input("Số nguyên tố p", value=23, min_value=2)
    g = st.number_input("Cơ số g", value=5, min_value=2)
with c2:
    a = st.number_input("Khóa riêng A", value=6, min_value=1)
    b = st.number_input("Khóa riêng B", value=15, min_value=1)

st.markdown("---")

if st.button("Tính", use_container_width=True):
    a_pub = tinh_khoa_cong_khai(g, a, p)
    b_pub = tinh_khoa_cong_khai(g, b, p)

    with st.spinner("Đang trao đổi khóa công khai..."):
        time.sleep(0.8)

    st.markdown(f"""
    <div class="flow-box fade-in">
        <div class="flow-node">A<br>{a_pub}</div>
        <div class="flow-arrow"></div>
        <div class="flow-node">B<br>{b_pub}</div>
    </div>
    """, unsafe_allow_html=True)

    khoa_chung_a = tinh_khoa_chung(b_pub, a, p)
    khoa_chung_b = tinh_khoa_chung(a_pub, b, p)

    with st.spinner("Mỗi bên tự tính khóa chung..."):
        time.sleep(0.8)

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.text(f"A tính được : {khoa_chung_a}")
    st.text(f"B tính được : {khoa_chung_b}")
    st.markdown("---")
    if khoa_chung_a == khoa_chung_b:
        st.text(f"Khớp — khóa chung = {khoa_chung_a}")
    else:
        st.text("Không khớp")
    st.markdown("</div>", unsafe_allow_html=True)