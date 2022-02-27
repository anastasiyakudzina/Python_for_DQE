import datetime
import time
from random import randint
import os
import os.path
import re
from module_4_String_Object import add_dot_and_paragraph_into_text
from module_4_String_Object import create_capitalizing_sentences


class PublicationFactory:
    @staticmethod
    def get():
        publication_type = int(
            input("Please enter a publication type:\n1 - News, 2 - Advertising, 3 - Horoscope, 4 - Input from file\n"))
        if publication_type == 1:
            return NewsConsole()
        elif publication_type == 2:
            return AdvertisingConsole()
        elif publication_type == 3:
            return HoroscopeConsole()
        elif publication_type == 4:
            input_path = InputPath()
            filepath_input = input_path.get_input_file()
            return BatchPublication(filepath_input)
        raise NameError


class InputPath:
    def __init__(self):
        file_path_type = input("Do you want to choose your own file path?\ny - Yes, n - No\n")
        if file_path_type == "y":
            input_path = input("Please enter your file path (it can be either relative or absolute):\n")
            self.input_filepath = os.path.abspath(input_path)
            # C:\Python_for_DQE\module_6\input.txt
            # module_6\input.txt
        elif file_path_type == "n":
            input_path = 'module_6/input.txt'
            self.input_filepath = os.path.abspath(input_path)
        else:
            raise NameError

    def get_input_file(self):
        return self.input_filepath


class OutputPath:
    def __init__(self):
        success_path = 'module_6/news.txt'
        self.success_filepath = os.path.abspath(success_path)
        os.makedirs(os.path.dirname(self.success_filepath), exist_ok=True)

        current_date = datetime.date.today()
        time_tuple = time.localtime()
        current_time = time.strftime("%H-%M-%S", time_tuple)
        fail_path = 'module_6/fail_' + str(current_date) + '_' + str(current_time) + '.txt'
        self.fail_filepath = os.path.abspath(fail_path)
        os.makedirs(os.path.dirname(self.fail_filepath), exist_ok=True)

    def get_success_file(self):
        return self.success_filepath

    def get_fail_file(self):
        return self.fail_filepath


class PublicationConstructor:
    def __init__(self, text):
        self.body = add_dot_and_paragraph_into_text(create_capitalizing_sentences(text.replace('. ', '.')))

    def get_content(self):
        return self.body


class NewsConstructor(PublicationConstructor):
    def __init__(self, text, city):
        super().__init__(text)
        self.extension = city
        self.date = datetime.datetime.now()

    def get_content(self):
        return "News -------------------------\n" + \
               super().get_content() + "\n" + \
               self.extension + ", " + str(self.date) + "\n" + \
               "------------------------------\n\n"


class NewsConsole(NewsConstructor):
    def __init__(self):
        text = input("Please enter a publication text: ")
        city = input("Please write a city: ")
        super().__init__(text, city)


class AdvertisingConstructor(PublicationConstructor):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.current_date = datetime.date.today()
        self.extension = expiration_date
        self.end_date = datetime.datetime.strptime(self.extension, "%Y-%m-%d").date()
        if self.end_date < self.current_date:
            raise UserWarning("Expiration date must be greater than or equal to current date.")

    def get_content(self):
        diff_date = abs((self.end_date - self.current_date).days)
        return "Advertising-------------------\n" + \
               super().get_content() + "\n" + \
               "Actual until: " + str(self.end_date) + ", " + str(diff_date) + " days left\n" + \
               "------------------------------\n\n"


class AdvertisingConsole(AdvertisingConstructor):
    def __init__(self):
        text = input("Please enter a publication text: ")
        extension = input(
            "Please enter a expiration date in YYYY-MM-DD (must be >= " + str(datetime.date.today()) + "): ")
        super().__init__(text, extension)


class HoroscopeConstructor(PublicationConstructor):
    def __init__(self, text, zodiac):
        super().__init__(text)
        self.extension = zodiac

    def get_content(self):
        probability = randint(10, 100)
        return "Horoscope--------------------\n" + \
               super().get_content() + "\n" + \
               "Zodiac sign: " + str(self.extension) + ", " + str(probability) + "% probability\n" + \
               "------------------------------\n\n"


class HoroscopeConsole(HoroscopeConstructor):
    def __init__(self):
        text = input("Please enter a publication text: ")
        zodiac = input("Please write sign of the zodiac: ")
        super().__init__(text, zodiac)


class BatchPublication:
    def __init__(self, filepath_input):
        self.path = filepath_input

    @staticmethod
    def create_content(blocks):
        header = blocks[0]
        body = blocks[1]
        extension = blocks[2]
        normalize_body = add_dot_and_paragraph_into_text(create_capitalizing_sentences(body))
        if re.match(r'[news]', header.lower()):
            news = NewsConstructor(normalize_body, extension)
            publication = news.get_content()
        elif re.match(r'[adv]', header.lower()):
            adv = AdvertisingConstructor(normalize_body, extension)
            publication = adv.get_content()
        elif re.match(r'[hor]', header.lower()):
            hor = HoroscopeConstructor(normalize_body, extension)
            publication = hor.get_content()
        else:
            raise NameError
        return publication

    @staticmethod
    def split_line(text_line):
        blocks = []
        norm_line = text_line.replace('. ', '.')
        for i in norm_line.split('//'):
            blocks.append(i)
        return blocks

    def get_content(self):
        normalize_news = []
        with open(self.path, encoding="utf8") as fp:
            for line in fp:
                if line == "\n":
                    continue
                line_split = line.strip()
                list_with_line = self.split_line(line_split)
                try:
                    content = self.create_content(list_with_line)
                    normalize_news.append(content)
                except (NameError, IndexError, UserWarning):
                    continue
        return '\n'.join(normalize_news)

    def get_fail_content(self):
        fail_news = []
        with open(self.path, encoding="utf8") as fp:
            for line in fp:
                if line == "\n":
                    continue
                line_split = line.strip()
                list_with_line = self.split_line(line_split)
                try:
                    self.create_content(list_with_line)
                except (NameError, IndexError,  UserWarning):
                    fail_news.append(line_split + "\n")
                    continue
        return ''.join(fail_news)

    def get_processing_result(self):
        count = 0
        fail_count = 0
        with open(self.path, encoding="utf8") as fp:
            for line in fp:
                if line == "\n":
                    continue
                line_split = line.strip()
                list_with_line = self.split_line(line_split)
                count += 1
                try:
                    self.create_content(list_with_line)
                except (NameError, IndexError,  UserWarning):
                    fail_count += 1
                    continue
        success_count = count - fail_count
        print("Total publications: " + str(count) + "\n" +
              "Fail publications: " + str(fail_count) + "\n" +
              "Success publications: " + str(success_count))

        if os.path.exists(self.path) is True and fail_count == 0:
            os.remove(self.path)


class SuccessPublisher:
    @staticmethod
    def success_publish(publication):
        content = publication.get_content()
        success_path = OutputPath()
        with open(success_path.get_success_file(), "a+") as f:
            f.write(content)


class FailPublisher:
    @staticmethod
    def fail_publish(publication):
        content = publication.get_fail_content()
        fail_path = OutputPath()
        with open(fail_path.get_fail_file(), "a+") as f:
            f.write(content)


class ProcessingResultPublisher:
    @staticmethod
    def result_publish(publication):
        publication.get_processing_result()


class Runner:
    @staticmethod
    def run():
        try:
            newsfeed_publication = PublicationFactory.get()
            if isinstance(newsfeed_publication, BatchPublication) is True:
                SuccessPublisher.success_publish(newsfeed_publication)
                FailPublisher.fail_publish(newsfeed_publication)
                ProcessingResultPublisher.result_publish(newsfeed_publication)
            else:
                SuccessPublisher.success_publish(newsfeed_publication)
        except (NameError, ValueError):
            print("Invalid input, please try again.")
        except UserWarning as warn_err:
            print(warn_err.args[0])
        except (FileNotFoundError, TypeError):
            print("No such file or directory.")


Runner.run()
