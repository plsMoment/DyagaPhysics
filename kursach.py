import matplotlib
matplotlib.use("TkAgg")
import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np
from tkinter import *
#fig = plt.figure()

#lyambda = 3          # мкм
#c = 3 * 10 ** 14     # мкм/с
#L = 9                # мкм
#T = 4 * 10 ** (-14)  # с

#0.00000000000004
#300000000000000


def Po_n(n, L):
    return math.pi * (1 + 2 * n) / (2 * L)


def U_calculation_z_const(n, L, T, c, lyambda):
    U = 0
    tmp_z = L / 3
    interval_z = [tmp_z, tmp_z * 2, L]
    interval_t = np.linspace(0, T, 100)
    tmp_U = []
    U_data = []
    w = (2 * math.pi * c) / lyambda
    for z in interval_z:
        for t in interval_t:
            for i_n in range(n):
                Pn = Po_n(i_n, L)
                W_n = Pn * c
                if W_n - w == 0:
                    U += math.sin(Pn * z) * (math.sin(w * t) - w * t * math.cos(W_n * t)) / (2 * W_n)
                    print(t, z, i_n)
                else:
                    U += math.sin(Pn * z) * (W_n * math.sin(w * t) - w * math.sin(W_n * t)) / (W_n ** 2 - w ** 2)
            tmp_U.append(U)
            U = 0
        result = list(map(lambda item: item * 2 * c / L, tmp_U))
        tmp_U.clear()
        U_data.append(result)
    return U_data, interval_t, interval_z


def U_calculation_t_const(n, L, T, c, lyambda):
    U = 0
    tmp_t = T / 3

    interval_t = [tmp_t, tmp_t * 2, T]
    interval_z = np.linspace(0, L, 100)
    tmp_U = []
    U_data = []
    w = (2 * math.pi * c) / lyambda
    for t in interval_t:
        for z in interval_z:
            for i_n in range(n):
                Pn = Po_n(i_n, L)
                W_n = Pn * c
                if W_n - w == 0:
                    U += math.sin(Pn * z) * (math.sin(w * t) - w * t * math.cos(W_n * t)) / (2 * W_n)
                    print(t, z, i_n)
                else:
                    U += math.sin(Pn * z) * (W_n * math.sin(w * t) - w * math.sin(W_n * t)) / (W_n ** 2 - w ** 2)
            tmp_U.append(U)
            U = 0
        result = list(map(lambda item: item * 2 * c / L, tmp_U))
        tmp_U.clear()
        U_data.append(result)
    return U_data, interval_t, interval_z


def graph_U_t_const():
    n, L, T, c, lyambda = int(n_tf.get()), int(L_tf.get()), float(T_tf.get()), float(c_tf.get()), int(lyambda_tf.get())
    U_data, interval_t, interval_z = U_calculation_t_const(n, L, T, c, lyambda)
    i = 0
    for t in interval_t:
        plt.figure(figsize=(10, 10), dpi=80)

        plt.xlabel('z', color='red', fontsize=18)
        plt.ylabel('U(z,t)', color='red', fontsize=18)

        ax = plt.gca()

        ax.spines['right'].set_color('none')  # Удаление правой и верхней прямоугольных границ
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')  # Нижняя сторона, как ось x
        ax.yaxis.set_ticks_position('left')  # Левая сторона, как ось y

        ax.spines['bottom'].set_position(('data', 0))  #
        ax.spines['left'].set_position(('data', 0))

        plt.grid(True)
        ax.set_title(f'График зависимости U(z,t) от z при фиксированном t = {t}')
        plt.plot(interval_z, U_data[i], color="blue", linewidth=1, linestyle="-", label=f't = {t}')
        i += 1
        plt.show()

def graph_U_z_const():
    n, L, T, c, lyambda = int(n_tf.get()), int(L_tf.get()), float(T_tf.get()), float(c_tf.get()), int(lyambda_tf.get())

    U_data, interval_t, interval_z = U_calculation_z_const(n, L, T, c, lyambda)
    i = 0
    for z in interval_z:
        plt.figure(figsize=(8, 8), dpi=80)

        plt.xlabel('t', color='red', fontsize=18)
        plt.ylabel('U(z,t)', color='red', fontsize=18)

        ax = plt.gca()

        ax.spines['right'].set_color('none')  # Удаление правой и верхней прямоугольных границ
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')  # Нижняя сторона, как ось x
        ax.yaxis.set_ticks_position('left')  # Левая сторона, как ось y

        ax.spines['bottom'].set_position(('data', 0))  #
        ax.spines['left'].set_position(('data', 0))

        plt.grid(True)
        ax.set_title(f'График зависимости U(z,t) от t при фиксированном z = {z}')
        plt.plot(interval_t, U_data[i], color="blue", linewidth=1, linestyle="-", label=f'z = {z}')
        i += 1
        plt.show()

#graph_U_z_const(100, L, T, c)

window = Tk()
window.title('Калькулятор')
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

L_lb = Label(
    frame,
    text="Введите L"
)
L_lb.grid(row=3, column=1)

T_lb = Label(
    frame,
    text="Введите T",
)
T_lb.grid(row=4, column=1)

c_lb = Label(
    frame,
    text="Введите c",
)
c_lb.grid(row=5, column=1)

lyambda_lb = Label(
    frame,
    text="Введите lyambda",
)
lyambda_lb.grid(row=6, column=1)

n_lb = Label(
    frame,
    text="Введите n",
)
n_lb.grid(row=7, column=1)



L_tf = Entry(
    frame,
)
L_tf.grid(row=3, column=2, pady=5)

T_tf = Entry(
    frame,
)
T_tf.grid(row=4, column=2, pady=5)

c_tf = Entry(
    frame,
)
c_tf.grid(row=5, column=2, pady=5)

lyambda_tf = Entry(
    frame,
)
lyambda_tf.grid(row=6, column=2, pady=5)

n_tf = Entry(
    frame,
)
n_tf.grid(row=7, column=2, pady=5)


cal_btn = Button(
    frame,
    text='Рассчитать график с постоянной z',
    command=graph_U_z_const
)
cal_btn.grid(row=8, column=2)

cal_btn = Button(
    frame,
    text='Рассчитать график с постоянной t',
    command=graph_U_t_const
)
cal_btn.grid(row=9, column=2)

window.mainloop()


