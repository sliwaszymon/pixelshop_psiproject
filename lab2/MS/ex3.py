
def foo(text,letter):
	result_string = ""
	for x in text:
		if x!=letter:
			result_string = result_string + x
	return result_string

print(foo("text","x"))