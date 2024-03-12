import sys
import random

def generate(n):
    max_value = 10 * n
    numbers = [random.randint(1, max_value) for _ in range(n)]
    return numbers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Invalid value for n. Please provide an integer.")
        sys.exit(1)

    filename = f"arrays_{n//1000}_1k.txt"
    with open(filename, "w") as file:
        for l in range(10):
            file.write(f'Iteration {l}\n')
            file.write(";".join(map(str, generate(n))) + "\n")
            file.write(";".join(map(str, sorted(generate(n)))) + "\n")
            file.write(";".join(map(str, sorted(generate(n), reverse=True))) + "\n")
            file.write(";".join(map(str, sorted(generate(n // 2), reverse=True) + sorted(generate(n // 2)))) + "\n")
            file.write(";".join(map(str, sorted(generate(n // 2)) + sorted(generate(n // 2), reverse=True))) + "\n")

    print(f"Arrays saved to {filename}")