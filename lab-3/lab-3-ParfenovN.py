# Лабораторная №3. Выполнил студенты группы БСТ2203 Парфенов Никита
# Вариант 18 (6): Алгоритм Йены

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import copy
import sys
import time

window = Tk()
window.title("Нахождение кратчайшего пути в ориентированном графе (Алгоритм Дейкстра)")
window.geometry('950x740')
window.resizable(False, False)


# Расчёт кратчайшего пути по алгоритм Дейкстру
def dijkstra(graph, start, end):

    length = len(graph)  # длина графа

    num_edges = 0
    for i in range(length):  # счёт ребер
        for j in range(length):
            if int(graph[i][j]) != 0:
                num_edges += 1

    time_ = time.perf_counter()

    distance = [[float("inf") for i in range(len(graph))] for j in range(len(graph))]  # Все расстояния делаем равным бесконечности
    for source in range(len(graph)):
        visited = [False] * len(graph)  # Создаем список посещенных вершин
        distance[source][source] = 0
        while not all(visited):
            min_distance = float("inf")
            index = -1
            for i in range(len(graph)):
                if not visited[i] and distance[source][i] < min_distance:
                    min_distance = distance[source][i]
                    index = i
            if index == -1:
                break
            visited[index] = True

            for i in range(len(graph)):
                # проверяем, что между вершинами существует ребро и вершина еще не посещена
                if graph[index][i] != "inf" and not visited[i]:
                    new_distance = distance[source][index] + int(graph[index][i])
                    if new_distance < distance[source][i]:
                        distance[source][i] = new_distance

    time_1 = time.perf_counter() - time_

    tree.insert("", "end", values=(length, num_edges, time_1 * 1000))

    return distance[int(start)][int(end)]


def draw_graph(matrix):
    graph = nx.DiGraph()
    n = len(matrix)
    edge_labels = {}

    for i in range(n):
        for j in range(n):
            if int(matrix[i][j]) != 0:
                graph.add_edge(str(i), str(j), weight=matrix[i][j])
                edge_labels[(str(i), str(j))] = matrix[i][j]

    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    pos = nx.circular_layout(graph)

    nx.draw_networkx_nodes(graph, pos=pos, ax=ax)
    nx.draw_networkx_labels(graph, pos=pos, ax=ax)
    nx.draw_networkx_edges(graph, pos=pos, arrows=True, ax=ax)  # Рисуем стрелки
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, ax=ax)

    return fig


def resultAdj_click():
    # Считываем матрицу смежности из элемента Text
    if selected.get() == 1:
        matrix_text = matrixAdj.get("1.0", tk.END)
        matrix = [list(line.strip().split()) for line in matrix_text.split("\n") if line.strip()]
    elif selected.get() == 2:
        matrix_text = matrixAdj.get("1.0", tk.END)
        matrix = [list(line.strip().split()) for line in matrix_text.split("\n") if line.strip()]

    source = Source_entry.get()
    target = Target_entry.get()

    fig = draw_graph(matrix)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=430, y=46)

    result = dijkstra(matrix, source, target)

    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(result))


# Очистка полей ввода
def clearAdj_click():
    matrixAdj.delete("1.0", tk.END)
    Source_entry.delete(0, tk.END)
    Target_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)


# Ввод из файла
def read_file():
    filename = filedialog.askopenfilename()  # Открываем диалоговое окно выбора файла
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Преобразуем строки в матрицу
    matrix = [list(map(int, line.strip().split())) for line in lines]

    matrixAdj.delete("1.0", tk.END)
    for row in matrix:
        matrixAdj.insert(tk.END, ' '.join(map(str, row)) + '\n')

    inputAdj_entry.configure(state="normal")  # Разблокировка текстового поля
    inputAdj_entry.delete(0, tk.END)
    inputAdj_entry.insert(0, filename)  # Вставляем путь нашего файла
    inputAdj_entry.configure(state="disabled")  # Блокировка текстового поля

    return matrix


# Создание элементов управления

selected = tk.IntVar()
matrixAdj_rb = Radiobutton(text="Матрица смежности", font=12, variable=selected, value=1)
matrixAdj_rb.place(x=10, y=10)
# matrixInd_rb = Radiobutton(text="Матрица инцидентности", font=12, variable=selected, value=2)
# matrixInd_rb.place(x=220, y=10)
selected.set(1)

inputAdj_entry = Entry(window, state='readonly', font=10)
inputAdj_entry.place(x=13, y=59, width=170)

inputAdj_btn = Button(width=15, text='Ввод из файла', command=read_file)
inputAdj_btn.place(x=200, y=56)

matrixAdj = Text(window, font=14)
matrixAdj.place(x=10, y=90, height=230, width=390)

Source_lbl = Label(text="Исходная вершина", font=12)
Source_lbl.place(x=10, y=325)
Source_entry = Entry()
Source_entry.place(x=200, y=328, width=100)

Target_lbl = Label(text="Конечная вершина", font=12)
Target_lbl.place(x=10, y=355)
Target_entry = Entry()
Target_entry.place(x=200, y=360, width=100)

resultAdj_btn = Button(window, width=10, text='Выполнить', command=resultAdj_click)
resultAdj_btn.place(x=10, y=450)
resetAdj_btn = Button(window, width=10, text='Сброс', command=clearAdj_click)
resetAdj_btn.place(x=100, y=450)

graph_lbl = Label(text="Исходный граф", font=14)
graph_lbl.place(x=570, y=12)

result_lbl = Label(text="Длина кратчайшего пути", font=14)
result_lbl.place(x=440, y=470)
result_entry = Entry()
result_entry.place(x=680, y=475)

Stats_lbl = Label(text="Статистика", font=14)
Stats_lbl.place(x=10, y=490)

tree = ttk.Treeview(window,
                    columns=("Кол-во вершин", "Кол-во ребер", "Длины маршрутов", "Время выполнения(ms)"),
                    show="headings")
tree.heading("#1", text="Кол-во вершин")
tree.heading("#2", text="Кол-во ребер")
tree.heading("#3", text="Время выполнения(ms)")
tree.column("#1", width=100)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.place(x=10, y=530, width=900, height=200)

window.mainloop()
