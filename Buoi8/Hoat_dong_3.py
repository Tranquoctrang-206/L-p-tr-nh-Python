#Hoạt động 3: Bố cục – pack(), grid(), place()
#Dựng cùng một giao diện mẫu (3 Label + 2 Button) lần lượt bằng 3 cách bố cục để so sánh.
#Bài tập 3.1 – Bố cục bằng pack():
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Bo cuc bang pack()")
cua_so.geometry("300x250")
tk.Label(cua_so, text="Ho ten:").pack(pady=5)
tk.Label(cua_so, text="Tuoi:").pack(pady=5)
tk.Label(cua_so, text="Email:").pack(pady=5)
tk.Button(cua_so, text="Dong y").pack(side="left", padx=20, pady=15)
tk.Button(cua_so, text="Huy").pack(side="right", padx=20, pady=15)
cua_so.mainloop()

#Bài tập 3.2 – Cùng giao diện, bố cục bằng grid():

import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Bo cuc bang grid()")
cua_so.geometry("300x250")
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Button(cua_so, text="Dong y").grid(row=3, column=0, padx=10, pady=15)
tk.Button(cua_so, text="Huy").grid(row=3, column=1, padx=10, pady=15)
cua_so.mainloop()

#Bài tập 3.3 – Cùng giao diện, bố cục bằng place():
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Bo cuc bang place()")
cua_so.geometry("300x250")
tk.Label(cua_so, text="Ho ten:").place(x=20, y=20)
tk.Label(cua_so, text="Tuoi:").place(x=20, y=60)
tk.Label(cua_so, text="Email:").place(x=20, y=100)
tk.Button(cua_so, text="Dong y").place(x=40, y=160)
tk.Button(cua_so, text="Huy").place(x=150, y=160)
cua_so.mainloop()