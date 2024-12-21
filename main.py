from tkinter import *
from random import randint

root = Tk()
root.title("Catch the ball!")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="black")

root.bind("<Alt_L>", lambda e: "break")
root.bind("<Alt_R>", lambda e: "break")
root.bind("<FocusOut>", lambda e: root.focus_force())

catch = Frame(root, width=74, height=15, bg="white")
catch.place(y=325, x=175); catch.propagate(False)
root.bind("<Motion>", lambda e: catch.place_configure(x=e.x-catch.cget("width")/2, y=325))

Frame(catch, bg="#666", width=55).pack(expand=True, fill=Y)

time_to_catch = 0.0062
caught = 0
speed = 1

def new_ball():
    global time_to_catch, caught, speed
    
    ball = Frame(root, width=24, height=24, bg="red")
    ball.place(x=randint(0, 470), y=0)
    
    def move_ball(n=0):
        global caught, time_to_catch, speed
        
        if n >= 390 - 24:
            ball.place_forget()
            ball.destroy()
            
            root.unbind("<Motion>")
            for x in root.winfo_children():
                x.destroy()
            Label(root, text="You lose!", font=("TkDefaultFont", 25, "bold"), bg="black", fg="white").pack(expand=True)
            root.after(2500, root.quit)
            return
        
        ball.place_configure(y=n + speed)
        
        ball_x = int(ball.place_info().get("x"))
        ball_y = int(ball.place_info().get("y"))
        catch_x = int(catch.place_info().get("x"))
        catch_y = int(catch.place_info().get("y"))
        
        if catch_y == ball_y + 24 and catch_x <= ball_x <= catch_x + catch.cget("width"):
            ball.place_forget()
            ball.destroy()
            caught += 1
            root.title(f"Catch the ball! Points: {caught}")
            
            if caught % 4 == 0: speed *= 2
            new_ball()
            return
        
        root.after(int(max(time_to_catch, 0.0015) * 1000), move_ball, n + 1)
    
    move_ball()

new_ball()

root.mainloop()
