import random

# ========================================
# Welcome to the Duke AI Madlib Generator!
# ========================================
# This is your challenge:
# - Add ONE word to ANY/EACH of the lists below
# - OR create your own list (e.g., emotions, gadgets)
# - Make sure the sentence at the bottom uses your new word or category
# - Then commit your changes and open a pull request!

# Feel free to add a new adjective!
adjectives = ["brilliant", "overcaffeinated"]

# Add a new type of noun (people, AI terms, Duke references, etc.)
nouns = ["data scientist", "Blue Devil"]

# Add a verb related to coding, AI, or something fun!
verbs = ["debugged", "fine-tuned"]

# Add a cool or recognizable Duke location or tech space
places = ["Co-Lab", "Perkins Library"]

# Add your favorite tool, framework, or AI-related software
tools = ["TensorFlow", "GitHub Copilot"]

# Select one item randomly from each list
adj = random.choice(adjectives)
noun = random.choice(nouns)
verb = random.choice(verbs)
place = random.choice(places)
tool = random.choice(tools)

# Final Madlib sentence – feel free to update this if you add a new category!
print(f"At the {place}, a {adj} {noun} {verb} an AI model using {tool}.")
