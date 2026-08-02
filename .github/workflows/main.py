import tkinter as tk
from tkinter import messagebox

items = []

def add_item():
    name = name_entry.get()
    price = price_entry.get()
    
    if name and price.isdigit():
        p = int(price)
        items.append((name, p))
        listbox.insert(tk.END, f"{name}: {p}円")
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        calc_total()
    else:
        messagebox.showwarning("注意", "金額は半角の数字で入力してね！")

def delete_item(event):
    selected_index = listbox.nearest(event.y)
    if selected_index >= 0 and items:
        item_name = items[selected_index][0]
        if messagebox.askyesno("削除確認", f"「{item_name}」をリストから削除する？"):
            listbox.delete(selected_index)
            del items[selected_index]
            calc_total()

def calc_total():
    subtotal = sum(p for n, p in items)
    tax_rate = tax_var.get() / 100
    tax_amount = int(subtotal * tax_rate)
    total = subtotal + tax_amount
    
    if items:
        formula_str = " + ".join([f"{n}{p:,}円" for n, p in items]) + f" ＝ {subtotal:,}円"
    else:
        formula_str = "計算式: なし"
    
    formula_label.config(text=formula_str)
    subtotal_label.config(text=f"小計（税抜）: {subtotal:,} 円")
    total_label.config(text=f"税込合計: {total:,} 円 (税: {tax_amount:,}円)")

root = tk.Tk()
root.title("電卓")
root.geometry("380x560")

tk.Label(root, text="商品名").pack(pady=(10,0))
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="金額").pack(pady=(5,0))
price_entry = tk.Entry(root)
price_entry.pack()

add_btn = tk.Button(root, text="リストに追加", command=add_item, bg="#e1f5fe")
add_btn.pack(pady=10)

tk.Label(root, text="", fg="gray").pack()

listbox = tk.Listbox(root, height=7, font=("", 10))
listbox.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
listbox.bind("<Button-2>", delete_item)
listbox.bind("<Button-3>", delete_item)

tax_frame = tk.Frame(root)
tax_frame.pack(pady=5)
tax_var = tk.IntVar(value=10)

tk.Label(tax_frame, text="税率:").pack(side=tk.LEFT)
tk.Radiobutton(tax_frame, text="10%", variable=tax_var, value=10, command=calc_total).pack(side=tk.LEFT)
tk.Radiobutton(tax_frame, text="8%(軽減税率)", variable=tax_var, value=8, command=calc_total).pack(side=tk.LEFT)
tk.Radiobutton(tax_frame, text="0%(非課税)", variable=tax_var, value=0, command=calc_total).pack(side=tk.LEFT)

formula_label = tk.Label(root, text="計算式: なし", font=("", 9), fg="#555555", wraplength=340)
formula_label.pack(pady=(5, 0))

subtotal_label = tk.Label(root, text="小計（税抜）: 0 円", font=("", 10))
subtotal_label.pack(pady=(5, 0))

total_label = tk.Label(root, text="税込合計: 0 円", font=("", 13, "bold"), fg="#d32f2f")
total_label.pack(pady=(0, 15))

root.mainloop()
