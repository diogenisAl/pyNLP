import textblob
from textblob import TextBlob

blob = TextBlob('Ποιο είναι το όνομά σου?') # Works like input() but for a TextBlob object

english = blob.translate(to='en') # To "to" είναι η λέξη κλειδί για την γλώσσα μετάφρασής
print(english)

spanish = blob.translate(to='es')
print(spanish)