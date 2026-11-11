import tkinter as tk
from tkinter import messagebox, ttk

import csdl_sach as db
from mapilot import xu_ly_thong_ke as hien_thi_thong_ke

DANH_SACH_THE_LOAI = ["Ky nang song", "Tieu thuyet", "Lich su", "Khoa hoc", "Kinh te", "Khac"]

class UngDungTuSach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Tu sach ca nhan")
        self.geometry("650x480")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")
        
        tk.Label(khung_nhap, text="Ten sach:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten_sach = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten_sach.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(khung_nhap, text="Tac gia:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_tac_gia = tk.Entry(khung_nhap, width=30)
        self.o_nhap_tac_gia.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="The loai:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_the_loai = ttk.Combobox(khung_nhap, values=DANH_SACH_THE_LOAI, width=27, state="readonly")
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(khung_nhap, text="Them sach", command=self.xu_ly_them_sach).grid(row=3, column=0, columnspan=2, pady=10)
        
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)
        
        self.listbox_sach = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_sach.pack(side="left", fill="both", expand=True)
        
        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sach.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sach.config(yscrollcommand=thanh_cuon.set)
        
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)
        
        tk.Button(khung_nut_thao_tac, text="Danh dau da doc", command=self.xu_ly_danh_dau_da_doc).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut_thao_tac, text="Xoa sach", command=self.xu_ly_xoa_sach).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut_thao_tac, text="Thong ke theo the loai", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach_sach(self):
        self.listbox_sach.delete(0, tk.END)
        self.sach_hien_thi = db.lay_toan_bo_sach()
        for _, ten_sach, tac_gia, the_loai, da_doc in self.sach_hien_thi:
            trang_thai = "Da doc" if da_doc else "Chua doc"
            self.listbox_sach.insert(
                tk.END, f"{ten_sach} - {tac_gia} - {the_loai} ({trang_thai})"
            )

    def xu_ly_them_sach(self):
        ten_sach = self.o_nhap_ten_sach.get().strip()
        tac_gia = self.o_nhap_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get()

        if not ten_sach or not tac_gia:
            messagebox.showwarning("Thieu thong tin", "Vui long nhap ten sach va tac gia.")
            return

        db.them_sach(ten_sach, tac_gia, the_loai)
        self.o_nhap_ten_sach.delete(0, tk.END)
        self.o_nhap_tac_gia.delete(0, tk.END)
        self.tai_lai_danh_sach_sach()

    def xu_ly_danh_dau_da_doc(self):
        lua_chon = self.listbox_sach.curselection()
        if not lua_chon:
            messagebox.showwarning("Chua chon sach", "Vui long chon sach can danh dau.")
            return

        id_sach, _, _, _, da_doc = self.sach_hien_thi[lua_chon[0]]
        if da_doc:
            messagebox.showinfo("Thong tin", "Sach nay da duoc danh dau la da doc.")
            return

        db.danh_dau_da_doc(id_sach)
        self.tai_lai_danh_sach_sach()

    def xu_ly_xoa_sach(self):
        lua_chon = self.listbox_sach.curselection()
        if not lua_chon:
            messagebox.showwarning("Chua chon sach", "Vui long chon sach can xoa.")
            return

        id_sach = self.sach_hien_thi[lua_chon[0]][0]
        if not messagebox.askyesno("Xac nhan", "Ban co chac muon xoa sach nay?"):
            return

        db.xoa_sach(id_sach)
        self.tai_lai_danh_sach_sach()

    def xu_ly_thong_ke(self):
        hien_thi_thong_ke(self)


if __name__ == "__main__":
    app = UngDungTuSach()
    app.mainloop()