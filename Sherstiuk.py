import tkinter as tk
from tkinter import messagebox
import random

# Змінні
G = 22
N = 30
A = []
B = []
C = []
Z = []
Z2 = []
D_long = []
D_short = []
AandB = []
AandnotB = []
notAandC = []
plural1 = []
U = set(random.sample(range(0, 256),256))
min_range = 0
max_range = 256
i = 1

# Функція виклику головного вікана
def main_window():

    # Функції генерування множин за вказаною потужністю
    def generete_plural_A(plural_power = 3):
        global A
        if (plural_power > 256 or plural_power < 0):
            messagebox.showerror(title="Помилка", message="Введіть потужність від 0 до 256!")
        else:
            A = set(random.sample(range(min_range, max_range),plural_power))
            A_Entry.delete(0,1500)
            A_Entry.insert(0,sorted(A))

    def generete_plural_B(plural_power = 3):
        global B
        if (plural_power > 256 or plural_power < 0):
            messagebox.showerror(title="Помилка", message="Введіть потужність від 0 до 256!")
        else:
            B = set(random.sample(range(min_range, max_range), plural_power))
            B_Entry.delete(0,1500)
            B_Entry.insert(0,sorted(B))


    def generete_plural_C(plural_power = 3):
        global C
        if (plural_power > 256 or plural_power < 0):
            messagebox.showerror(title="Помилка", message="Введіть потужність від 0 до 256!")
        else:
            C = set(random.sample(range(min_range, max_range), plural_power))
            C_Entry.delete(0,1500)
            C_Entry.insert(0,sorted(C))

    # Функція для збережння певного діапазону генерування множин
    def set_range(min = 0,max = 256):
        global min_range
        global max_range
        global U
        # Сортування значень , якщо коритувач ввів їх навпаки
        if (min > max):
            maxx = min
            min = max
            max = maxx
        # Перевірка можливого діапазону
        if ((min < 0) or (max > 256)):
            messagebox.showerror(title="Помилка", message="Введіть діапазон від 0 до 256!")
            min_range = 0
            max_range = 256
        else:
            min_range = min
            max_range = max
            U = set(random.sample(range(min_range, max_range), max_range - min_range))
            min_range_entry.delete(0, 3)
            min_range_entry.insert(0, min_range)
            max_range_entry.delete(0, 3)
            max_range_entry.insert(0, max_range)

    # Функція для збереження множин, змін потужності , якщо це потрібно і сортування для виведення
    def save_plural(A_E,B_E,C_E):
        global A
        global B
        global C
        global min_range
        global max_range
        A_E = set(map(int, A_E.split(' ') ))
        B_E = set(map(int, B_E.split(' ') ))
        C_E = set(map(int, C_E.split(' ') ))

        if max(A_E) > max_range or max(B_E) > max_range or max(C_E) > max_range or min(A_E) < min_range or min(B_E) < min_range or min(C_E) < min_range:
            messagebox.showerror(title="Помилка", message="Введені елементи не входять до діапазону!")
        else:
            A = set(A_E)
            B = set(B_E)
            C = set(C_E)
            A_Entry.delete(0, 1500)
            A_Entry.insert(0, sorted(A))
            A_power_Entry.delete(0, 3)
            A_power_Entry.insert(0, len(A))
            B_Entry.delete(0, 1500)
            B_Entry.insert(0, sorted(B))
            B_power_Entry.delete(0, 3)
            B_power_Entry.insert(0, len(B))
            C_Entry.delete(0, 1500)
            C_Entry.insert(0, sorted(C))
            C_power_Entry.delete(0, 3)
            C_power_Entry.insert(0, len(C))

    # Створення головного вікна
    main_window = tk.Tk()
    main_window.title("Головне меню" )
    main_window.geometry("800x500")

    tk.Label(main_window, text="Головне меню", font='ubuntu 20').pack()

    # Створення 4 кнопок для виклику вікон
    tk.Button(main_window, text="Вікно 2", command = window2).place(relx = 0.3, rely = 0.1)
    tk.Button(main_window, text="Вікно 3", command = window3).place(relx = 0.4, rely = 0.1)
    tk.Button(main_window, text="Вікно 4", command = window4).place(relx = 0.5, rely = 0.1)
    tk.Button(main_window, text="Вікно 5", command = window5).place(relx = 0.6, rely = 0.1)

    # Виведення ПІП, групи, номер у списку і варінту
    tk.Label(main_window, text=("Шерстюк","Максим","Олександрович.","Номер","групи:", G)).place(x = 10, rely = 0.2)
    tk.Label(main_window, text=("Номер", "у", "списку:", N)).place(x = 10, rely = 0.25)
    tk.Label(main_window, text=("Варіант:", (N + G % 60) % 30 + 1)).place(x = 10, rely = 0.3)

    # Введенняя потужності множин і генерування самих множин
    tk.Label(main_window, text='Потужність множини A:').place(relx = 0.1, rely = 0.35)
    A_power_Entry = tk.Entry(main_window)
    A_power_Entry.place(relx = 0.1, rely = 0.4)
    tk.Label(main_window, text='Потужність множини B:').place(relx = 0.4, rely = 0.35)
    B_power_Entry = tk.Entry(main_window)
    B_power_Entry.place(relx = 0.4, rely = 0.4)
    tk.Label(main_window, text='Потужність множини C:').place(relx = 0.7, rely = 0.35)
    C_power_Entry = tk.Entry(main_window)
    C_power_Entry.place(relx = 0.7, rely = 0.4)

    # Кнопки для генерування множин
    tk.Button(main_window, text='Згенерувати A:', command = lambda :
        generete_plural_A(int(A_power_Entry.get()))).place(relx=0.125, rely=0.47)
    tk.Button(main_window, text='Згенерувати B:', command = lambda :
        generete_plural_B(int(B_power_Entry.get()))).place(relx=0.425, rely=0.47)
    tk.Button(main_window, text='Згенерувати C:', command = lambda :
        generete_plural_C(int(C_power_Entry.get()))).place(relx=0.725, rely=0.47)

    # Введенняя і вивід множин
    tk.Label(main_window, text='Множина A:').place(relx = 0.1, rely = 0.55)
    A_Entry = tk.Entry(main_window)
    A_Entry.place(relx = 0.1, rely = 0.6)
    tk.Label(main_window, text='Множина B:').place(relx = 0.4, rely = 0.55)
    B_Entry = tk.Entry(main_window)
    B_Entry.place(relx = 0.4, rely = 0.6)
    tk.Label(main_window, text='Множина C:').place(relx = 0.7, rely = 0.55)
    C_Entry = tk.Entry(main_window)
    C_Entry.place(relx = 0.7, rely = 0.6)
    tk.Button(main_window, text='Зберегти множини',
        command=lambda: save_plural(str(A_Entry.get()), str(B_Entry.get()), str(C_Entry.get()) )).place(relx=0.42, rely=0.65)

    # Введенняя діапазону генерування
    tk.Label(main_window, text='Введіть діапазон:').place(relx = 0.42, rely = 0.75)
    min_range_entry = tk.Entry(main_window)
    min_range_entry.place(relx = 0.3, rely = 0.8)
    max_range_entry = tk.Entry(main_window)
    max_range_entry.place(relx = 0.5, rely = 0.8)
    tk.Button(main_window, text='Зберегти діапазон',
              command=lambda: set_range(int(min_range_entry.get()),int(max_range_entry.get()))).place(relx=0.42, rely=0.85)
    min_range_entry.delete(0, 3)
    min_range_entry.insert(0, 0)
    max_range_entry.delete(0, 3)
    max_range_entry.insert(0, 256)

    main_window.mainloop()

# Функція виклику 2 вікна
def window2():
    global i
    i = 1
    # Функція для збережння D у файл
    def save():
        global D_long
        with open(r"long_D.txt", mode="w+", encoding="utf-8") as f:
            f.write(str(D_long))

    # Функція для виведення кроків , та обрахунку
    def step():
        global i
        global A
        global B
        global C
        global AandB
        global AandnotB
        global notAandC
        global plural1
        global D_long
        if (i == 1):
            AandB = A|B
            text = "A ∪ B = " + str(sorted(AandB))
            tk.Label(window2, text=text).place(x=5, y=135)
        elif (i == 2):
            AandnotB = U.difference(B)|A
            text = "A ∪ B̅ = " + str(sorted(AandnotB))
            tk.Label(window2, text=text).place(x=5, y=165)
        elif (i == 3):
            notAandC = U.difference(A)|C
            text = "A̅ ∪ C = " + str(sorted(notAandC))
            tk.Label(window2, text=text).place(x=5, y=195)
        elif (i == 4):
            plural1 = AandB|AandnotB
            text = "(A ∪ B)∪(A ∪ B̅) = " + str(sorted(plural1))
            tk.Label(window2, text=text).place(x=5, y=225)
        elif (i == 5):
            plural1 = U.difference(B)&plural1
            text = "((A ∪ B)∪(A ∪ B̅)) ∩ B̅ = " + str(sorted(plural1))
            tk.Label(window2, text=text).place(x=5, y=255)
        elif (i == 6):
            plural1 = plural1&A
            text = "((A ∪ B)∪(A ∪ B̅)) ∩ B̅ ∩ A = " + str(sorted(plural1))
            tk.Label(window2, text=text).place(x=5, y=285)
        elif (i == 7):
            D_long = plural1&notAandC
            text = "D = " + str(sorted(D_long))
            tk.Label(window2, text=text).place(x=5, y=315)
        i = i + 1

    window2 = tk.Tk()
    window2.title("Вікно 2" )
    window2.geometry("600x400")
    # Вивід множин
    tk.Label(window2, text=("А=", A)).place(x = 5, y = 0)
    tk.Label(window2, text=("B=", B)).place(x = 5, y = 25)
    tk.Label(window2, text=("C=", C)).place(x = 5, y = 50)
    tk.Label(window2, text=("D = ((A ∪ B) ∪ (A ∪ B̅)) ∩ B̅ ∩ A ∩ (A̅ ∪ C)")).place(x = 5, y = 75)
    # Кнопка для покрокового виводу розв'зку
    tk.Button(window2, text='Крок',command=lambda: step()).place(relx = 0.45, y = 100)
    # Кнопка для збереження результату
    tk.Button(window2, text='Зберегти результат', command=lambda: save()).place(relx=0.37, y=350)
    window2.mainloop()

# Функція виклику 2 вікна
def window3():
    global i
    i = 1

    # Функція для збережння D у файл
    def save():
        global D_short
        with open(r"short_D.txt", mode="w+", encoding="utf-8") as f:
            f.write(str(D_short))

    # Функція для виведення кроків , та обрахунку
    def step():
        global i
        global A
        global B
        global C
        global plural1
        global D_short
        if (i == 1):
            plural1 = A&C
            text = "A ∩ C = " + str(sorted(plural1))
            tk.Label(window3, text=text).place(x=5, y=135)
        elif (i == 2):
            D_short = U.difference(B)&plural1
            text = "D = " + str(sorted(D_short))
            tk.Label(window3, text=text).place(x=5, y=165)
        i = i + 1

    window3 = tk.Tk()
    window3.title("Вікно 3" )
    window3.geometry("600x250")
    # Вивід множин
    tk.Label(window3, text=("А=", A)).place(x = 5, y = 0)
    tk.Label(window3, text=("B=", B)).place(x = 5, y = 25)
    tk.Label(window3, text=("C=", C)).place(x = 5, y = 50)
    tk.Label(window3, text=("D = B̅ ∩ (A ∩ C)")).place(x = 5, y = 75)
    # Кнопка для покрокового виводу розв'зку
    tk.Button(window3, text='Крок',command=lambda: step()).place(relx = 0.45, y = 100)
    # Кнопка для збереження результату
    tk.Button(window3, text='Зберегти результат', command=lambda: save()).place(relx=0.37, y=200)
    window3.mainloop()

# Функція виклику 4 вікна
def window4():

    # Функція для збережння D у файл
    def save():
        global Z
        with open(r"Z.txt", mode="w+", encoding="utf-8") as f:
            f.write(str(Z))

    global A
    global B
    global C
    global X
    global Y
    global Z

    window4 = tk.Tk()
    window4.title("Вікно 4" )
    window4.geometry("450x200")

    # Присвоєння
    X = B
    Y = Dopovnenya(U, A)
    Z = Obyednannja(X, Y)

    # Вивід множин
    tk.Label(window4, text=("X=", X)).place(x = 5, y = 0)
    tk.Label(window4, text=("Y=", Y)).place(x = 5, y = 25)
    tk.Label(window4, text=("Z=", Z)).place(x = 5, y = 50)

    # Кнопка для збереження результату
    tk.Button(window4, text='Зберегти результат', command=lambda: save()).place(relx=0.35, y=100)

    window4.mainloop()

# Функція виклику 5 вікна
def window5():

    # Функція для зчитування данних з файлу long_D.txt
    def readD_long():
        global D_long
        with open(r"long_D.txt", mode="r") as f:
            D_long = f.read()
            tk.Label(window5, text="Звичайний вираз, D =" + str(D_long)).place(x=150, y=30)

    # Функція для зчитування данних з файлу short_D.txt
    def readD_short():
        global D_short
        with open(r"short_D.txt", mode="r") as f:
            D_short = f.read()
            tk.Label(window5, text="Спрощений вираз, D =" + str(D_short)).place(x=150, y=80)

    # Функція для зчитування данних з файлу Z.txt
    def readZ():
        global Z
        with open(r"Z.txt", mode="r") as f:
            Z = f.read()
            tk.Label(window5, text="Z = X ∪ Y =" + str(Z)).place(x=150, y=130)

    # Функція для зчитування данних з файлу readZ.txt
    def calculate_Z():
        global Z2
        Z2 = str(B|U.difference(A))
        tk.Label(window5, text="Z = X ∪ Y =" + str(Z2)).place(x=150, y=180)


    # Функція для порівняння D
    def compareD():
        global D_short
        global D_long
        if (D_short == D_long):
            tk.Label(window5, text="Результати D однакові").place(relx = 0.17, rely = 0.83)
        else:
            tk.Label(window5, text="Результати D різні").place(relx = 0.17, rely = 0.83)

    # Функція для порівняння Z
    def compareZ():
        global Z
        global Z2
        if (Z == Z2):
            tk.Label(window5, text="Результати Z однакові").place(relx = 0.57, rely = 0.83)
        else:
            tk.Label(window5, text="Результати Z різні").place(relx = 0.57, rely = 0.83)

    window5 = tk.Tk()
    window5.title("Вікно 5" )

    # Кнопки для зчитування файлів і розрахунку
    tk.Button(window5, text='Зчитати 1 файл', command=lambda: readD_long()).place(x=10, y=25)
    tk.Button(window5, text='Зчитати 2 файл', command=lambda: readD_short()).place(x=10, y=75)
    tk.Button(window5, text='Зчитати 3 файл', command=lambda: readZ()).place(x=10, y=125)
    tk.Button(window5, text='Розрахувати Z ', command=lambda: calculate_Z()).place(x=10, y=175)

    tk.Button(window5, text='Порівняти D', command=lambda: compareD()).place(relx = 0.2, rely = 0.7)
    tk.Button(window5, text='Порівняти Z ', command=lambda: compareZ()).place(relx = 0.6, rely = 0.7)

    window5.geometry("800x350")
    window5.mainloop()

# Об'єднання U
def Obyednannja(a, b):
    a = list(a)
    b = list(b)
    c = []
    for i in a:
        c.append(i)
    for i in b:
        if i not in c:
            c.append(i)
    c.sort()
    return set(c)

# Доповенення
def Dopovnenya(a, b):
    a = list(a)
    b = list(b)
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    c.sort()
    return set(c)

main_window()
