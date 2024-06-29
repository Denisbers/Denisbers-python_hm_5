text_input = input('Please, enter text: ').title()

new_hash = '#'

for symbol in text_input:
    if symbol.isalnum():
        new_hash += symbol

print(new_hash[:140])