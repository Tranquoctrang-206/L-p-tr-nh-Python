#Hoạt động 4: 
#Bàtập 4.1 
toa_do = (3, 5)
print(toa_do, type(toa_do))
x, y = toa_do
print("x =", x, "- y =", y)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

#Bài tập 4.3
c, d = 17, 5
thuong_du = divmod(c, d) 
thuong, du = thuong_du
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

#Hoạt động 5: 
import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b
khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")
#Yêu cầu:
import math
cac_diem = [(0, 0), (3, 4), (6, 8)]
for x, y in cac_diem:
    khoang_cach = math.sqrt(x**2 + y**2) 
    print(f"Khoảng cách từ điểm ({x}, {y}) đến gốc tọa độ: {khoang_cach}")