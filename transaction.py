import tkinter as tk
root = tk.Tk()
root.title("Window")
root.title('Counting seconds')
button = tk.Button(root, text='Stop the application', width=25, command=root.destroy)
button.pack()
root.mainloop()