import tkinter as tk
root = tk.Tk()
root.title("CLOUD OPS")
root.geometry("300x100")
root.configure(bg="pink")
l_2=tk.Label(root,text="Person Not Registered For Event !!",font=("times new roman",15),fg="red",bg='pink').place(x=10,y=10)
exit_file_button = tk.Button(root,text="OK",font=("times new roman",12),fg="yellow",bg="blue",command=root.destroy).place(x=115,y=50)
root.mainloop()
