def fib(nth_term):
    seq = [0, 1]
    while len(seq) < nth_term:
        seq.append(seq[-1] + seq[-2])

    return ', '.join(map(str, seq))

user_input = int(input("Enter the number of terms you need for the fib seq: \n\t"))

fib_result = fib(user_input)

print(f"The fib seq for {user_input} is : \n\t {fib_result}")