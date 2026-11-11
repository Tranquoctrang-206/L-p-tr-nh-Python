from tkinter import messagebox

import csdl_sach as db


def xu_ly_thong_ke(cua_so):
    """Ve bieu do so luong sach theo the loai."""
    data = db.thong_ke_theo_the_loai()
    if not data:
        messagebox.showinfo("Thong bao", "Chua co du lieu sach de thong ke.")
        return

    try:
        import matplotlib

        matplotlib.use("TkAgg")
        import matplotlib.pyplot as plt
    except ImportError:
        messagebox.showerror(
            "Thieu thu vien",
            "Can cai dat matplotlib de xem bieu do (pip install matplotlib).",
        )
        return

    the_loai, so_luong = zip(*data)
    plt.figure(figsize=(7, 5))
    cot = plt.bar(the_loai, so_luong, color="#5B9BD5", width=0.45)
    plt.bar_label(cot, padding=3, fontweight="bold")
    plt.title("So luong sach theo the loai", fontweight="bold", pad=15)
    plt.xlabel("The loai")
    plt.ylabel("So luong sach")
    plt.ylim(0, max(so_luong) + 1.5)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
