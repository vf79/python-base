# Para realizar trace
# python -m trace -s --count -C . .\extras\simple.py

import time
name = "Simple"


def sum(x, y):
    return x + y


def hello(name):
    time.sleep(3)
    return f"Hello {name}"


if __name__ == "__main__":
    # print(sum(3, 5))
    # print(sum(5, 55))
    print(hello(name=name))
