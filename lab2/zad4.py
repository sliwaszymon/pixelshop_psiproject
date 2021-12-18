def foo(amount, temperature_type):
    if temperature_type == 'Fahrenheit':
        return float(amount) * (9 / 5) + 32
    elif temperature_type == 'Rankine':
        return float(amount)  * 1.8 + 491.67
    elif temperature_type == 'Kelvin':
        return float(amount) + 273.15
    else:
        print('Wrong temperature type. Use Fahrenheit, Rnkine or Kelvin.')
        return 'error'

print(foo(12, 'Fahrenheit'))
print(foo(12, 'Kelvin'))
print(foo(12, 'Rankine'))
print(foo(12, 'Celsius')) # just for test the error