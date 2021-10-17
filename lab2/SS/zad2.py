def foo(data_text):
    info = {
        'lenght': len(data_text),
        'letters': list(set(list(data_text.replace(' ','').replace(',','').replace('.','')))),
        'big_letters': data_text.upper(),
        'small_letters': data_text.lower()
    }
    return info

text = 'Ala ma kota, a kot ma Alę.'
print(foo(text))