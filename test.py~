import nltk
import random

text = "This is a sample text. It can be used for text generation tasks."
nltk.download('punkt')

tokens = nltk.word_tokenize(text)

bigrams = list(nltk.bigrams(tokens))

# generate text based on bigrams
generated_text = []

# start with a random word
seed_word = random.choice(tokens)
# print(seed_word)
generated_text.append(seed_word)

# set desired length of the generated text
desired_length = 20

for _ in range(desired_length - 1):
    # find all bigrams that start with the last word in generated text
    possible_next_words = [bigram[1] for bigram in bigrams if bigram[0] == generated_text[-1]]

    # chooose a random next word from the possibilities
    next_word = random.choice(possible_next_words)

    generated_text.append(next_word)

# join the generated words to form the final generated text
generated_text = ' '.join(generated_text)
print(generated_text)


