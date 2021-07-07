with open("XYZ.txt") as f:
    text = f.read()
    print(text.count('Y'), "- number of characters Y")
    print(text.count('Z'), "- number of characters Z")

