
def nhap_so_thuc(thong_bao, toi_thieu=None):
    """Hàm bắt buộc nhập đúng số thực/số nguyên dương bằng try-except."""
    while True:
        try:
            val = float(input(thong_bao))
            if toi_thieu is not None and val < toi_thieu:
                print(f" Giá trị phải >= {toi_thieu}. Vui lòng nhập lại!")
                continue
            return val
        except ValueError:
            print(" Dữ liệu không hợp lệ! Vui lòng nhập vào một số.")


def nhap_so_nguyen(thong_bao, toi_thieu=None):
    """Hàm bắt buộc nhập đúng số nguyên bằng try-except."""
    while True:
        try:
            val = int(input(thong_bao))
            if toi_thieu is not None and val < toi_thieu:
                print(f" Giá trị phải >= {toi_thieu}. Vui lòng nhập lại!")
                continue
            return val
        except ValueError:
            print(" Dữ liệu không hợp lệ! Vui lòng nhập vào một số nguyên.")


def hien_thi_danh_sach_kho(ds_kho):
    """Chức năng 1: Hiển thị danh sách toàn bộ nguyên liệu trong kho"""
    print("\n--- DANH SÁCH TỒN KHO NGUYÊN LIỆU TRÀ SỮA ---")
    if not ds_kho:
        print("Kho hiện đang trống!")
        return
    
    print(f"{'Mã NL':<8} | {'Tên nguyên liệu':<22} | {'ĐVT':<8} | {'Tồn kho':<10} | {'Đơn giá (VNĐ)':<14} | {'Trạng thái':<15}")
    print("-" * 88)
    for nl in ds_kho:
        trang_thai = " SẮP HẾT" if nl["so_luong"] <= nl["nguong_canh_bao"] else " An toàn"
        print(f"{nl['ma_nl']:<8} | {nl['ten_nl']:<22} | {nl['dvt']:<8} | {nl['so_luong']:<10.2f} | {nl['don_gia']:<14,.0f} | {trang_thai:<15}")


def xem_nguyen_lieu_sap_het(ds_kho):
    """Chức năng 2: Xem danh sách nguyên liệu chạm ngưỡng cảnh báo cần nhập gấp"""
    print("\n--- CẢNH BÁO NGUYÊN LIỆU SẮP HẾT ---")
    ds_sap_het = [nl for nl in ds_kho if nl["so_luong"] <= nl["nguong_canh_bao"]]
    
    if not ds_sap_het:
        print("Tất cả nguyên liệu trong kho đều đang ở mức an toàn!")
        return

    print(f"{'Mã NL':<8} | {'Tên nguyên liệu':<22} | {'ĐVT':<8} | {'Tồn hiện tại':<12} | {'Ngưỡng tối thiểu':<15}")
    print("-" * 75)
    for nl in ds_sap_het:
        print(f"{nl['ma_nl']:<8} | {nl['ten_nl']:<22} | {nl['dvt']:<8} | {nl['so_luong']:<12.2f} | {nl['nguong_canh_bao']:<15.2f}")


def them_nguyen_lieu_moi(ds_kho):
    """Chức năng 3: Khai báo nguyên liệu mới vào kho"""
    print("\n--- THÊM NGUYÊN LIỆU MỚI ---")
    ma_nl = input("Nhập mã nguyên liệu mới (ví dụ NL04): ").strip().upper()
    
    for nl in ds_kho:
        if nl["ma_nl"] == ma_nl:
            print(f" Mã nguyên liệu '{ma_nl}' đã tồn tại trong hệ thống!")
            return

    ten_nl = input("Nhập tên nguyên liệu: ").strip()
    while not ten_nl:
        print(" Tên nguyên liệu không được để trống!")
        ten_nl = input("Nhập tên nguyên liệu: ").strip()

    dvt = input("Nhập đơn vị tính (kg, lít, hộp, túi...): ").strip()
    so_luong = nhap_so_thuc("Nhập số lượng ban đầu: ", toi_thieu=0)
    don_gia = nhap_so_thuc("Nhập đơn giá nhập kho (VNĐ/ĐVT): ", toi_thieu=0)
    nguong_canh_bao = nhap_so_thuc("Nhập ngưỡng cảnh báo sắp hết: ", toi_thieu=0)

    ds_kho.append({
        "ma_nl": ma_nl,
        "ten_nl": ten_nl,
        "dvt": dvt,
        "so_luong": so_luong,
        "don_gia": don_gia,
        "nguong_canh_bao": nguong_canh_bao
    })
    print(f" Đã thêm nguyên liệu '{ten_nl}' ({ma_nl}) vào kho thành công!")


def nhap_kho(ds_kho):
    """Chức năng 4: Nhập thêm số lượng cho nguyên liệu đã có sẵn"""
    print("\n--- NHẬP HÀNG VÀO KHO ---")
    ma_nl = input("Nhập mã nguyên liệu cần nhập thêm: ").strip().upper()
    
    for nl in ds_kho:
        if nl["ma_nl"] == ma_nl:
            so_luong_nhap = nhap_so_thuc(f"Nhập số lượng thêm ({nl['dvt']}): ", toi_thieu=0.1)
            nl["so_luong"] += so_luong_nhap
            print(f" Đã nhập thêm {so_luong_nhap} {nl['dvt']} '{nl['ten_nl']}'. Tồn kho mới: {nl['so_luong']:.2f} {nl['dvt']}")
            return

    print(f" Không tìm thấy nguyên liệu có mã '{ma_nl}'.")


def xuat_kho(ds_kho, lich_su_giao_dich):
    """Chức năng 5: Xuất kho sử dụng nguyên liệu cho pha chế"""
    print("\n--- XUẤT KHO NGUYÊN LIỆU PHAC HẾ ---")
    ma_nl = input("Nhập mã nguyên liệu cần xuất: ").strip().upper()

    for nl in ds_kho:
        if nl["ma_nl"] == ma_nl:
            print(f"Nguyên liệu: {nl['ten_nl']} | Tồn kho hiện tại: {nl['so_luong']:.2f} {nl['dvt']}")
            so_luong_xuat = nhap_so_thuc(f"Nhập số lượng cần xuất ({nl['dvt']}): ", toi_thieu=0.1)

            if so_luong_xuat > nl["so_luong"]:
                print(f" Số lượng trong kho không đủ để xuất! (Chỉ còn {nl['so_luong']:.2f} {nl['dvt']})")
                return

            nl["so_luong"] -= so_luong_xuat
            tong_gia_tri = so_luong_xuat * nl["don_gia"]

            lich_su_giao_dich.append({
                "ma_nl": nl["ma_nl"],
                "ten_nl": nl["ten_nl"],
                "so_luong": so_luong_xuat,
                "dvt": nl["dvt"],
                "tong_tien": tong_gia_tri
            })

            print(f" Xuất kho thành công {so_luong_xuat:.2f} {nl['dvt']} '{nl['ten_nl']}'. Giá trị xuất: {tong_gia_tri:,.0f} VNĐ")
            if nl["so_luong"] <= nl["nguong_canh_bao"]:
                print(f"CẢNH BÁO: Nguyên liệu '{nl['ten_nl']}' hiện chỉ còn {nl['so_luong']:.2f} {nl['dvt']}!")
            return

    print(f" Không tìm thấy nguyên liệu có mã '{ma_nl}'.")


def thong_ke_kho(ds_kho, lich_su_giao_dich):
    """Chức năng 6: Thống kê tổng giá trị tồn kho và giá trị đã xuất"""
    print("\n--- THỐNG KÊ TỔNG QUAN KHO TRÀ SỮA ---")

    tong_gia_tri_ton = sum(nl["so_luong"] * nl["don_gia"] for nl in ds_kho)
    print(f"📦 Tổng giá trị hàng tồn kho hiện tại: {tong_gia_tri_ton:,.0f} VNĐ")


    print("\n--- LỊCH SỬ XUẤT KHO PHAC HẾ ---")
    if not lich_su_giao_dich:
        print("Chưa có lượt xuất kho nào được ghi nhận.")
        return

    print(f"{'Mã NL':<8} | {'Tên nguyên liệu':<22} | {'Số lượng xuất':<15} | {'Thành tiền (VNĐ)':<15}")
    print("-" * 68)
    tong_xuat = 0
    for gd in lich_su_giao_dich:
        sl_str = f"{gd['so_luong']:.2f} {gd['dvt']}"
        print(f"{gd['ma_nl']:<8} | {gd['ten_nl']:<22} | {sl_str:<15} | {gd['tong_tien']:<15,.0f}")
        tong_xuat += gd["tong_tien"]

    print("-" * 68)
    print(f"👉 TỔNG GIÁ TRỊ NGUYÊN LIỆU ĐÃ XUẤT: {tong_xuat:,.0f} VNĐ")

def main():
    # Dữ liệu khởi tạo ban đầu cho quán trà sữa
    danh_sach_kho = [
        {"ma_nl": "NL01", "ten_nl": "Trân châu đen", "dvt": "kg", "so_luong": 12.0, "don_gia": 45000, "nguong_canh_bao": 5.0},
        {"ma_nl": "NL02", "ten_nl": "Trà đen Ô Long", "dvt": "kg", "so_luong": 2.5, "don_gia": 200000, "nguong_canh_bao": 3.0},
        {"ma_nl": "NL03", "ten_nl": "Bột sữa cao cấp", "dvt": "kg", "so_luong": 20.0, "don_gia": 85000, "nguong_canh_bao": 8.0},
        {"ma_nl": "NL04", "ten_nl": "Sữa đặc Ngôi Sao", "dvt": "hộp", "so_luong": 4.0, "don_gia": 22000, "nguong_canh_bao": 10.0}
    ]
    
    lich_su_giao_dich = []

    while True:
        print("\n" + "=" * 48)
        print("    HỆ THỐNG QUẢN LÝ KHO TRÀ SỮA MINI    ")
        print("=" * 48)
        print("1. Hiển thị toàn bộ danh sách tồn kho")
        print("2. Xem nguyên liệu sắp hết (Cần nhập gấp)")
        print("3. Thêm nguyên liệu mới vào danh mục")
        print("4. Nhập thêm hàng vào kho")
        print("5. Xuất kho nguyên liệu pha chế")
        print("6. Thống kê giá trị kho & Lịch sử xuất")
        print("0. Thoát chương trình")
        print("=" * 48)

        lua_chon = nhap_so_nguyen("Mời bạn chọn chức năng (0-6): ", toi_thieu=0)

        if lua_chon == 1:
            hien_thi_danh_sach_kho(danh_sach_kho)
        elif lua_chon == 2:
            xem_nguyen_lieu_sap_het(danh_sach_kho)
        elif lua_chon == 3:
            them_nguyen_lieu_moi(danh_sach_kho)
        elif lua_chon == 4:
            nhap_kho(danh_sach_kho)
        elif lua_chon == 5:
            xuat_kho(danh_sach_kho, lich_su_giao_dich)
        elif lua_chon == 6:
            thong_ke_kho(danh_sach_kho, lich_su_giao_dich)
        elif lua_chon == 0:
            print("\nCảm ơn bạn đã sử dụng phần mềm quản lý kho trà sữa! Tạm biệt.")
            break
        else:
            print("Lựa chọn không nằm trong menu. Vui lòng chọn từ 0 đến 6!")


if __name__ == "__main__":
    main()