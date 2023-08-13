from tkinter import *

# Создаем окно
root = Tk()
root.title("Мое окно")
root.geometry("400x600") # размер окна

# Задний фон
background = "#FFFFFF" # белый цвет
root.configure(bg=background)

# Картинка 1
image1 = PhotoImage(file="Image.png")
label1 = Label(root, image=image1, bg=background)
label1.place(relx=0.5, rely=0.3, anchor=CENTER) # размещаем по центру

# Текст
text = "Привет, мир!"
label2 = Label(root, text=text, font=("Arial", 24), bg=background)
label2.place(relx=0.5, rely=0.5, anchor=CENTER) # размещаем по центру

# Картинка 2
image2 = PhotoImage(file="Imageq.png")
label3 = Label(root, image=image2, bg=background)
label3.place(relx=0.5, rely=0.7, anchor=CENTER) # размещаем по центру

root.mainloop()