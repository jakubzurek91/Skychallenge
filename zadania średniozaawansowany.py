"Zad 1"
# def count_chars():
#     word = input("podaj coś").replace(" ","")
#     a = 0
#     b = 0
#     for i in range(len(word)):
#         if word[i].isupper() == True:
#             a+=1
#         else:
#             b+=1
#     print(f"wyraz ma długość {len(word)}, małych liter {b}, dużych {a}")
#
# count_chars()
"Zad 2"
# def ispangram(word):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in str(word).lower():
#             return False
#
#     return True
#
# word = input("podaj coś ")
# print(ispangram(word))

"zad 4"
def anagram(str1, str2):
    return set(str(str1).lower()) == set(str(str2).lower())

print(anagram("Tom Marvolo Riddle", "I am Lord Voldemort"))