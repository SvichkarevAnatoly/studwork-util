import os.path
import datetime


class Logger(object):
    def __init__(self):
        self.folder = "log/"
        time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
        extension = ".log"
        self.logFile = os.path.join(self.folder, time + extension)
        self.logMsg = ""

    def log(self, msg):
        self.logMsg += str(msg) + '\n'

    def save(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        with open(self.logFile, "w") as textFile:
            textFile.write(self.logMsg)


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

    # логирование
    logger = Logger()
    logger.log("prices: " + ', '.join(str(x) for x in prices))
    logger.log("ratings: " + ', '.join(str(x) for x in ratings))
    logger.log("personRating: " + str(personRating))

    # сбор статистики
    amountPriceRating, amountRating = accumulateStatistics(prices, ratings)

    # вычисление оптимальной цены
    optimalPrice = computeOptimalPrice(personRating, amountPriceRating, amountRating)
    logger.log("optimal price: " + str(optimalPrice))

    print("Оптимальная цена: ", optimalPrice)
    logger.save()
