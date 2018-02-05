sentence = input("Enter a sentence: ")
word = input("Enter word to replace: ")
replace = input("Enter replacement word: ")
n = sentence.find(word)
length = len(word)
if n <= -1:
	print("ERROR: Word is not in your sentence")
else:
	print(sentence[:n] + replace + sentence[n+length:])
