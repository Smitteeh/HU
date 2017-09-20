def convert(Celsius):
    Fahrenheit = Celsius * 1.8 + 32
    return Fahrenheit

print(convert(10))

def table():
    for Celsius in range(-30, 41, 10):
        Fahrenheit = Celsius * 1.8 + 32
        print('{:5} {:4}'.format(Fahrenheit, Celsius))

print(table())