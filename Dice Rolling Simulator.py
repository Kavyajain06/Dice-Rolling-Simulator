import tkinter
from PIL import Image, ImageTk
import random
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the dice')
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()
# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Let's play",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()
# images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
# packing a widget in the parent widget 
ImageLabel.pack( expand=True)
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)
root.mainloop()
