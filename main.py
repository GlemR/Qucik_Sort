import copy
import sys
import timeit
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt

sys.setrecursionlimit(1000000)


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
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


if __name__ == '__main__':
    time_of_rec = {'random': [0]*7, 'ascending': [0]*7, 'descending': [0]*7, 'v_shaped': [0]*7, 'a_shaped': [0]*7}
    time_of_ite = {'random': [0]*7, 'ascending': [0]*7, 'descending': [0]*7, 'v_shaped': [0]*7, 'a_shaped': [0]*7}
    keys = ['random', 'ascending', 'descending', 'v_shaped', 'a_shaped']
    progress_bar = tqdm(total=350, desc="Progress")
    for count in range(7):
        with open(f'arrays_{count+1}_1k.txt', 'r') as f:
            x = f.readlines()
        for i, line in enumerate(x):
            line = line.strip()
            if i % 6 != 0:
                recursion = copy.deepcopy(line)
                iteration = copy.deepcopy(line)
                recursion = list(map(int, recursion.split(';')))
                iteration = list(map(int, iteration.split(";")))
                elapsed_time_rec = timeit.timeit(lambda: qckrec(recursion, 0, len(recursion) - 1), number=1)
                elapsed_time_ite = timeit.timeit(lambda: qckit(iteration, 0, len(iteration) - 1), number=1)
                time_of_rec[keys[i%6-1]][count] += elapsed_time_rec
                time_of_ite[keys[i % 6-1]][count] += elapsed_time_ite
                progress_bar.update(1)


    for key in time_of_rec.keys():
        for j in range(len(time_of_rec[key])):
            time_of_rec[key][j] = time_of_rec[key][j]/10
    for key in time_of_ite.keys():
        for j in range(len(time_of_ite[key])):
            time_of_ite[key][j] = time_of_ite[key][j]/10
    print("\ntime of recursive sort:")
    for k, v in time_of_rec.items():
        print(f'{k}\t{v}')
    print("\ntime of iterative sort:")
    for k, v in time_of_ite.items():
        print(f'{k}\t{v}')