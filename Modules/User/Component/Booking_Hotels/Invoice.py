

# import Modules.User.User_Landing_Process as up
from tkinter import *
import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from tkinter import ttk, messagebox
from pathlib import Path
from pymongo import MongoClient
from datetime import datetime
import uuid
import subprocess


class Invoice_View:
    def __init__(self):
        self.window = tk.Tk()

        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 693
        self.window_height = 496
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Invoice")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        assets_path = Path(r"D:\uel_form-master\Image\User\Invoice")

        self.image_refs = {}


        try:
            self.image_refs['background'] = PhotoImage(file=assets_path / "Background.png")
            self.image_refs['signout'] = PhotoImage(file=assets_path / "Button_Signout.png")
            self.image_refs['account'] = PhotoImage(file=assets_path / "Button_Account.png")
            self.image_refs['addtocart'] = PhotoImage(file=assets_path / "Button_Addtocart.png")
            self.image_refs['invoice'] = PhotoImage(file=assets_path / "Button_Invoice.png")
            self.image_refs['process'] = PhotoImage(file=assets_path / "Button_Process.png")
            self.image_refs['quit'] = PhotoImage(file=assets_path / "Button_Quit.png")
            self.image_refs['remove'] = PhotoImage(file=assets_path / "Button_Remove.png")
            self.image_refs['rooms'] = PhotoImage(file=assets_path / "Button_Rooms.png")
            self.image_refs['textbox1'] = PhotoImage(file=assets_path / "Textbox1.png")
            self.image_refs['textbox2'] = PhotoImage(file=assets_path / "Textbox2.png")
        except Exception as e:
            print(f"Lỗi tải hình ảnh: {e}")
        print("Danh sách ảnh đã load:", self.image_refs.keys())
        self.background = self.canvas.create_image(342.0, 246.0, image=self.image_refs['background'])
        self.canvas.update_idletasks()
        self.rooms_button = Button(image=self.image_refs['rooms'], borderwidth=0, highlightthickness=0,command=self.go_to_main_view)
        self.rooms_button.place(x=59, y=86, width=93, height=34)

        self.account_button = Button(image=self.image_refs['account'], borderwidth=0, highlightthickness=0)
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.invoice_button = Button(image=self.image_refs['invoice'], borderwidth=0, highlightthickness=0,command=self.go_to_invoice_page)
        self.invoice_button.place(x=223, y=86, width=93, height=34)

        self.signout_button = Button(image=self.image_refs['signout'], borderwidth=0, highlightthickness=0,command=self.go_to_signout_page)
        self.signout_button.place(x=387, y=86, width=93, height=34)

        self.quit_button = Button(image=self.image_refs['quit'], borderwidth=0, highlightthickness=0,command=self.go_to_landing_page)
        self.quit_button.place(x=551, y=86, width=91.22, height=34)

        self.addtocart_button = Button(image=self.image_refs['addtocart'], borderwidth=0, highlightthickness=0, command=self.add_to_cart)
        self.addtocart_button.place(x=435, y=385, width=70.7, height=19.26)

        self.remove_button = Button(image=self.image_refs['remove'], borderwidth=0, highlightthickness=0,command=self.remove_cart)
        self.remove_button.place(x=520, y=385, width=70.7, height=19.26)

        self.process_button = Button(image=self.image_refs['process'], borderwidth=0, highlightthickness=0,command=self.go_to_end_page)
        self.process_button.place(x=350, y=335, width=75.75, height=70.61)

        self.entry_bg_1 = self.canvas.create_image(520, 185, image=self.image_refs['textbox1'])
        self.entry_1 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=450, y=176.5, width=140, height=18.42)

        self.entry_bg_2 = self.canvas.create_image(520, 215, image=self.image_refs['textbox1'])
        self.entry_2 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=450, y=206.5, width=140, height=18.42)

        self.entry_bg_3 = self.canvas.create_image(520, 244, image=self.image_refs['textbox1'])
        self.entry_3 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=450, y=235.5, width=140, height=18.42)

        self.entry_bg_4 = self.canvas.create_image(520, 272, image=self.image_refs['textbox1'])
        self.entry_4 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=450, y=263, width=140, height=18.42)

        self.entry_bg_5 = self.canvas.create_image(560, 342, image=self.image_refs['textbox2'])
        self.entry_5 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=522, y=335, width=75, height=16.26)

        self.entry_bg_6 = self.canvas.create_image(560, 369, image=self.image_refs['textbox2'])
        self.entry_6 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=522, y=362, width=75, height=16.26)

        self.entry_bg_7 = self.canvas.create_image(520, 423, image=self.image_refs['textbox1'])
        self.entry_7 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_7.place(x=450, y=415, width=130, height=16.26)


                # Tạo Frame chứa bảng
        self.table_frame = tk.Frame(self.window, bg="#E1F2CE")
        self.table_frame.place(x=10, y=173)

        # Tạo Treeview (Bảng)
        self.columns = ("name", "checkin", "checkout", "quantity", "price")
        self.tree = ttk.Treeview(self.table_frame, columns=self.columns, show="headings", height=12)
        self.tree.pack()

        # Thiết lập tiêu đề cột
        self.tree.heading("name", text="Name")
        self.tree.heading("checkin", text="Check-in")
        self.tree.heading("checkout", text="Check-out")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")

        # Điều chỉnh độ rộng cột (tổng width = 250)
        self.tree.column("name", width=50)
        self.tree.column("checkin", width=65)
        self.tree.column("checkout", width=65)
        self.tree.column("quantity", width=70)
        self.tree.column("price", width=50)

        self.total = 0.0

        self.window.resizable(0, 0)
        self.window.update_idletasks()
        self.window.update()

    def add_to_cart(self):
        """Thêm dữ liệu vào giỏ hàng và hiển thị lên bảng."""
        name = self.entry_1.get()
        checkin = self.entry_2.get()
        checkout = self.entry_3.get()
        quantity = self.entry_4.get()
        price = self.entry_5.get()

        if name and checkin and checkout and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)
                total_price = quantity * price
                self.tree.insert("", "end", values=(name, checkin, checkout, quantity, price))
                self.total += total_price

                # Xóa nội dung các ô nhập liệu sau khi thêm thành công
                self.entry_1.delete(0, tk.END)
                self.entry_2.delete(0, tk.END)
                self.entry_3.delete(0, tk.END)
                self.entry_4.delete(0, tk.END)
                self.entry_5.delete(0, tk.END)

                messagebox.showinfo("Success", "Added to cart successfully!")
            except ValueError:
                messagebox.showwarning("Warning", "Quantity and Price must be numbers.")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def remove_cart(self):
        """Xóa toàn bộ dữ liệu đang nhập và làm trống bảng."""
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.entry_3.delete(0, tk.END)
        self.entry_4.delete(0, tk.END)
        self.entry_5.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        self.total = 0.0
        messagebox.showinfo("Info", "Cart has been cleared.")

    def go_to_signout_page(self):
        self.window.destroy()
        from Modules.Login.Login_View import Login_View
        app = Login_View()
        app.run()

    def go_to_end_page(self):
        """Chuyển đến trang kết thúc sau khi xử lý hóa đơn."""
        if self.tree.get_children():
            self.window.destroy()  # Đóng cửa sổ hiện tại
            subprocess.run(["python", "End.py", str(self.total)])  # Truyền tổng giá trị sang End.py
        else:
            messagebox.showwarning("Warning", "Cart is empty. Please add items to cart.")
    def go_to_landing_page(self):
        self.window.destroy()
        from Modules.User.User_Landing_View import User_Landing_View
        app = User_Landing_View()
        app.run()
    def go_to_main_view(self):
        self.window.destroy()
        from Modules.User.Component.User_Main_View import HotelBookingApp
        app = HotelBookingApp()
        app.run()
    def go_to_invoice_page(self):
        self.window.destroy()
        from Modules.User.Component.Booking_Hotels.End import Hotel_View
        app = Hotel_View()
        app.run()
    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    app = Invoice_View()
    app.run()