def tinh_luy_thua_mod(g, m, p):   # g: co so, m: so mu, p: so nguyen to
    kq = 1
    luy_thua = g % p
    while m > 0:
        if m % 2 == 1:
            kq = kq * luy_thua % p # cập nhật kết quả
        luy_thua = luy_thua * luy_thua % p  # cập nhật lũy thừa || (a * b) mod n = [ (a mod n) * (b mod n) ] mod n
        m = m // 2
    return kq 

def tinh_khoa_cong_khai(c, khoa_rieng,p):
    kq = tinh_luy_thua_mod(c, khoa_rieng,p)
    return kq

def tinh_khoa_chung(khoa_cong_khai_doi_phuong, khoa_rieng, p):
    kq = tinh_luy_thua_mod(khoa_cong_khai_doi_phuong, khoa_rieng, p)
    return kq