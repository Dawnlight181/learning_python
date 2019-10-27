import random

words = {"cat":"animal", "dragon":"imaginary animal", "soup":"food", "computer":"useful tool", "febrary":"month"}
random_key = random.choice(list(words.items()))[0]
print(random_key)
