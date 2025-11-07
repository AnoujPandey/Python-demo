def original_title(*titles):
    for title in titles:
        print("\nOriginal:", title)
        formatted = title.title()
        print("Formatted:", formatted)

original_title("python PROGRAMMING basics", "THE GREAT GATSBY", "harry potter")
