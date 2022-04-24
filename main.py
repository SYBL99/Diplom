def g1(x):
    return 0.01776 * x ** 2 - 9.583397 * x


def g2(x):
    return -3.38 * 10 ** -4 * x ** 2 + 0.151712 * x


def g3(x):
    return 2.24 * 10 ** -5 * x ** 2 - 0.01562 * x


def g4(x):
    return 2.39 * 10 ** -4 * x ** 2 - 0.047 * x


def g5(x):
    return 0.0137 * x


def create_matrix():
    V = [12, 15, 18, 21, 24, 27, 30]
    D = [260, 263, 266, 269, 272, 275]
    C = [50, 60, 70, 80, 90]
    CH = [185, 188, 191, 194, 197, 200]
    CS = [100, 110, 120, 130, 140]
    mass = []
    index_list = []
    for i in range(len(V) - 1):
        pair_V = [V[i], V[i + 1]]
        for j in range(len(D) - 1):
            buff = []
            pair_D = [D[j], D[j + 1]]
            index_list.append([pair_V, pair_D])
            for k in range(len(C) - 1):
                pair_C = [C[k], C[k + 1]]
                for n in range(len(CH) - 1):
                    pair_CH = [CH[n], CH[n + 1]]
                    for l in range(len(CS) - 1):
                        pair_CS = [CS[l], CS[l + 1]]
                        buff.append(1364.16672 + g5(pair_V[0]) + min(g1(pair_D[0]), g1(pair_D[1])) +
                                    min(g2(pair_CH[0]), g2(pair_CH[1])) + g3(pair_C[1]) + g4(pair_CS[1]))
            mass.append(buff)
    return mass, index_list


def wald_criterion(matrix):
    min_mass = []
    for i in range(len(matrix)):
        min_mass.append(min(matrix[i]))
    return min_mass.index(max(min_mass))


def savage_criterion(matrix):
    max_mass = []
    for j in range(len(matrix[0])):
        buff = []
        for i in range(len(matrix)):
            buff.append(matrix[i][j])
        max_mass.append(max(buff))
    risk_mass = []
    for i in range(len(matrix)):
        risk_mass.append(matrix[i].copy())
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            risk_mass[i][j] = max_mass[j] - risk_mass[i][j]
    max_mass = []
    for i in range(len(matrix)):
        max_mass.append(max(risk_mass[i]))
    return max_mass.index(min(max_mass))


def hurwitz_criterion(matrix, y):
    mass = []
    for i in range(len(matrix)):
        mass.append(y * min(matrix[i]) + (1-y) * max(matrix[i]))
    return mass.index(max(mass))


data, index = create_matrix()
print('Введите коэффициент оптимизма "y" для критерия Гурвица в пределах (0, 1)')
try:
    y = float(input())
except Exception:
    print('Вводите значение через точку')
    y = float(input())
print('По Вальду (максимину) {} стратегия является лучшей со значениями V = {} и D = {}'.format(wald_criterion(data) + 1, index[wald_criterion(data)][0], index[wald_criterion(data)][1]))
print('По Сэвиджу (минимаксу) {} стратегия является лучшей со значениями V = {} и D = {}'.format(savage_criterion(data) + 1, index[savage_criterion(data)][0], index[savage_criterion(data)][1]))
print('По Гурвицу {} стратегия является лучшей со значениями V = {} и D = {}'.format(hurwitz_criterion(data, y) + 1, index[hurwitz_criterion(data, y)][0], index[hurwitz_criterion(data, y)][1]))
input()