import subprocess
if __name__ == "__main__":
    script_path = "generator.py"
    array = [1000,  2000, 3000, 4000, 5000, 6000, 7000]
    for i in range(7):
        subprocess.run(["python", script_path, str(array[i])])