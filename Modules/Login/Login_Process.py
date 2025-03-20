from tkinter import messagebox
import tkinter as tk
import Api.Login_Api as Login_Api
import Modules.Admin.Landing_View as av
import Modules.User.User_Landing_View as uv
import Modules.Signup.Signup_View as suv

class Login_Process:
    @staticmethod
    def confirm_button_handle(obj):
        username = obj.entry_username.get()
        password = obj.entry_password.get()
        api = Login_Api.Login_Api()

        try:
            success = api.check_user_login(username, password)
            if success == -1:
                messagebox.showerror("Warning", "Invalid User Input")
                obj.entry_username.delete(0, tk.END)
                obj.entry_password.delete(0, tk.END)
            elif success == -2:
                messagebox.showerror("Warning", "User not found")
                obj.entry_username.delete(0, tk.END)
                obj.entry_password.delete(0, tk.END)
            elif success == -3:
                messagebox.showerror("Warning", "Wrong password")
                obj.entry_password.delete(0, tk.END)
            else:
                if success == "Admin":
                    messagebox.showinfo("MB", "Welcome Admin")
                    obj.window.destroy()
                    app = av.Admin_View()
                    app.window.mainloop()
                elif success == "User":
                    messagebox.showinfo("MB", "Welcome User")
                    obj.window.destroy()
                    app = uv.User_Landing_View()
                    app.window.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {e}")

    @staticmethod
    def signup_button_handle(self):
        self.window.destroy()
        app = suv.Signup_View()
        app.window.mainloop()
