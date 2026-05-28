# The Scenario: Automation scripts often scrape prices from websites, but they come back as messy text with currency symbols instead of numbers you can calculate.

# The Task: Create a custom function named clean_price(raw_text) that takes a string like "Rs. 1,499" or "Rs. 475", removes the "Rs. " part, removes any commas, and returns just the bare number as a clean string.

# The Output: Call your function inside a print statement using an f-string to display: The calculated numeric price is: {cleaned_value}.



def clean_price(raw_text) :
    cleaned_string = old_string.replace("Rs.", "").replace(",", "").replace(" ", "")
    return cleaned_string

old_string = "Rs. 1,499"
print(f"The calculated numeric price is: {clean_price(old_string)}")