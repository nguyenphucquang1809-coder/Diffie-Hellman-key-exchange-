# Diffie-Hellman Key Exchange & MitM Attack Simulation

---

## Mục lục nhanh

* [1. Tìm hiểu hệ mã](#1-tìm-hiểu-hệ-mã)
* [2. Thực thi hệ mã](#2-thực-thi-hệ-mã)
  * [`dh_algorithm.py`](./src/core/dh_algorithm.py) - Thuật toán lũy thừa mod $O(\log n)$
  * [`mitm_simulation.py`](./src/core/mitm_simulation.py) - Mô phỏng tấn công MitM
  * [`test_dh.py`](./src/tests/test_dh.py) - Bộ kiểm thử test cases
* [3. Chạy demo](#3-chạy-demo)
* [4. Báo cáo & Phân công](#4-báo-cáo--phân-công)

---

## 1. Tìm hiểu hệ mã

* **Bối cảnh:** Whitfield Diffie & Martin Hellman (1976). Giải quyết bài toán phân phối khóa trên kênh truyền mở.
* **Cơ chế:**
  * Tham số công khai: Số nguyên tố $p$, căn nguyên thủy $g$.
  * Khóa công khai: $A = g^a \bmod p$ (Alice), $B = g^b \bmod p$ (Bob).
  * Khóa bí mật chung: $K = B^a \bmod p = A^b \bmod p = g^{ab} \bmod p$.
* **Ví dụ số nhỏ ($p=19, g=2$):**
  * A ($a=8$) -> $A = 2^8 \bmod 19 = 9$.
  * B ($b=5$) -> $B = 2^5 \bmod 19 = 13$.
  * Khóa chung: $K = 13^8 \bmod 19 = 9^5 \bmod 19 = 16$.
* **Độ an toàn:** Dựa trên bài toán Logarit rời rạc (DLP). Điểm yếu: Không xác thực danh tính, dễ bị tấn công Man-in-the-Middle (MitM).
* **So sánh RSA:** Diffie-Hellman có Forward Secrecy (bản DHE) nhưng chỉ dùng để thỏa thuận khóa, không dùng mã hóa dữ liệu trực tiếp hay ký số như RSA.

---

## 2. Thực thi hệ mã

Cấu trúc thư mục:

```text
├── README.md
├── docs/
│   └── Bao_Cao.pdf
└── src/
    ├── core/
    │   ├── dh_algorithm.py
    │   ├── aes_cipher.py
    │   └── mitm_simulation.py
    ├── tests/
    │   └── test_dh.py
    └── main.py
