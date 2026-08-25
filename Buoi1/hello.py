ten = "Sinh vien"
print("Xin chao,", ten)
print("Day la chuong trinh Python dau tien cua toi.")
# Đặt lại tên biến và hằng số theo chuẩn PEP8
ho_ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  # Hằng số

# In toàn bộ thông tin ra màn hình
print("Họ và tên:", ho_ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)
import keyword

# 1. Liệt kê từ khóa
print(keyword.kwlist)
print("Số lượng từ khóa:", len(keyword.kwlist))

# 2. Cố tình thử đặt tên biến trùng từ khóa để quan sát lỗi
# class = 5  # Nếu bỏ comment, Python sẽ báo lỗi SyntaxError: invalid syntax
# Vì class là từ khóa của Python, nên không thể dùng làm tên biến.

a = 17
b = 5

print("a + b =", a + b)  # 22
print("a - b =", a - b)  # 12
print("a * b =", a * b)  # 85
print("a / b =", a / b)  # 3.4
print("a // b =", a // b)  # 3
print("a % b =", a % b)  # 2
print("a ** b =", a**b)  # 1419857

diem = 6.5
tuoi = 20

# 1. Điểm đạt loại Khá (từ 6.5 đến dưới 8.0)
la_loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Đạt loại Khá:", la_loai_kha)  # True

# 2. Tuổi dưới 18 hoặc trên 60
ngoai_do_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("Dưới 18 hoặc trên 60:", ngoai_do_tuoi_lao_dong)  # False

# 3. Phủ định điều kiện điểm loại Khá bằng not
khong_phai_kha = not la_loai_kha
print("Không phải loại Khá:", khong_phai_kha)  # False

x = 10

x += 5
print("Sau x += 5:", x)  # 15

x -= 3
print("Sau x -= 3:", x)  # 12

x *= 2
print("Sau x *= 2:", x)  # 24

x /= 4
print("Sau x /= 4:", x)  # 6.0

x //= 2
print("Sau x //= 2:", x)  # 3.0

x **= 3
print("Sau x **= 3:", x)  # 27.0

# Toán tử đặc biệt
danh_sach = [1, 2, 3, "python"]

# Kiểm tra sự tồn tại bằng 'in'
print(3 in danh_sach)  # True

# So sánh 2 biến cùng tham chiếu đối tượng bằng 'is'
danh_sach_2 = danh_sach
print(danh_sach_2 is danh_sach)  # True

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

# 1. Khai báo thông tin và điểm các môn
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

# 2. Tính điểm trung bình
dtb = (diem_toan + diem_ly + diem_hoa) / 3

# 3. Kiểm tra các điều kiện xếp loại (Trả về True/False)
la_gioi = dtb >= 8.0
la_kha = (dtb >= 6.5) and (dtb < 8.0)
la_trung_binh = (dtb >= 5.0) and (dtb < 6.5)
la_yeu = dtb < 5.0

# 4. In kết quả ra màn hình
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))