import sys

sys.set_int_max_str_digits(0)

def fast_power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
        #print(f"base = {base}, exponent = {exponent}, result = {result}")
    return result

def main():
    x = 2
    exponent = 65535
    result = fast_power(x, exponent)
    print(f"The value of {x}^{exponent} is {result}")

if __name__ == "__main__":
    main()
