#!python


def fibonnacci():
    a = 1
    b = 1
    # if n > 1:
    print(a)
    print(b)

    while True:
        bridge = a
        c = b
        d = bridge + c
        yield (d)
        a = b
        b = bridge + b


fib = fibonnacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
