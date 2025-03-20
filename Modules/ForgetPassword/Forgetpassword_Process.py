from tkinter import messagebox
from Api.ForgetPassword_Api import ForgetPassword_Api
import tkinter as tk
import importlib  # Import động để tránh lỗi vòng lặp




class Forgetpassword_Process:
    @staticmethod
    def reset_password(username, phone_number, new_password, re_new_password, window):
        api = ForgetPassword_Api()
        result, status = api.reset_password(username, phone_number, new_password, re_new_password)

        if status == 200:
            messagebox.showinfo("Success", "Password reset successful! Returning to login.")
            Forgetpassword_Process.go_to_login(window)
        else:
            messagebox.showerror("Error", result["error"])

    @staticmethod
    def go_to_login(window):
        window.destroy()

        try:
            Login_View = importlib.import_module("Modules.Login.Login_View").Login_View
            app = Login_View()


        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Login View: {e}")

    @staticmethod
    def go_to_signup(window):
        window.destroy()
        try:
            Signup_View = importlib.import_module("Modules.Signup.Signup_View").Signup_View
            app = Signup_View()  # Gọi đúng class


        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Signup View: {e}")

