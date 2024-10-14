'''' english.french.translator
 Create an English to French translator program.
 The program takes a word from the user as an input and translates it using a dictionary data type as a vocabulary
 Please add the translation of 'prune' in your homework ®.
 If word is not in the code vocabulary print (Iword) is not in my memory)
 ***The user will select the language they would to translate to*** (optional)'''''

# . Dictionary for English to French translation
vocabulary = {  "apple": "pomme",
    "banana": "banane",
    "orange": "orange",
    "grape": "raisin",
    "prune": "prune", # adding the translation for prune
    "car": "voiture",
    "house": "maison",
    "cat": "chat",
    "dog": "chien",
    "book": "livre"}

# use the  inputed word  to translate to french language

word = input("Enter an English word to translate: ").lower()

# Translate the word
if word in vocabulary:
    print(f"The French translation of '{word}' is '{vocabulary[word]}'")
else:
    print(f"'{word}' is unknown to my memory")