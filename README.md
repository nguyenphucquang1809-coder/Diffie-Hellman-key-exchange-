# Thỏa thuận khóa Diffie-Hellman & Tấn công Man-in-the-Middle

Mô phỏng giao thức thỏa thuận khóa Diffie-Hellman, minh họa lỗ hổng tấn công người đứng giữa (MitM) và thực nghiệm thuật toán tính lũy thừa nhị phân tối ưu.


## 📁 Cấu trúc Repository
*   `/src`: Chứa mã nguồn cài đặt thuật toán.
    *   `diffie_hellman.py`: Mã nguồn mô phỏng DH cơ bản bằng thuật toán bình phương liên tiếp.
    *   `mitm_attack.py`: Kịch bản mô phỏng kẻ tấn công chặn và tráo đổi tham số (Tùy chọn).
*   `/docs`: Chứa slide bài giảng thuyết trình, sơ đồ khối thuật toán.
*   `/assets`: Hình ảnh minh họa kết quả chạy thử (console log) và tài liệu toán học.

## 🚀 Hướng dẫn khởi chạy mã nguồn

1. **Yêu cầu: Máy tính cài đặt Python 3.x.
2. **Tải mã nguồn:**
   ```bash
   git clone [https://github.com/](https://github.com/)[thay-bang-username-cua-ban]/diffie-hellman-neu.git
   cd diffie-hellman-neu/src
   ```
3. **Chạy thử nghiệm giao thức DH:**
   ```bash
   python diffie_hellman.py
   ```
