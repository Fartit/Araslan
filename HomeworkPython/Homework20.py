
import re

number_abonent = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'

validacia = r'\+*\d{1}\s*\(?\d{3}\)?\s*\d{3}[\s-]*\d{2}[\s-]*\d{2}'

print(re.findall(validacia, number_abonent))


