import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path

# Giả sử bạn có module xử lý login riêng
# Nếu chưa có, bạn có thể comment lại phần import này
# import Modules.Login.Login_Process as lgp

class Login_View:
    def __init__(self):
        self.window = tk.Tk()

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.window_width = 693
        self.window_height = 496

        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        
        self.window.configure(bg="#FFFFFF")
        self.window.title("Landing Page")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"C:\DoAn\Image\User\LandingPage")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.booking_image = PhotoImage(file=assets_path / "Button_Bookingnow.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: ap.Admin_Process.log_out_button_handle(self))
        self.logout_button.place(x=462, y=85, width=130, height=40)

        self.bookingnow_button = Button(image=self.booking_image, borderwidth=0, highlightthickness=0)
        self.bookingnow_button.place(x=290 ,y=390 ,width=123, height=24.52)
                           
        self.window.resizable(0, 0)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Login_View()
    app.run()
