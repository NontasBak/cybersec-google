def square_and_multiply(base, exponent, modulus):
    binary_exp = bin(exponent)[2:]

    print(f"Exponent: {exponent}")
    print(f"Binary:   {binary_exp}\n")

    print(
        f"{'Step':<5} | {'Bit':<3} | {'Operation':<17} | {'Calculation':<25} | {'Result':<5}"
    )
    print("-" * 70)

    # First step: Initialization (MSB is always 1)
    result = base
    print(f"{'1':<5} | {'1':<3} | {'Initial':<17} | {'-':<25} | {result:<5}")

    # Iterate through the rest of the bits
    step_count = 2
    for bit in binary_exp[1:]:
        prev_result = result

        # Always Square first
        result = (result * result) % modulus
        op_name = "Square"
        calc_desc = f"{prev_result}^2"

        # If bit is 1, also Multiply
        if bit == "1":
            result = (result * base) % modulus
            op_name = "Square & Multiply"
            calc_desc = f"({prev_result}^2) * {base}"

        print(
            f"{step_count:<5} | {bit:<3} | {op_name:<17} | {calc_desc + ' mod n':<25} | {result:<5}"
        )
        step_count += 1

    print("-" * 70)
    print(f"Final Result: {result}")


m = 1234
e = 24377
n = 41567

square_and_multiply(m, e, n)
