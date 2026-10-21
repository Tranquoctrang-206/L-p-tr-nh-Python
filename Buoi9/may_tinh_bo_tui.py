import tkinter as tk
from tkinter import messagebox
import math

# --- PHẦN LOGIC ---
def click_nut(gia_tri):
    bien_hien_thi.set(bien_hien_thi.get() + str(gia_tri))

def xoa_trang():
    bien_hien_thi.set("")

def xoa_mot_ky_tu():
    """Xóa ký tự cuối cùng trong chuỗi hiện tại"""
    hien_tai = bien_hien_thi.get()
    bien_hien_thi.set(hien_tai[:-1])

def tinh_can():
    """Tính toán biểu thức hiện tại trước, sau đó lấy căn bậc 2"""
    try:
        # Nếu màn hình trống thì coi như là 0
        bieu_thuc = bien_hien_thi.get()
        if not bieu_thuc:
            return
        
        gia_tri = eval(bieu_thuc)
        if gia_tri < 0:
            messagebox.showerror("Lỗi", "Không thể tính căn số âm!")
            bien_hien_thi.set("")
        else:
            ket_qua = math.sqrt(gia_tri)
            # Nếu kết quả là số nguyên thì bỏ phần .0 đi cho đẹp
            if ket_qua.is_integer():
                bien_hien_thi.set(str(int(ket_qua)))
            else:
                bien_hien_thi.set(str(ket_qua))
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức lỗi!")
        bien_hien_thi.set("")

def tinh_toan():
    try:
        ket_qua = str(eval(bien_hien_thi.get()))
        bien_hien_thi.set(ket_qua)
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0!")
        bien_hien_thi.set("")
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức lỗi!")
        bien_hien_thi.set("")

# --- PHẦN GIAO DIỆN ---
root = tk.Tk()
root.title("Máy Tính Hiện Đại")
root.geometry("320x540") # Tăng chiều cao cửa sổ để chứa 5 hàng phím
root.configure(bg="#1C1C1C")
root.resizable(False, False)

bien_hien_thi = tk.StringVar()

# 1. Màn hình
man_hinh = tk.Entry(
    root, 
    textvariable=bien_hien_thi, 
    font=('Helvetica', 40), 
    bg="#1C1C1C", fg="#FFFFFF", bd=0, justify='right', state='readonly',
    readonlybackground="#1C1C1C"
)
man_hinh.pack(fill="x", padx=15, pady=25)

# 2. Khung chứa phím bấm
frame_ban_phim = tk.Frame(root, bg="#1C1C1C")
frame_ban_phim.pack(expand=True, fill="both", padx=10, pady=10)

# Cấu hình grid cho 5 hàng và 4 cột
for i in range(4):
    frame_ban_phim.columnconfigure(i, weight=1)
for i in range(5):
    frame_ban_phim.rowconfigure(i, weight=1)

# Danh sách nút: Thêm hàng trên cùng (C, >, √, /) và nút 00, dấu chấm (.)
cau_hinh_nut = [
    ('C', '#A5A5A5', '#000000', 0, 0), ('>', '#A5A5A5', '#000000', 0, 1), ('√', '#A5A5A5', '#000000', 0, 2), ('/', '#FF9F0A', '#FFFFFF', 0, 3),
    ('7', '#333333', '#FFFFFF', 1, 0), ('8', '#333333', '#FFFFFF', 1, 1), ('9', '#333333', '#FFFFFF', 1, 2), ('*', '#FF9F0A', '#FFFFFF', 1, 3),
    ('4', '#333333', '#FFFFFF', 2, 0), ('5', '#333333', '#FFFFFF', 2, 1), ('6', '#333333', '#FFFFFF', 2, 2), ('-', '#FF9F0A', '#FFFFFF', 2, 3),
    ('1', '#333333', '#FFFFFF', 3, 0), ('2', '#333333', '#FFFFFF', 3, 1), ('3', '#333333', '#FFFFFF', 3, 2), ('+', '#FF9F0A', '#FFFFFF', 3, 3),
    ('00', '#333333', '#FFFFFF', 4, 0), ('0', '#333333', '#FFFFFF', 4, 1), ('.', '#333333', '#FFFFFF', 4, 2), ('=', '#FF9F0A', '#FFFFFF', 4, 3)
]

# Tạo nút
for (nhan, mau_nen, mau_chu, hang, cot) in cau_hinh_nut:
    if nhan == '=':
        lenh = tinh_toan
    elif nhan == 'C':
        lenh = xoa_trang
    elif nhan == '>':
        lenh = xoa_mot_ky_tu
    elif nhan == '√':
        lenh = tinh_can
    else:
        lenh = lambda t=nhan: click_nut(t)
    
    btn = tk.Button(
        frame_ban_phim, text=nhan, font=('Helvetica', 18), 
        bg=mau_nen, fg=mau_chu, activebackground="#555555", activeforeground="#FFFFFF",
        relief="flat", command=lenh
    )
    btn.grid(row=hang, column=cot, sticky="nsew", padx=2, pady=2)

root.mainloop()