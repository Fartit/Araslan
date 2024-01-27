
text = 'I am learning Python. hello, WORLD!'
start_pos = text.find('h') + 1
end_pos = text.rfind('h')
substring = text[start_pos:end_pos]
reversed_substring = substring[::-1]
text = text.replace(substring, reversed_substring)
print(text)

