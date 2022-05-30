# -------------------------------------------------
# Алгоритм Краскала поиска минимального остова графа
# -------------------------------------------------

# список ребер графа (длина, вершина 1, вершина 2)
graph = [
    (13, 1, 2), (18, 1, 3), (17, 1, 4),
    (14, 1, 5), (22, 1, 6), (26, 2, 3),
    (22, 2, 5), (3, 3, 4), (19, 4, 6)
]

sorted_graph = sorted(graph, key=lambda x: x[0])
nodes = set()  # список соединенных вершин
D = {}  # словарь списка изолированных групп вершин
edges = []  # список ребер остова

for r in sorted_graph:
    if r[1] not in nodes or r[2] not in nodes:  # проверка для исключения циклов в остове
        if r[1] not in nodes and r[2] not in nodes:  # если обе вершины не соединены, то
            D[r[1]] = [r[1], r[2]]  # формируем в словаре ключ с номерами вершин
            D[r[2]] = D[r[1]]  # и связываем их с одним и тем же списком вершин
        else:  # иначе
            if not D.get(r[1]):  # если в словаре нет первой вершины, то
                D[r[2]].append(r[1])  # добавляем в список первую вершину
                D[r[1]] = D[r[2]]  # и добавляем ключ с номером первой вершины
            else:
                D[r[1]].append(r[2])  # иначе, все то же самое делаем со второй вершиной
                D[r[2]] = D[r[1]]

        edges.append(r)  # добавляем ребро в остов
        nodes.add(r[1])  # добавляем вершины в множество U
        nodes.add(r[2])

for r in sorted_graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
    if r[2] not in D[r[1]]:  # если вершины принадлежат разным группам, то объединяем
        edges.append(r)  # добавляем ребро в остов
        gr1 = D[r[1]]
        D[r[1]] += D[r[2]]  # объединем списки двух групп вершин
        D[r[2]] += gr1

print(edges)

def kruckal(graph : list[list[int]]) -> list[list[int]]:
    return graph