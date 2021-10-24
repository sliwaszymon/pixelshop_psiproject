text = "teXt"

def foo(data_text):
	result = {}
	result["len"]=len(data_text)
	result["letters"]=list(data_text.strip(" "))
	result["big_letters"]=list((data_text.upper()).strip(" "))
	result["small_letters"]=list((data_text.lower()).strip(" "))
	return result

print(foo(text))