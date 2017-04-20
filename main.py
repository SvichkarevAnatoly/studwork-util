def inputStatistics():
    ratings = list()
    prices = list()

    i = 0
    price = 1
    while price != 0:
        print("Исполнитель ", i + 1, ":", sep="")
        price = input("Введите предлагаемую цену: ")
        if not price:
            print("Конец ввода")
            print()
            break
        price = int(price)
        rating = int(input("Введите рейтинг: ")) + 1
        prices.append(price)
        ratings.append(rating)
        i += 1
        print()

    return prices, ratings


def inputPersonRating():
    # с псевдоотчётом
    return int(input("Ваш рейтинг: ")) + 1


def accumulateStatistics(prices, ratings):
    amountPriceRating = 0
    amountRating = 0
    for price, rating in zip(prices, ratings):
        # рейтинг может быть 0, поэтому псевдоотчёты
        amountPriceRating += (rating + 1) * price
        amountRating += (rating + 1)
    return amountPriceRating, amountRating


def computeOptimalPrice(personRating, amountPriceRating, amountRating):
    optimalPrice = (((amountPriceRating * (amountRating + personRating))
                     / amountRating) - amountPriceRating) / personRating
    return int(optimalPrice)


if __name__ == "__main__":
    # считывание данных
    prices, ratings = inputStatistics()
    personRating = inputPersonRating()

    # сбор статистики
    amountPriceRating, amountRating = accumulateStatistics(prices, ratings)

    # вычисление оптимальной цены
    optimalPrice = computeOptimalPrice(personRating, amountPriceRating, amountRating)

    print("Оптимальная цена: ", optimalPrice)
