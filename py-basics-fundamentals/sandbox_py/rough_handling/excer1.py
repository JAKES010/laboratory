# squares = []
# for n in range(5):
#     squares.append(n ** 2)
# print(squares)

# squares = [n ** 2 for n in range(5)]
# print(squares)

# numbers = []
# for n in range(11):
#     if n % 2 == 0:
#         numbers.append(n)
# print(numbers)

# result = [num for num in range(11) if num % 2 == 0]
# print(result)
# product = { n: n for n in range(11) if  n % 2 == 0 }
# print(product)

# words = ["apple", "banana", "kiwi", "cherry"]
# value = {n : len(n) for n in words if len(n) > 4 }
# print(value)

text = "the cat and the hat and the bat"
my_dict = {}
for word in text.split():
    if text not in my_dict:
        print(text)