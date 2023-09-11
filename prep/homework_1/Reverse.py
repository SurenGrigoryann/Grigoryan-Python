word = input("Your word > ")
# getting the user's word
reverse_word = ''
# reverse word variabke

for i in range(len(word)):
  reverse_word += word[-i-1]
  # getting the reverse word

print(reverse_word)

if word == reverse_word:
  # checking palindrome
  print(f"{word} is a palindrome!")
else:
  print(f"{word} is not a palindrome!")
  
# end if
