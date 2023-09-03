
''''
import spacy

# Load the English pre-trained model
nlp = spacy.load("en_core_web_sm")


# Process a text string
text = "SpaCy is a powerful natural language processing library."
doc = nlp(text)


# Access tokenized words and part-of-speech tags
for token in doc:
	print(token.text, token.pos_)

'''
import os 

cwd = os.getcwd()

path = os.path.join(cwd, "lyrics.txt")
path = "lyrics.txt"


with open(path) as file:
	lst = [song for song in file.read().split('<end>')]

print(lst)
