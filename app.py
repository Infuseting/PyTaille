import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
    def render(self):
        bg = tk.PhotoImage(file = "textures/background.png")
        label1 = tk.Label( root, image = bg) 
        label1.place(x = -2, y = 0) 
        print("Render good")
        myapp.master.title("Bataille")
        root.geometry("800x800") 
        myapp.master.maxsize(800, 800)
        myapp.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(root)
    myapp.render()
    
    