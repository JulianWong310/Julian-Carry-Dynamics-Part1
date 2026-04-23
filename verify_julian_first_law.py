def verify_julian_first_law(B, k, max_n):
    # Calculate the Stable Tail (T)
    T = (B ** 2) % (10 ** k)
    # Calculate the Julian Constant (C_J)
    C_J = (B * T - T) // (10 ** k)

    # Starting Leading Part (A_2)
    A = (B ** 2) // (10 ** k)

    for n in range(3, max_n+1):

        # Applying Julian's First Law: A_n = B * A_{n-1} + C_J
        predict_A = B * A + C_J

        # Calculating actual value for validation
        actual_A = (B ** n) // (10 ** k)

        # Iterating: The current prediction becomes the base for the next power
        A = predict_A

        # Verify if the Law holds true
        print(f"n={n}: {predict_A == actual_A}")



if __name__ == "__main__":
    verify_julian_first_law(B=5,  k=2, max_n=10)