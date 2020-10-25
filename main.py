
def sentence_maker(phrase):
     interrogatives = ("how","what","why")
     capitalize = phrase.capitalize()
     if phrase.startswith(interrogatives):
         return "{}?".format(capitalize)
     else:
         return "{}.".format(capitalize)

results  = []
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
print(" ".join(results))

