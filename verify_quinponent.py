def verify_quinponent(n):
    front = 0  # Starting with 5^2
    for i in range(2, n + 1):
        result = 5 ** i
        print(f"5^{i} = {result} | Leading part is {front}")
        front = front * 5 + 1

if __name__ == "__main__":
    verify_quinponent(10)