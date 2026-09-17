
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  
print(f"Tên: {ten}")
print(f"Điểm Toán: {diem_toan}")
print(f"Điểm Văn: {diem_van}")
print(f"Số lượng môn học: {so_luong_mon_hoc}")
print(f"Mức lương tối thiểu: {MUC_LUONG_TOI_THIEU}")

#Hoạt động 5
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

#Hoạt động 5.2
diem = 6.5
tuoi = 20
la_loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", la_loai_kha)
ngoai_do_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60 tuổi:", ngoai_do_tuoi_lao_dong)
print("Phủ định loại Khá:", not la_loai_kha)
print("Phủ định điều kiện tuổi:", not ngoai_do_tuoi_lao_dong)
#Hoạt động 5.3
x = 10
x -= 3
print("Sau x -= 3:", x)
x *= 2
print("Sau x *= 2:", x)
x /= 4 
print("Sau x /= 4:", x)
x //= 2
print("Sau x //= 2:", x)
x **= 3
print("Sau x **= 3:", x)
danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach:", 3 in danh_sach)
list1 = danh_sach
list2 = danh_sach
print("list1 is list2:", list1 is list2)
#Hoạt động 6
bien = 10
print(bien, type(bien))
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))
#Hoạt động 6.2
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))