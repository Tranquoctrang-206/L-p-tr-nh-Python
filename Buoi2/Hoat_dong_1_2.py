ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

# In kết quả ra màn hình
print("\n--- THONG TIN DA NHAP ---")
print("Ho va ten:", ho_ten)
print("Nam sinh:", nam_sinh)
print("Diem trung binh:", diem_tb)    

print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" : ")
print("Dong 2")  

# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# str.format()
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# toán tử %

print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# Chu thich mot dong: khai bao thong tin sinh vien
# Chu thich nhieu dong:
# Chuong trinh quan ly diem sinh vien - Buoi 2      
ho_ten = "Tran Thi B" # bien luu ho ten
nam_sinh = 2000 # bien luu nam sinh
diem_tb = 8.5 # bien luu diem trung binh

s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)