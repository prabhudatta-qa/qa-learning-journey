# The Scenario: In Playwright automation, passing a URL with uppercase characters (like HTTPS://GOOGLE.COM) can sometimes break browser navigation scripts.

# The Task:

# Define a variable inside a main function containing a mixed-case URL: target_url = "Https://GitHub.Com/Prabhudatta-QA".

# Try to print that variable from outside your function to see what error Python throws (to test your understanding of Scope).

# Fix the scope error, convert the URL completely to lowercase, and swap out "github.com" with "gitlab.com" using a string method.



def main():
    target_url = "Https://GitHub.Com/Prabhudatta-QA".replace("Github.Com", "gitlab.com").replace("Https://", "https://")
    print(target_url) 