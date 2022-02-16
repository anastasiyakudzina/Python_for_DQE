import datetime
from random import randint


class PublicationFactory:
    @staticmethod
    def get():
        publication_type = int(input("Please enter a publication type:\n1 - News, 2 - Advertising, 3 - Horoscope\n"))
        if publication_type == 1:
            return News()
        elif publication_type == 2:
            return Advertising()
        elif publication_type == 3:
            return Horoscope()
        raise NameError


class Publication:
    def __init__(self):
        self.text = input("Please enter a publication text: ")

    def get_content(self):
        return self.text


class News(Publication):
    def __init__(self):
        super(News, self).__init__()
        self.city = input("Please write a city: ")
        self.date = datetime.datetime.now()

    def get_content(self):
        return "News -------------------------\n" + \
               super(News, self).get_content() + "\n" + \
               self.city + ", " + str(self.date) + "\n" + \
               "------------------------------\n\n"


class Advertising(Publication):
    def __init__(self):
        super(Advertising, self).__init__()
        self.current_date = datetime.date.today()
        expiration_year = int(input("Please enter a expiration year (must be >= " + str(self.current_date.year) + "): "))
        expiration_month = int(input("Please enter a expiration month (must be >= " + str(self.current_date) + "): "))
        expiration_day = int(input("Please enter a expiration day (must be >= " + str(self.current_date) + "): "))
        self.expiration_date = datetime.date(expiration_year, expiration_month, expiration_day)
        if self.expiration_date < self.current_date:
            raise UserWarning("Expiration date must be greater than or equal to current date.")

    def get_content(self):
        diff_date = abs((self.expiration_date - self.current_date).days)
        return "Advertising-------------------\n" + \
               super(Advertising, self).get_content() + "\n" + \
               "Actual until: " + str(self.expiration_date) + ", " + str(diff_date) + " days left\n" + \
               "------------------------------\n\n"


class Horoscope(Publication):
    def __init__(self):
        super(Horoscope, self).__init__()
        self.zodiac = input("Please write sign of the zodiac: ")

    def get_content(self):
        probability = randint(10, 100)
        return "Horoscope--------------------\n" + \
               super(Horoscope, self).get_content() + "\n" + \
               "Zodiac sign: " + str(self.zodiac) + ", " + str(probability) + "% probability\n" + \
               "------------------------------\n\n"


class Publisher:
    @staticmethod
    def publish(publication):
        content = publication.get_content()
        file_path = open("C:/Users/Anastasiya_Kudzina1/Desktop/news.txt", "a+")
        file_path.write(content)
        file_path.close()


class Runner:
    @staticmethod
    def run():
        try:
            newsfeed_publication = PublicationFactory.get()
            Publisher.publish(newsfeed_publication)
        except NameError:
            print("Unknown publication type, please try again.")
        except ValueError:
            print("Invalid input, please try again.")
        except UserWarning as warn_err:
            print(warn_err.args[0])


Runner.run()
