
def foo(temperature,temperature_type):
	if (temperature_type=="Fahrenheit"):
		return float(temperature) * 1.8 + 32
	elif (temperature_type=="Rankine"):
		return (float(temperature) + 273.15) * (9/5)
	elif (temperature_type=="Kelvin"):
		return float(temperature) + 273.15
	else:
		return "type error please choose from Fahrenheit,Rankine or Kelvin"

print(foo(-273.15,"Fahrenheit"))
print(foo(-273.15,"Rankine"))
print(foo(-273.15,"Kelvin"))
print(foo(-273.15,"TEST"))
