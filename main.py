while(True):
   words = {
  "РОФЛ": "Шутка",
  "ЩИЩ": "одобрение или восторг",
  "КРИПОВЫЙ": " страшный, пугающий",
  "АГРИТЬСЯ ": "злиться"
  }
word = input("Введите слово: ")
word = word.upper()
if word in words.keys():
    print(words[word])
else:
    print("Слово не нашлось")
