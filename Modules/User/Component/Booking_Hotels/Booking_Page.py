import tkinter as tk
from tkinter import Canvas, PhotoImage, Button
from pathlib import Path
from tkinter import ttk
import importlib

# from Modules.User.Component.Booking_Hotels.Invoice import Invoice_View


class Hotel_View:
    def __init__(self):

        self.window = tk.Tk()
        # self.window = tk.Toplevel(parent_window) if parent_window else tk.Tk()

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

        assets_path = Path(r"D:\uel_form-master\Image\User\Room2")
        self.image_refs = {}

        try:
            self.image_refs['background'] = PhotoImage(file=assets_path / "Background.png")
            self.image_refs['account'] = PhotoImage(file=assets_path / "Button_Account.png")
            self.image_refs['homepage'] = PhotoImage(file=assets_path / "Button_HomePage.png")
            self.image_refs['logout'] = PhotoImage(file=assets_path / "Button_Logout.png")
            self.image_refs['update'] = PhotoImage(file=assets_path / "Button_Update.png")
        except Exception as e:
            print(f"Lỗi tải hình ảnh: {e}")


        self.background = self.canvas.create_image(342.0, 246.0, image=self.image_refs.get('background'))
        self.account_button = Button(self.window, image=self.image_refs.get('account'), borderwidth=0,
                                     highlightthickness=0)
        self.account_button.place(x=76, y=16, width=39, height=39)

        self.update_button = Button(self.window, image=self.image_refs.get('update'), borderwidth=0,
                                    highlightthickness=0, relief="flat", command=self.go_to_invoice)
        self.update_button.place(x=570, y=457, width=97.8, height=24.6)

        self.homepage_button = Button(self.window, image=self.image_refs.get('homepage'), borderwidth=0,
                                      highlightthickness=0, command=self.go_to_homepage)
        self.homepage_button.place(x=37.3, y=70.1, width=130.4, height=32.8)

        self.logout_button = Button(self.window, image=self.image_refs.get('logout'), borderwidth=0,
                                    highlightthickness=0, command=self.go_to_login)
        self.logout_button.place(x=563, y=26, width=103.28, height=32.8)

        # self.background_img = PhotoImage(file=assets_path / "Background.png")
        # self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        # self.homepage_image = PhotoImage(file=assets_path / "Button_HomePage.png")
        # self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        # self.update_image = PhotoImage(file=assets_path / "Button_Update.png")



        self.title_label = tk.Label(self.window, text="Price List", font=("Inter", 16, "bold"), bg="#FFFFFF")
        self.title_label.place(x=25, y=150, width=642, height=60)

        self.table_frame = tk.Frame(self.window, bg="#D9E7C5", width=642, height=230)
        self.table_frame.place(x=25, y=210)

        self.tree = ttk.Treeview(self.table_frame, columns=("Room Number", "Price", "Description"), show="headings")
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Description", text="Description")

        self.tree.column("Room Number", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Description", width=442, anchor="w")

        self.tree.place(x=0, y=0, width=642, height=230)
        self.window.update_idletasks()
    def go_to_homepage(self):
        self.window.destroy()
        User_Landing_View = importlib.import_module("Modules.User.User_Landing_View").User_Landing_View
        User_Landing_View()
    def go_to_login(self):
        self.window.destroy()
        Login_View = importlib.import_module("Modules.Login.Login_View").Login_View
        Login_View()
    def go_to_invoice(self):

        self.window.destroy()
        from Modules.User.Component.Booking_Hotels.Invoice import Invoice_View
        app = Invoice_View()
        app.run()
    def run(self):
            self.window.mainloop()
# Chạy ứng dụng
if __name__ == "__main__":
    # root = tk.Tk()
    app = Hotel_View()
    app.run()