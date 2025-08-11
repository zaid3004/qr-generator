import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

img = None

def generate_QR():
    global img
    data = entry.get()
    if data.strip() == "":
        messagebox.showwarning("Input required", "Please enter a valid link, UPI ID, or text.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_disp = img.resize((200, 200))
    tk_img = ImageTk.PhotoImage(img_disp)
    qr_label.config(image=tk_img)
    qr_label.image = tk_img
    
    result_label.config(text="QR code generated successfully!")

def save_as_pdf():
    global img
    if img is None:
        messagebox.showwarning("No QR Code", "Please generate a QR code first.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("PNG files", "*.png")],
        title="Save QR Code As"
    )

    if not file_path:
        return

    try:
        if file_path.lower().endswith(".pdf"):
            img.save(file_path, "PDF")
        else:
            img.save(file_path, "PNG")
        messagebox.showinfo("Saved", f"Image saved as '{file_path}'")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x500")

tk.Label(root, text="Enter URL, UPI ID, or any text: ").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate QR", command=generate_QR)
generate_btn.pack(pady=10)

save_btn = tk.Button(root, text="Save QR Code", command=save_as_pdf)
save_btn.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

text_label = tk.Label(root, text="")
text_label.pack()

root.mainloop()
