from tkinter import *

okToPressReturn = True

bomb = 100

day = 0

def start(event):
    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        start.config(text = "")
        updateBomb()
        updateDay()
        updateDisplay()

        okToPressReturn = False

def updateDisplay():
    global bomb
    global day
    if bomb<=50:
        bomb_normal.config(image = nophoto)
    else:
        bomb_normal.config(image = normalphoto)
    bombLabel.config(text="Фитиль: " +str(bomb))
    dayLabel.config(text="День: " + str(day))
    bomb_normal.after(100, updateDisplay)

def updateBomb():
    global bomb
    bomb -= 1
    if isAlive():
        bombLabel.after(500, updateBomb)

def updateDay():
    global day
    day +=1
    if isAlive():
        dayLabel.after(5000, updateDay)

def stop():
    global bomb
    if isAlive():
        if bomb <=79:
            bomb + 20
        else:
            bomb -= 20

def isAlive():
    global bomb
    if bomb<=0:
        startLabel.config(text = "БаБаХ!!!!")
        bomb_normal.config(image = bangphoto)
        return False
    else:
        return True


root = Tk()
root.title("Бомба")
root.geometry("500x500")

startLabel = Label(root, text="Нажми Enter, чтобы начать игру!", font = ("Helvetica", 12))
bombLabel =  Label(root, text = "Фитить: " +str(bomb), font = ("Helvetica", 12))
dayLabel = Label(root, text = "День: " + str(day), font = ("Helvetica", 12))

startLabel.pack()
bombLabel.pack()
dayLabel.pack()

nophoto = PhotoImage(file = "b2.gif")
normalphoto = PhotoImage(file = "b1.gif")
bangphoto = PhotoImage(file = "b3.gif")

bomb_normal = Label(root, image=normalphoto)

btn_no_bomb = Button(root, text = "Нажми меня", command=stop)

bomb_normal.pack()
btn_no_bomb.pack()

bang_photo = Label(root, image = bangphoto)
bang_photo.pack()

root.bind("<return>", start)

root.mainloop()
