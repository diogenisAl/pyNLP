import autocomplete

autocomplete.load()

# Imagine writing "the b"
a = autocomplete.predict('the','b')

# Now you type an "o"
b = autocomplete.predict('the','bo')

print(a)
print(b)
