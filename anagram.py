if sorted(input("First word: ").replace(" ", "").lower()) == sorted(input("Second word: ").replace(" ", "").lower()):
    print("Anagrams")
else:
    print("Not Anagrams")