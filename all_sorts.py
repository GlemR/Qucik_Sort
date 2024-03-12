import copy
import random
import timeit

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def qckrec(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        qckrec(arr, start, p - 1)
        qckrec(arr, p + 1, end)


def qckit(arr, start, end):
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        pivot_index = partition(arr, start, end)
        if pivot_index - 1 > start:
            stack.append((start, pivot_index - 1))
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))

def make_heap(arr, n, i):
    largest = i  # rodzic
    left = 2 * i + 1  # left = 2i + 1
    right = 2 * i + 2  # right = 2*i + 2
    if left < n and arr[left] < arr[largest]:  # jeżeli istnieje lewe dziecko i lewe dziecko jest mniejsze niż rodzic
        largest = left
    if right < n and arr[right] < arr[largest]:  # jeżeli istnieje prawe dziecko i prawe dziecko jest mniejsze niż rodzic
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        make_heap(arr, n, largest)

def heapSort(arr, n):
    for i in range(n // 2 - 1, -1, -1):  # last parent = n//2 -1, -1 bo zaczynamy indeksowanie od 0
        make_heap(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        make_heap(arr, i, 0)



def merge_sort(arr):
    global c
    if len(arr) > 1: #dzielenie zbiorow az podzbiory beda mialy po 1 elemencie
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        c += 1



def insertion_sort(matrix, start, jump):
    for j in range(start + jump, len(matrix), jump):
        x = matrix[j]
        i = j - jump
        while i >= 0 and matrix[i] < x:
            matrix[i + jump] = matrix[i]
            i = i - jump
        matrix[i + jump] = x
    return matrix
def shell_sort_hibbard(matrix):
    n = len(matrix)
    h = 1
    while h <= n / 2:
        h = 2 * h + 1  #hibbard 1 3 7 15 31..
    h//=2
    while h >= 1:
        print("Przyrost Hibbarda:", h)
        for i in range(h):
            insertion_sort(matrix, i, h)
        h //= 2


#arr = list(map(int,input().split()))
arr = [random.randint(1, 500) for _ in range(10)]
n = len(arr)
arr_qckit = copy.deepcopy(arr)
arr_qckre = copy.deepcopy(arr)
arr_shell = copy.deepcopy(arr)
arr_merge = copy.deepcopy(arr)
arr_heap = copy.deepcopy(arr)
print("Przed sortowaniem:", arr)
print("quick  sort iteracyjny:")
elapsed_time = timeit.timeit(lambda: qckit(arr_qckit, 0, n-1), number=1)
print(f"czas: {elapsed_time}")
print(arr_qckit)
print("quick sort rekurencyjny")
elapsed_time = timeit.timeit(lambda: qckrec(arr_qckre, 0, n-1), number=1)
print(f"czas: {elapsed_time}")
print(arr_qckre)
print("heap sort")
elapsed_time = timeit.timeit(lambda: heapSort(arr_heap, n), number=1)
print(f"czas: {elapsed_time}")
print(arr_heap)
print("merge sort")
c = 0
elapsed_time = timeit.timeit(lambda:  merge_sort(arr_merge), number=1)
print(f"czas: {elapsed_time}")
print(arr_merge)
print("liczba scalen: ", c)
print("shell sort")
elapsed_time = timeit.timeit(lambda: shell_sort_hibbard(arr_shell), number=1)
print(f"czas: {elapsed_time}")
print(arr_shell)