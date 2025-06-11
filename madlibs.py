import random

# Lists of words to choose from — add your own word to any list or create a new category!
adjectives = ["brilliant", "overcaffeinated"]
nouns = ["data scientist", "Blue Devil"]
verbs = ["debugged", "fine-tuned"]
places = ["Co-Lab", "Perkins Library"]
tools = ["TensorFlow", "GitHub Copilot"]

# Randomly select one item from each list
adj = random.choice(adjectives)
noun = random.choice(nouns)
verb = random.choice(verbs)
place = random.choice(places)
tool = random.choice(tools)

# Build the madlib sentence
print(f"At the {place}, a {adj} {noun} {verb} an AI model using {tool}.")
