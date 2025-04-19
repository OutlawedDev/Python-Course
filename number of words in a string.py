text = "this is a program to count the words in this text"

word_count = 0

words = text.split()

for word in words:
    word_count+=1

print("number of words in this string are", word_count)