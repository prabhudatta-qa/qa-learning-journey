# The Scenario: When testers type a developer's name into a bug tracking system, they often accidentally leave trailing spaces, mess up the capitalization, or hit Enter too early.

# The Task: Prompt the user for their full name using input(). Clean up the input so that if they type something messy like "   pRaBhuDaTta   ", your program outputs a perfectly cleaned string: "Prabhudatta".

# Constraint: You must chain at least two string methods together on a single line of code to do the cleaning.


name = input("What's Your Name?").strip().title()
print("Hello,", name)