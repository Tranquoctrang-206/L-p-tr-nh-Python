danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]
# Them sinh vien moi
danh_sach_sv.append((8.0, "Em"))
danh_sach_sv.remove((7.0, "Binh"))
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)
danh_sach_sv.sort()
print("Danh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")
# Sap xep giam dan
danh_sach_sv.sort(reverse=True)
print("Danh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")