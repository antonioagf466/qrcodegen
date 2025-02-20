import qrcode
import tkinter as tk
from tkinter import messagebox

def qrcodegen(text, file_name):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def generate_qr():
    text = entry_link.get()
    pick_name = entry_name.get()
    entry_link.delete(0, tk.END)  
    entry_name.delete(0, tk.END)  
    
    if not text or not pick_name:
        messagebox.showwarning("Input Error", "Please fill in both fields.")
        return
    
    file_name = pick_name + "_qrcode.png"
    qrcodegen(text, file_name)
    
    response = messagebox.askyesno("Success", f"QR code saved as {file_name}\nWould you like to create another QR code?")
    
    if not response:  
        root.destroy()  

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")
root.configure(bg="#2e2e2e")


bg_color = "#2e2e2e"
fg_color = "#ffffff"
entry_bg = "#3e3e3e"
entry_fg = "#ffffff"


label_link = tk.Label(root, text="Enter the link:", bg=bg_color, fg=fg_color)
label_link.pack(pady=(10, 0))

entry_link = tk.Entry(root, width=40, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
entry_link.pack(pady=5)

label_name = tk.Label(root, text="Where does this QR code lead to?:", bg=bg_color, fg=fg_color)
label_name.pack(pady=(10, 0))

entry_name = tk.Entry(root, width=40, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
entry_name.pack(pady=5)

button_generate = tk.Button(root, text="Generate QR Code", command=generate_qr, bg="#4e4e4e", fg=fg_color)
button_generate.pack(pady=20)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()