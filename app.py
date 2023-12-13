import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.XSIZE, self.YSIZE = 800, 800
    
    def Button(self, x, y, h = None, w = None, type= None, text=None, textures = None):
        if text != None:
            if h != None and w != None:
                if type != None:
                    x1=tk.Button(root, text=text)
                    if textures != None:
                        photo=tk.PhotoImage(file="textures/" + textures + ".png")
                        x1.config(image=photo,width=w,height=h)
                    else: 
                        x1.config(width=w,height=h)
                    x1.config(command=lambda :self.action(type))
                    x1.place(x=x, y=y)
                    x1.pack()
           
        
    def action(self,type):
        if type == "exit":
            root.destroy()
    def render(self):
        bg = tk.PhotoImage(file = "textures/background.png")
        label1 = tk.Label( root, image = bg) 
        label1.place(x = -2, y = 0) 
        print("Render good")
        myapp.master.title("Bataille")
        root.geometry(str(self.XSIZE)+"x"+str(self.YSIZE)) 
        myapp.master.maxsize(self.XSIZE, self.YSIZE)
        self.Button(30,30, 100, 100, "exit", "Ceci est un bouton")
        myapp.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(root)
    myapp.render()
    
    