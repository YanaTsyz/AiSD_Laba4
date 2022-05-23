import random
import time

def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

print("\n---------- Результат работы программы ----------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100 : "))
    while row_q < 6 or row_q > 100:
        row_q = int(input("Вы ввели неверное число.\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100 : "))
    K = int(input("Введите число К = "))
    start = time.time()
    A, F, AF, FA, AT, FT = [], [], [], [], [], [] # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        FA.append([0] * row_q)
        AT.append([0] * row_q)
        FT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):                        # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    
    for i in range(row_q):                        # формируем матрицу F, копируя из матрицы А
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []                                        # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):                         # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[size + row_q % 2 + i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)

    E = []                                        # задаем матрицу E
    size = row_q // 2
    for i in range(size):
        E.append([0] * size)

    for i in range(size):                         # формируем подматрицу E
        for j in range(size):
            E[i][j] = F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(E, "E", time_next - time_prev)

    # количество нулей по периметру области 2

    quantity = 0
    multiplication = 1
    point = 0

    for x in range(size - 1, size // 2 - 1, -1):             # считаем нули внизу "треугольника"
        for y in range(size - 1, size // 2, -1):
            if C[x][-1 - point] == 0:
                quantity += 1
            point += 1
            break
        
                                                             # прошли через границу симметрии и считаем количество нулей сверху "треугольника"

    if size % 2 == 1:                                        # центр есть 
        point = 1
        for x in range(size // 2 - 1, 0 - 1, -1):
            for y in range(size // 2 + 1, size, 1):
                if C[x][size // 2 + point] == 0:
                    quantity += 1
                point += 1
                break
    else:                                                    # центра нет 
        point = 0
        for x in range(size // 2 - 1, 0 - 1, -1):
            for y in range(size // 2, size, 1):
                if C[x][(size // 2) + point] == 0:
                    quantity += 1
                point += 1
                break

    for i in range(1, size-1):                               # проверяем основание "треугольника"
        for j in range(size):
            point=0
            if C[i+point][size-1] == 0:
                quantity += 1
                point += 1
            break

    # произведение чисел по периметру области 4

    point = 0

    for x in range(size - 1, size // 2 - 1, -1):             # считаем произведение внизу "треугольника"
        for y in range(0 , size // 2, 1):
            multiplication *= C[x][point]
            point += 1
            break
  
                                                             # прошли через границу симметрии и считаем произведение сверху "треугольника"
    
    if size % 2 == 1:                                        # центр есть
        point = 1
        for x in range(size // 2 - 1, 0 - 1, -1):
            for y in range(size // 2 + 1, size, 1):
                multiplication *= C[x][size // 2 - point]
                point += 1
                break
    else:                                                    # центра нет
        point = 1
        for x in range(size // 2 - 1, 0 - 1, -1):
            for y in range(size // 2, size, 1):
                multiplication *= C[x][(size // 2) - point]
                point += 1
                break

    for i in range(1, size-1):                               # добавляем к произведению основание "треугольника"
        for j in range(1):
            point=0
            multiplication *= C[i+point][0]
            point+=1
            break
        
    variable = 0

    if quantity > multiplication:                            # меняем 1 и 4 области симметрично подматрице E
        print("Случай 1.")                  
        for i in range (size - 1, 0, -1):
            for j in range (0 , size // 2, 1):
                if i != j:
                    E[i][j], E[j][i] = E[j][i], E[i][j]
        E[size - 1][1], E[1][size - 1] = E[1][size - 1], E[size - 1][1]
                    
        print_matrix(E,"E изменённая",time_next-time_prev)
    else:
        print("Случай 2.")
        for i in range(0, size + row_q % 2):                 # меняем подматрицы C и B местами несимметрично
            for j in range(size + row_q % 2, row_q): 
                variable = F [i][j]
                F [i][j] = F[i + size + row_q % 2][j]
                F[i + size + row_q % 2][j] = variable
        print_matrix(F,"F",time_next-time_prev)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", 0)

    # считаем пример ((К * AT) * (F + А) - K * FT) по действиям
    
    for i in range(row_q):                                 # AT
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)
        
    for i in range(row_q):                                 # FT
        for j in range(i, row_q, 1):
            FT[i][j], FT[j][i] = F[j][i], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "F^T", time_next - time_prev)

    for i in range(row_q):                                 # K * AT
        for j in range(row_q):
            AT[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K * A^T", time_next - time_prev)

    for i in range(row_q):                                 # F + A
        for j in range(row_q):
            FA[i][j] = F[i][j] + A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "F + A", time_next - time_prev)

    for i in range(row_q):                                 # K * FT
        for j in range(row_q):
            FT[i][j] = K * FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K * F^T", time_next - time_prev)

    for i in range(row_q):                                 # (К * AT) * (F + А)
        for j in range(row_q):
            AF[i][j] = AT[i][j] * FA[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "(К * A^T) * (F + А)", time_next - time_prev)

    for i in range(row_q):                                 # ((К * AT) * (F + А) - K * FT)
        for j in range(row_q):
            AF[i][j] = AF[i][j] - FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "((К * A^T) * (F + А) - K * F^T)", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except ValueError:
   print("\nЭто не число.")

