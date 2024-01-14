text = ["hello", "world", "good", "morning", "good", "afternoon", "good", "evening", "good", "night"]

for i in range(round(len(text) / 3)):
    for j in range(3):
        word = text[i * 3 + j]
        print(f"{word: ^10}", end="")
    print()