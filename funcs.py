from tkinter import messagebox
import tkinter as tk
import random as rn


def create_label(window, message, row=None, column=None):
    """ "Функція для створення тексту у вікні"""
    label = tk.Label(window, text=message)
    if row is None and column is None:
        label.pack()
        return
    label.grid(row=row, column=column)


def generateSet(value: tk.Entry, max_value: int) -> set:
    result = set()
    try:
        for _ in range(int(value.get())):
            result.add(rn.randint(0, max_value))
    except ValueError:
        messagebox.showerror("Помилка", message="Не задана потужність множини!")
    return result


def generateA(A: set, valueA: tk.Entry):
    try:
        A.clear()
        for _ in range(int(valueA.get())):
            A.add(rn.randint(0, 256))
    except ValueError:
        messagebox.showerror("Помилка", message="Не задана потужність множини А!")


def generateB(B: set, valueB: tk.Entry):
    try:
        B.clear()
        for _ in range(int(valueB.get())):
            B.add(rn.randint(0, 256))
    except ValueError:
        messagebox.showerror("Помилка", message="Не задана потужність множини B!")


def generateC(C: set, valueC: tk.Entry):
    try:
        C.clear()
        for i in range(int(valueC.get())):
            C.add(rn.randint(0, 256))
    except ValueError:
        messagebox.showerror("Помилка", message="Не задана потужність множини C!")


def getUWithBoundaries(lower: int, higher: int) -> set:
    if higher > lower:
        return set(i for i in range(lower, higher))
    else:
        messagebox.showerror("Помилка", message="Верхня межа менша за нижню")
        return set()


def extractSetFromEntry(entry: tk.Entry) -> set:
    A_str = list(entry.get().split())
    return set(int(element) for element in A_str)


def step(window: tk.Tk, inA: set, inB: set, inC: set, inU: set):
    nott = lambda A: inU - A

    if not hasattr(window, "step_counter"):
        window.step_counter = 1
    else:
        window.step_counter += 1

    if window.step_counter == 1:
        temporary_result = nott(inA).union(inB)
        Label5 = tk.Label(window, text=f"A̅ ∪ B = {temporary_result}")
        Label5.pack()
    elif window.step_counter == 2:
        temporary_result = nott(inA).union(inB).union(nott(inC))
        Label6 = tk.Label(window, text=f"A̅ ∪ B ∪ C̅ = {temporary_result}")
        Label6.pack()
    elif window.step_counter == 3:
        temporary_result = (
            nott(inA).union(inB).union(nott(inC)).union(inB.intersection(nott(inC)))
        )
        Label7 = tk.Label(
            window, text=f"D = A̅ ∪ B ∪ C̅ ∪ (B ∩ C̅) = {temporary_result}"
        )
        Label7.pack()
    elif window.step_counter == 4:
        temporary_result = (
            nott(inA)
            .union(inB)
            .union(nott(inC))
            .union(inB.intersection(nott(inC)))
            .union(inC.intersection(nott(inA)))
        )
        Label8 = tk.Label(
            window, text=f"D = A̅ ∪ B ∪ C̅ ∪ (B ∩ C̅)∪ (A̅ ∩ C) = {temporary_result}"
        )
        Label8.pack()
    elif window.step_counter == 5:
        temporary_result = (
            nott(inA)
            .union(inB)
            .union(nott(inC))
            .union(inB.intersection(nott(inC)))
            .union(inC.intersection(nott(inA)))
            .union(inA.intersection(inB))
        )
        Label9 = tk.Label(
            window,
            text=f"D = A̅ ∪ B ∪ C̅ ∪ (B ∩ C̅) ∪ (A̅ ∩ C) ∪ (A ∩ B) = {temporary_result}",
        )
        Label9.pack()


def stepResult(inA: set, inB: set, inC: set, inU: set):
    nott = lambda A: inU - A
    temporary_result = nott(inA).union(inB)
    temporary_result = temporary_result.union(nott(inC))
    temporary_result = temporary_result.union(inB.intersection(nott(inC)))
    temporary_result = temporary_result.union(inC.intersection(nott(inA)))
    temporary_result = temporary_result.union(inA.intersection(inB))

    return temporary_result


def saveD(D: set, file):
    with open(file, "w+") as f:
        f.write(str(D))


def step2(window: tk.Tk, inA: set, inB: set, inC: set, inU: set):
    nott = lambda A: inU - A

    result = nott(inA).union(inB.union(nott(inC)))
    temporary_result = nott(inA).union(inB)
    Label5 = tk.Label(window, text=f"A̅ ∪ B = {temporary_result}")
    Label5.pack()

    temporary_result = nott(inC).union(temporary_result)
    Label6 = tk.Label(window, text=f"A̅ ∪ B ∪ C̅ = {temporary_result}")
    Label6.pack()


def symmetric_difference(A, B, inU):
    nott = lambda A: inU - A
    X = nott(A)
    Y = nott(B)

    result = set()

    for element in X:
        if element not in Y:
            result.add(element)

    for element in Y:
        if element not in X:
            result.add(element)

    return result
