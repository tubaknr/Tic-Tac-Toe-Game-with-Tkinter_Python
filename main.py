from tkinter import *
import settings
import ctypes

root = Tk()
root.title("TicTacToe Game")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)



center_frame = Frame(root, bg="red",
                    width=settings.WIDTH*0.50,
                    height = settings.HEIGHT*0.50)

center_frame.place(x=settings.WIDTH*0.25,
                    y = settings.HEIGHT*0.25)



class ButtonClass:
    buttons = []
    def __init__(self, width, height, text, x, y):
        self.width = width
        self.height = height 
        self.text = " " 
        self.btn_obj = None
        self.x = x
        self.y = y
        ButtonClass.buttons.append(self)
        self.clicked = False

    def create_button(self,location):
        btn = Button(location,
                    width = self.width, 
                    height = self.height,
                    text = self.text)
        
        btn.bind('<Button-1>',self.left_click) #left click of mouse=<Button-1>
        self.btn_obj = btn



    def left_click(self, event):
        if self.clicked==True:
            print("Already clicked. Choose another one.")

        #human's turn: X
        if not (who_win(ButtonClass.buttons, "X")) and not (who_win(ButtonClass.buttons, "O")):
            if self.clicked == False:
                self.btn_obj.configure(text="X")
                self.btn_obj.configure(bg="SystemButtonFace")
                self.clicked = True
                self.text = "X"
                print(f"You clicked {self.text} to: {self.x},{self.y}")
                if (who_win(ButtonClass.buttons, "X")):
                    print("Human wins!")
                    ctypes.windll.user32.MessageBoxW(0, "Congratulations! Human won!")

                elif (who_win(ButtonClass.buttons, "O")):
                    print("Computer wins!")
                    ctypes.windll.user32.MessageBoxW(0, "Congratulations! Computer won!")
            
                #computer's turn: O
                if not (who_win(ButtonClass.buttons, "X")) and not (who_win(ButtonClass.buttons, "O")):
                    for button in ButtonClass.buttons:
                        
                        if button==self or button.clicked==True:
                            continue

                                                                  
                        button.btn_obj.configure(text="O")
                        button.btn_obj.configure(bg="SystemButtonFace")
                        button.clicked = True
                        button.text = "O"
                        print(f"Computer clicked {button.text} to: {button.x},{button.y}")
                        break

                    if (who_win(ButtonClass.buttons, "X")):
                        print("Human wins!")
                        ctypes.windll.user32.MessageBoxW(0, "Congratulations! Human won!")

                    elif (who_win(ButtonClass.buttons, "O")):
                        print("Computer wins!")
                        ctypes.windll.user32.MessageBoxW(0, "Congratulations! Computer won!")



def who_win(btn,a):
    return ((btn[0].text==btn[1].text==btn[2].text==a) or 
        (btn[3].text==btn[4].text==btn[5].text==a) or 
        (btn[6].text==btn[7].text==btn[8].text==a) or 
        (btn[0].text==btn[3].text==btn[6].text==a) or 
        (btn[1].text==btn[4].text==btn[7].text==a) or 
        (btn[2].text==btn[5].text==btn[8].text==a) or
        (btn[0].text==btn[4].text==btn[8].text==a) or
        (btn[2].text==btn[4].text==btn[6].text==a))

    
#board
for i in range(settings.n_row):
    for j in range(settings.n_col):
        btn = ButtonClass(6, 6, " ", x=i, y=j)
        btn.create_button(center_frame)
        btn.btn_obj.grid(column=j, row=i)
    

root.mainloop()


