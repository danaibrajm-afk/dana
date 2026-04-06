correct_words= {"привет","мир","программа","pyton"}
word= input("введите слова:").lower()
if word in correct_words:
    print("слова правильное")
else:
    print("слова неправильное")
