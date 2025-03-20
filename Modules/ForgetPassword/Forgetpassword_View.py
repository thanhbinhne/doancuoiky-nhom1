import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button, messagebox
from pathlib import Path
from Modules.ForgetPassword.Forgetpassword_Process import Forgetpassword_Process

class ForgetPassword_View:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Forget Password")
        self.window.geometry("700x500")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path("D:/uel_form-master/Image/ForgetPassword")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.reset_pw_image = PhotoImage(file=assets_path / "Button_Resetpassword.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.login_image = PhotoImage(file=assets_path / "Button_Login.png")
        self.signup_image = PhotoImage(file=assets_path / "Button_Signup.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.entry_bg_1 = self.canvas.create_image(360, 150, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=256, y=131, width=207, height=39)

        self.entry_bg_2 = self.canvas.create_image(360, 218, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=256, y=199, width=207, height=39)

        self.entry_bg_3 = self.canvas.create_image(360, 286, image=self.entry_image)
        self.entry_3 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=256, y=267, width=207, height=39)

        self.entry_bg_4 = self.canvas.create_image(360, 356, image=self.entry_image)
        self.entry_4 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=256, y=337, width=207, height=39)

        self.login_button = Button(image=self.login_image, borderwidth=0, highlightthickness=0, command=lambda: Forgetpassword_Process.go_to_login(self.window))
        self.login_button.place(x=532, y=25, width=129.5, height=39.5)

        self.signup_button = Button(image=self.signup_image, borderwidth=0, highlightthickness=0,command=lambda: Forgetpassword_Process.go_to_signup(self.window))
        self.signup_button.place(x=529.3, y=73, width=133.5, height=47)

        self.reset_ps_button = Button(image=self.reset_pw_image, borderwidth=0, highlightthickness=0, command=self.reset_password)
        self.reset_ps_button.place(x=273, y=400, width=174, height=39)

        self.window.resizable(0, 0)

    def reset_password(self):
        username = self.entry_1.get()
        phone_number = self.entry_2.get()
        new_password = self.entry_3.get()
        re_new_password = self.entry_4.get()

        Forgetpassword_Process.reset_password(username, phone_number, new_password, re_new_password, self.window)


if __name__ == "__main__":
    app = ForgetPassword_View()
    app.window.mainloop()
