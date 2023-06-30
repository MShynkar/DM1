import tkinter as tk
from tkinter import messagebox
import random as rn
from funcs import *


class Solution:
    A: set = set()
    B: set = set()
    C: set = set()
    U: set = set(i for i in range(256))
    X: set = set()
    Y: set = set()


def Window1(s: Solution):
    G = 22  # номер групи
    N = 31  # номер у групі

    Window1 = tk.Tk()
    Window1.title("Головне меню")
    Window1.geometry(f"800x600")
    name = tk.Label(
        Window1,
        text=f"ПІБ: Шинкар Максим \n"
        f"Олександрович\n "
        f"Група: ІО-{G}\n "
        f"Мій варіант: {(N + G % 60) % 30 + 1}",
        font=("Times New Roman", 14),
    )
    name.grid(row=0, column=0)

    def onWindow2():
        window2(s)

    def onWindow3():
        window3(s)


    def onWindow4():
        window4(s)

    def onWindow5():
        window5(s)

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
        s.A = generateSet(valueA, max(s.U), min(s.U))

    def onGenerateB():
        s.B = generateSet(valueB, max(s.U),min(s.U))

    def onGenerateC():
        s.C = generateSet(valueC, max(s.U), min(s.U))

    generateA_btn = tk.Button(Window1, text="Згенерувати A", command=onGenerateA)
    generateA_btn.grid(row=4, column=2)

    generateB_btn = tk.Button(Window1, text="Згенерувати B", command=onGenerateB)
    generateB_btn.grid(row=4, column=3)

    generateC_btn = tk.Button(Window1, text="Згенерувати C", command=onGenerateC)
    generateC_btn.grid(row=4, column=4)

    entryA = tk.Entry(Window1)
    entryA.grid(row=5, column=2)
    entryB = tk.Entry(Window1)
    entryB.grid(row=5, column=3)
    entryC = tk.Entry(Window1)
    entryC.grid(row=5, column=4)

    def onSaveA():
        s.A = extractSetFromEntry(entryA)

    def onSaveB():
        s.B = extractSetFromEntry(entryB)

    def onSaveC():
        s.C = extractSetFromEntry(entryC)

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
        higher_boundary = (
            int(entry_higher_boundary.get())
            if (entry_higher_boundary.get() != "")
            else 255
        )
        lower_boundary = (
            int(entry_lower_boundary.get())
            if (entry_lower_boundary.get() != "") else 0
        )
        s.U = getUWithBoundaries(lower_boundary, higher_boundary)

    saveU = tk.Button(Window1, text="Встановити границі", command=OnSetU)
    saveU.grid(row=9, column=2)

    Window1.mainloop()


def window2(p: Solution):
    Window2 = tk.Tk()
    Window2.geometry(f"300x300")
    Window2.title("Вікно2")
    Label1 = tk.Label(Window2, text="A=" + str(p.A))
    Label1.pack()  # grid(column=1,row=1)
    Label2 = tk.Label(Window2, text="B=" + str(p.B))
    Label2.pack()  # grid(column=1,row=2)
    Label3 = tk.Label(Window2, text="C=" + str(p.C))
    Label3.pack()  # grid(column=1,row=3)
    Label4 = tk.Label(Window2, text="D = A̅ ∪ B ∪ C̅ ∪ (B ∩ C̅) ∪ (A̅ ∩ C) ∪ (A ∩ B)")
    Label4.pack()  # grid(column=1,row=4)

    def onStep():
        step(Window2, p.A, p.B, p.C, p.U)

    StepButton = tk.Button(Window2, text="Крок", command=onStep)
    StepButton.pack(side=tk.TOP)

    D = stepResult(p.A, p.B, p.C, p.U)

    def onSave():
        save(D, "D.txt")

    SaveButton = tk.Button(Window2, text="Зберегти результат", command=onSave)
    SaveButton.pack(side=tk.BOTTOM)

    Window2.mainloop()


def window3(s: Solution):
    Window3 = tk.Tk()
    Window3.geometry(f"300x300")
    Window3.title("Вікно3")
    Label1 = tk.Label(Window3, text="A=" + str(s.A))
    Label1.pack()  # grid(column=1,row=1)
    Label2 = tk.Label(Window3, text="B=" + str(s.B))
    Label2.pack()  # grid(column=1,row=2)
    Label3 = tk.Label(Window3, text="C=" + str(s.C))
    Label3.pack()  # grid(column=1,row=3)
    Label4 = tk.Label(Window3, text="D = A̅ ∪ B ∪ C̅ ")
    Label4.pack()  # grid(column=1,row=4)

    def onStep():
        step2(Window3, s.A, s.B, s.C, s.U)

    StepButton = tk.Button(Window3, text="Крок", command=onStep)
    StepButton.pack(side=tk.TOP)

    D2 = step2Result(s.A, s.B, s.C, s.U)

    def onSave():
        save(D2, "D2.txt")

    SaveButton = tk.Button(Window3, text="Зберегти результат", command=onSave)
    SaveButton.pack(side=tk.BOTTOM)

    Window3.mainloop()


def window4(s: Solution):
    Window4 = tk.Tk()
    Window4.geometry(f"300x300")
    Window4.title("Вікно4")

    s.X = s.U - s.A
    s.Y = s.U - s.B
    Label1 = tk.Label(Window4, text="X=" + str(s.X))
    Label1.pack()

    Label2 = tk.Label(Window4, text="Y=" + str(s.Y))
    Label2.pack()

    Z = symmetricDifference(s.X, s.Y)
    Z2 = (s.X).symmetric_difference(s.Y)

    Label3 = tk.Label(Window4, text="Z=" + str(Z))
    Label3.pack()

    def onSave():
        save(Z, "Z.txt")
        save(Z2, "Z2.txt")

    saveResults = tk.Button(Window4, text="Зберегти Z", command=onSave)
    saveResults.pack(side=tk.BOTTOM)


    Window4.mainloop()


def window5(s: Solution):
    Window5 = tk.Tk()
    Window5.geometry(f"400x400")
    Window5.title("Вікно5")

    def onReadD():
        D = read("D.txt")
        LabelD1 = tk.Label(Window5, text=f"D = A̅ ∪ B ∪ C̅ ∪ (B ∩ C̅) ∪ (A̅ ∩ C) ∪ (A ∩ B) = {D}")
        LabelD1.grid(row=0, column=1)

    readD = tk.Button(Window5, text="Зчитати D\n розраховану повним виразом", command=onReadD)
    readD.grid(row=1, column=0)

    def onReadD2():
        D = read("D2.txt")
        LabelD1 = tk.Label(Window5, text=f"D = A̅ ∪ B ∪ C̅ = {D}")
        LabelD1.grid(row=1, column=1)

    readD2 = tk.Button(Window5, text="Зчитати D\n розраховану спрощеним виразом", command=onReadD2)
    readD2.grid(row=2, column=0)

    def onReadZ():
        Z = read("Z.txt")
        LabelD1 = tk.Label(Window5, text=f"Z = X/Y = {Z}")
        LabelD1.grid(row=2, column=1)

    readZ = tk.Button(Window5, text="Зчитати Z\n розраховану власною функцією", command=onReadZ)
    readZ.grid(row=3, column=0)

    def onReadZ2():
        Z2 = read("Z2.txt")
        LabelD1 = tk.Label(Window5, text=f"Z = X/Y = {Z2}")
        LabelD1.grid(row=3, column=1)

    readZ2 = tk.Button(Window5, text="Зчитати Z\n розраховану вбудованою функцією", command=onReadZ2)
    readZ2.grid(row=4, column=0)

    def onCompareD():
        equals = compare("D.txt", "D2.txt")
        if equals:
            LabelD1 = tk.Label(Window5, text="Так, множини співпадають")
            LabelD1.grid(row=6, column=1)
        else:
            LabelD1 = tk.Label(Window5, text="Ні, множини не співпадають")
            LabelD1.grid(row=6, column=1)

    compare1 = tk.Button(Window5, text="Порівняти множини розрахунки D", command=onCompareD)
    compare1.grid(row=5, column=1)

    def onCompareZ():
        equals = compare("Z.txt", "Z2.txt")
        if equals:
            LabelD1 = tk.Label(Window5, text="Так, множини співпадають")
            LabelD1.grid(row=6, column=2)
        else:
            LabelD1 = tk.Label(Window5, text="Ні, множини не співпадають")
            LabelD1.grid(row=6, column=2)

    compare2 = tk.Button(Window5, text="Порівняти множини розрахунки Z", command=onCompareZ)
    compare2.grid(row=5, column=2)

    Window5.mainloop()
