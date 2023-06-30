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


def generateSet(value: tk.Entry, max_value: int, min_value: int) -> set:
    result = set()
    try:
        count = int(value.get())
        while len(result) < count:
            result.add(rn.randint(min_value, max_value))
    except ValueError:
        messagebox.showerror("Помилка", message="Не задана потужність множини!")
    return result



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


def save(D: set, file: str):
    with open(file, "w+") as f:
        f.write(str(D))


def step2(window: tk.Tk, inA: set, inB: set, inC: set, inU: set):
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

def step2Result(inA: set, inB: set, inC: set, inU: set):
    nott = lambda A: inU - A
    result = (nott(inA).union(inB)).union(nott(inC))
    return result

def symmetricDifference(inX: set, inY:set):
    result = set()

    for element in inX:
        if element not in inY:
            result.add(element)

    for element in inY:
        if element not in inX:
            result.add(element)

    return result

def read(file):
    with open(file, "r+") as f:
        content = f.read()
        
    return content

def compare(file1: str,file2:str ):
    content1 = read(file1)
    content2 = read(file2)
    if content1 == content2:
        return True
    return False