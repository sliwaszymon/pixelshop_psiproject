def foo(text, letter, uppandlow=False):
    if uppandlow:
        return text.replace(letter.upper(),'').replace(letter.lower(),'')
    return text.replace(letter, '')

print(foo('Ala ma kota.', 'a'))
print(foo('Ala ma kota.', 'a', True))
print(foo('Ala ma kota.', 'A', True))