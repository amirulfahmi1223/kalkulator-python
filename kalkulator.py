def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def divide(a, b):
    return a / b

# TODO Junior 2: tambah fungsi multiply(a, b)

if __name__ == "__main__":
    a = float(input("Angka pertama: "))
    b = float(input("Angka kedua: "))
    print("Tambah:", plus(a, b))
    print("Kurang:", minus(a, b))
    print("Bagi:", divide(a, b))