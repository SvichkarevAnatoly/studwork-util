ratings = list()
prices = list()

i = 0
price = 1
while price != 0:
    print("Исполнитель ", i + 1, ":", sep="")
    price = int(input("Введите предлагаемую цену: "))
    rating = int(input("Введите рейтинг: ")) + 1
    prices.append(price)
    ratings.append(rating)
    i += 1
    print()
prices.pop()
ratings.pop()

# print(prices)
# print(ratings)

amount = 0
amountRating = 0
for price, rating in zip(prices, ratings):
    amount += rating * price
    amountRating += rating

polinaRating = int(input("Рейтинг Полины: "))

optPrice = (((amount * (amountRating + polinaRating)) / amountRating) - amount) / polinaRating
print("Оптимальная цена: ", amount / amountRating)
