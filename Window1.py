import tkinter as tk
from tkinter import messagebox
import random as rn
from funcs import *

A = set()
B = set()
C = set()
U = set(i for i in range(256))  # універсальна множина


def Window1(A, B, C, U):
    
    G = 22  # номер групи
    N = 31  # номер у групі

    Window1 = tk.Tk()
    Window1.title("Головне меню")
    Window1.geometry(f"800x600")
    name = tk.Label(Window1, text=f"ПІБ: Шинкар Максим \n"
                                f"Олександрович\n "
                                f"Група: ІО-{G}\n "
                                f"Мій варіант: {(N + G % 60) % 30 + 1}",
                    font=("Times New Roman", 14))
    name.grid(row=0, column=0)

    def onWindow2():
        window2(A,B,C,U)
    def onWindow3():
        window3(A,B,C,U)
    def onWindow4():
        window4(A,B,C,U)
    def onWindow5():
        window5(A,B,C,U)   
    


    window2Call = tk.Button(Window1, text="Виклик вікна №2", command=onWindow2)   
    window2Call.grid(row=0, column=1)
    window3Call = tk.Button(Window1, text="Виклик вікна №3", command=onWindow3)
    window3Call.grid(row=0, column=2)
    window4Call = tk.Button(Window1, text="Виклик вікна №4", command=onWindow4)
    window4Call.grid(row=0, column=3)
    window5Call = tk.Button(Window1, text="Виклик вікна №5", command=onWindow5)
    window5Call.grid(row=0, column=4)



    valueA = tk.Entry(Window1)
    valueA.grid(row=3, column=2)
    valueB = tk.Entry(Window1)
    valueB.grid(row=3, column=3)
    valueC = tk.Entry(Window1)
    valueC.grid(row=3, column=4)

    create_label(Window1, "Введіть потужність A:", row=2, column=2)
    create_label(Window1, "Введіть потужність B:", row=2, column=3)
    create_label(Window1, "Введіть потужність C:", row=2, column=4)


    def onGenerateA():
        generateA(A, valueA)

    def onGenerateB():
        generateB(B, valueB)
    
    def onGenerateC():
        generateC(C, valueC)

    generateA_btn = tk.Button(Window1, text="Згенерувати A",
                            command=onGenerateA)
    generateA_btn.grid(row=4, column=2)

    generateB_btn = tk.Button(Window1, text="Згенерувати B",
                            command=onGenerateB)
    generateB_btn.grid(row=4, column=3)

    generateC_btn = tk.Button(Window1, text="Згенерувати C",
                            command=onGenerateC)
    generateC_btn.grid(row=4, column=4)

    entryA = tk.Entry(Window1)
    entryA.grid(row=5, column=2)
    entryB = tk.Entry(Window1)
    entryB.grid(row=5, column=3)
    entryC = tk.Entry(Window1)
    entryC.grid(row=5, column=4)

    def onSaveA():
        saveA(A, entryA)
    
    def onSaveB():
        saveB(B, entryB)

    def onSaveC():
        saveC(C, entryC)


    saveA_btn = tk.Button(Window1, text="Зберегти A", command=onSaveA)
    saveA_btn.grid(row=6, column=2)
    saveB_btn = tk.Button(Window1, text="Зберегти B", command=onSaveB)
    saveB_btn.grid(row=6, column=3)
    saveC_btn = tk.Button(Window1, text="Зберегти C", command=onSaveC)
    saveC_btn.grid(row=6, column=4)

    create_label(Window1, "Нижня межа", row=7, column=2)
    create_label(Window1, "Верхня межа", row=7, column=3)

    # введення діапазону універсальної множини
    entry_lower_boundary = tk.Entry(Window1)
    entry_lower_boundary.grid(row=8, column=2)
    # place(x=350, y=250)

    entry_higher_boundary = tk.Entry(Window1)
    entry_higher_boundary.grid(row=8, column=3)
    # place(x=500, y=250)

    def OnSetU():
        higher_boundary = int(entry_higher_boundary.get()) if (entry_higher_boundary.get() != '') else 255
        lower_boundary = int(entry_lower_boundary.get()) if (entry_lower_boundary.get() != '') else 0
        U = getUWithBoundaries(lower_boundary, higher_boundary)


    saveU = tk.Button(Window1, text="Встановити границі", command=OnSetU)
    saveU.grid(row=9, column=2)


    Window1.mainloop()



def window2(A, B, C, U):
    Window2 = tk.Tk()
    Window2.geometry(f"300x300")
    Window2.title("Вікно2")
    Label1 = tk.Label(Window2, text="A="+str(A)) 
    Label1.pack()  #grid(column=1,row=1)
    Label2 = tk.Label(Window2, text="B="+str(B))
    Label2.pack() #grid(column=1,row=2)
    Label3 = tk.Label(Window2, text="C="+str(C))
    Label3.pack() #grid(column=1,row=3)
    Label4 = tk.Label(Window2,text= "D = A̅ ∪ B ∪ C̅ ∪ (B ∩ C̅) ∪ (A̅ ∩ C) ∪ (A ∩ B)")
    Label4.pack() #grid(column=1,row=4)

    def onStep():
        step(Window2,A, B, C, U)

    StepButton = tk.Button(Window2, text="Крок", command=onStep)
    StepButton.pack(side=tk.TOP)


    D = stepResult(A, B, C, U)
    def onSave():
        saveD(D, "D.txt")

    SaveButton = tk.Button(Window2, text="Зберегти результат", command=onSave)
    SaveButton.pack(side=tk.BOTTOM)

    Window2.mainloop()
    
def window3(A, B, C, U):
    Window3 = tk.Tk()
    Window3.geometry(f"300x300")
    Window3.title("Вікно3")
    Label1 = tk.Label(Window3, text="A="+str(A))
    Label1.pack()  #grid(column=1,row=1)
    Label2 = tk.Label(Window3, text="B="+str(B))
    Label2.pack() #grid(column=1,row=2)
    Label3 = tk.Label(Window3, text="C="+str(C))
    Label3.pack() #grid(column=1,row=3)
    Label4 = tk.Label(Window3,text= "D = A̅ ∪ B ∪ C̅ ")
    Label4.pack() #grid(column=1,row=4)

    def onStep():
        step(Window3,A, B, C, U)

    StepButton = tk.Button(Window3, text="Крок", command=onStep)
    StepButton.pack(side=tk.TOP)


    D = stepResult(A, B, C, U)
    def onSave():
        saveD(D, "D2.txt")

    SaveButton = tk.Button(Window3, text="Зберегти результат", command=onSave)
    SaveButton.pack(side=tk.BOTTOM)

    Window3.mainloop()


def window4(A, B, C, U):
    def nott(inA, inU):
        return inU - inA

    Window4 = tk.Tk()
    Window4.geometry(f"300x300")
    Window4.title("Вікно4")

    x = nott(A, U)
    y = nott(B, U)
    z = symmetric_difference(A, B, U)

    Label1 = tk.Label(Window4, text="X=" + str(x))
    Label1.pack()

    Label2 = tk.Label(Window4, text="Y=" + str(y))
    Label2.pack()

    Label3 = tk.Label(Window4, text="Z=" + str(z))
    Label3.pack()

    Window4.mainloop()
def window5():
    pass

Window1(A,B,C,U)