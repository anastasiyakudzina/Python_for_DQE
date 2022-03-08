import datetime
import time
from random import randint
import os
import os.path
import re
import csv
import json
import xml.etree.ElementTree as ET
from module_4_String_Object import add_dot_and_paragraph_into_text
from module_4_String_Object import create_capitalizing_sentences
from module_4_Collections import merge_dictionary_list


class PublicationFactory:
    @staticmethod
    def get():
        publication_type = int(
            input("Please enter a publication type:\n1 - News, 2 - Advertising, 3 - Horoscope, 4 - Input from .txt "
                  "file, 5 - Input from .json file, 6 - Input from .xml file\n"))
        if publication_type == 1:
            return NewsConsole()
        elif publication_type == 2:
            return AdvertisingConsole()
        elif publication_type == 3:
            return HoroscopeConsole()
        elif publication_type == 4:
            input_path = InputPath()
            filepath_input = input_path.get_txt_input_file()
            return TextPublication(filepath_input)
        elif publication_type == 5:
            input_path = InputPath()
            filepath_input = input_path.get_json_input_file()
            return JSONPublication(filepath_input)
        elif publication_type == 6:
            input_path = InputPath()
            filepath_input = input_path.get_xml_input_file()
            return XMLPublication(filepath_input)
        raise NameError


class InputPath:
    def __init__(self):
        file_path_type = input("Do you want to choose your own file path?\ny - Yes, n - No\n")
        if file_path_type == "y":
            input_path = input("Please enter your file path (it can be either relative or absolute):\n")
            self.txt_input_filepath = os.path.abspath(input_path)
            self.json_input_filepath = os.path.abspath(input_path)
            self.xml_input_filepath = os.path.abspath(input_path)
            # C:\Python_for_DQE\module_6\test.txt
            # module_8\input.json
        elif file_path_type == "n":
            txt_input_path = 'module_7/input.txt'
            self.txt_input_filepath = os.path.abspath(txt_input_path)
            json_input_path = 'module_8/input.json'
            self.json_input_filepath = os.path.abspath(json_input_path)
            xml_input_path = 'module_9/input.xml'
            self.xml_input_filepath = os.path.abspath(xml_input_path)
        else:
            raise NameError

    def get_txt_input_file(self):
        return self.txt_input_filepath

    def get_json_input_file(self):
        return self.json_input_filepath

    def get_xml_input_file(self):
        return self.xml_input_filepath


class OutputPath:
    def __init__(self):
        success_path = 'module_9/news.txt'
        self.success_filepath = os.path.abspath(success_path)
        os.makedirs(os.path.dirname(self.success_filepath), exist_ok=True)

        current_date = datetime.date.today()
        time_tuple = time.localtime()
        current_time = time.strftime("%H-%M-%S", time_tuple)

        fail_path = 'module_9/fail_txt_' + str(current_date) + '_' + str(current_time) + '.txt'
        self.fail_filepath = os.path.abspath(fail_path)
        os.makedirs(os.path.dirname(self.fail_filepath), exist_ok=True)

        fail_json_path = 'module_9/fail_json_' + str(current_date) + '_' + str(current_time) + '.json'
        self.fail_json_filepath = os.path.abspath(fail_json_path)
        os.makedirs(os.path.dirname(self.fail_json_filepath), exist_ok=True)

        fail_xml_path = 'module_9/fail_xml_' + str(current_date) + '_' + str(current_time) + '.xml'
        self.fail_xml_filepath = os.path.abspath(fail_xml_path)
        os.makedirs(os.path.dirname(self.fail_xml_filepath), exist_ok=True)

        csv_words_path = 'module_9/csv_words_' + str(current_date) + '_' + str(current_time) + '.csv'
        self.csv_words_filepath = os.path.abspath(csv_words_path)
        os.makedirs(os.path.dirname(csv_words_path), exist_ok=True)

        csv_letters_path = 'module_9/csv_letters_' + str(current_date) + '_' + str(current_time) + '.csv'
        self.csv_letters_filepath = os.path.abspath(csv_letters_path)
        os.makedirs(os.path.dirname(csv_letters_path), exist_ok=True)

    def get_success_file(self):
        return self.success_filepath

    def get_fail_file(self):
        return self.fail_filepath

    def get_fail_json_file(self):
        return self.fail_json_filepath

    def get_fail_xml_file(self):
        return self.fail_xml_filepath

    def get_csv_words_file(self):
        return self.csv_words_filepath

    def get_csv_letters_file(self):
        return self.csv_letters_filepath


class PublicationConstructor:
    def __init__(self, text):
        self.body = add_dot_and_paragraph_into_text(create_capitalizing_sentences(text.replace('. ', '.')))
        if self.body == "":
            raise ImportWarning

    def get_content(self):
        return self.body


class NewsConstructor(PublicationConstructor):
    def __init__(self, text, city):
        super().__init__(text)
        self.extension = city
        if self.extension == "":
            raise ImportWarning
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
            raise UserWarning

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
        if self.extension == "" or self.extension is None:
            raise ImportWarning

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


class Content:
    def __init__(self, header, body, extension):
        self.header = header
        self.body = body
        self.extension = extension

    def create_content(self):
        normalize_body = add_dot_and_paragraph_into_text(create_capitalizing_sentences(self.body))
        if re.search(r'\bnew\w+', self.header.lower()) or re.search(r'\bnew$', self.header.lower()):
            news = NewsConstructor(normalize_body, self.extension)
            publication = news.get_content()
        elif re.search(r'\badv\w+', self.header.lower()) or re.search(r'\badv$', self.header.lower()):
            adv = AdvertisingConstructor(normalize_body, self.extension)
            publication = adv.get_content()
        elif re.search(r'\bhor\w+', self.header.lower()) or re.search(r'\bhor$', self.header.lower()):
            hor = HoroscopeConstructor(normalize_body, self.extension)
            publication = hor.get_content()
        else:
            raise NameError
        return publication


class TextPublication:
    def __init__(self, filepath_input):
        self.path = filepath_input

    @staticmethod
    def create_content(blocks):
        header = blocks[0]
        body = blocks[1]
        extension = blocks[2]
        content = Content(header, body, extension)
        return content.create_content()

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
                except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError):
                    continue
        return ''.join(normalize_news)

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
                except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError):
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
                except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError):
                    fail_count += 1
                    continue
        success_count = count - fail_count
        print("Total publications: " + str(count) + "\n" +
              "Fail publications: " + str(fail_count) + "\n" +
              "Success publications: " + str(success_count))

        if os.path.exists(self.path) is True and fail_count == 0:
            os.remove(self.path)


class JSONPublication:
    def __init__(self, filepath_input):
        self.path = filepath_input

    @staticmethod
    def create_content(diction):
        header = diction.get('header')
        body = diction.get('text').replace('. ', '.')
        extension = diction.get('extension')
        content = Content(header, body, extension)
        return content.create_content()

    def get_content(self):
        normalize_news = []
        with open(self.path, "r") as content:
            input_json = json.load(content)
            if isinstance(input_json, list):
                for dictionary in input_json:
                    try:
                        content = self.create_content(dictionary)
                        normalize_news.append(content)
                    except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                        continue
            if isinstance(input_json, dict):
                try:
                    content = self.create_content(input_json)
                    normalize_news.append(content)
                except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                    pass
        return ''.join(normalize_news)

    def get_fail_content(self):
        fail_news = []
        with open(self.path, "r") as content:
            input_json = json.load(content)
            if isinstance(input_json, list):
                for dictionary in input_json:
                    try:
                        self.create_content(dictionary)
                    except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                        fail_news.append(dictionary)
                        continue
            if isinstance(input_json, dict):
                try:
                    self.create_content(input_json)
                except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                    fail_news.append(input_json)
        return fail_news

    def get_processing_result(self):
        count = 0
        fail_count = 0
        with open(self.path, "r") as content:
            input_json = json.load(content)
            if isinstance(input_json, list):
                for dictionary in input_json:
                    count += 1
                    try:
                        self.create_content(dictionary)
                    except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                        fail_count += 1
                        continue
            if isinstance(input_json, dict):
                count += 1
                try:
                    self.create_content(input_json)
                except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                    fail_count += 1
        success_count = count - fail_count
        print("Total publications: " + str(count) + "\n" +
              "Fail publications: " + str(fail_count) + "\n" +
              "Success publications: " + str(success_count))

        if os.path.exists(self.path) is True and fail_count == 0:
            os.remove(self.path)


class XMLPublication:
    def __init__(self, filepath_input):
        self.path = filepath_input

    @staticmethod
    def create_content(blocks):
        header = blocks[0]
        body = blocks[1].replace('. ', '.')
        extension = blocks[2]
        content = Content(header, body, extension)
        return content.create_content()

    def get_content(self):
        normalize_news = []
        xml_file = ET.parse(self.path)
        root = xml_file.getroot()
        for news in root:
            blocks = [list(news.attrib.values())[0]]
            for j in news:
                blocks.append(j.text)
            try:
                content = self.create_content(blocks)
                normalize_news.append(content)
            except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                continue
        return ''.join(normalize_news)

    def get_fail_content(self):
        tree = None
        xml_file = ET.parse(self.path)
        root = xml_file.getroot()
        new_root = ET.Element(f"{root.tag}")
        for news in root:
            blocks = [list(news.attrib.values())[0]]
            for j in news:
                blocks.append(j.text)
            try:
                self.create_content(blocks)
            except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
                new_root.insert(0, news)
                tree = ET.ElementTree(new_root)
                continue
        return tree

    def get_processing_result(self):
        count = 0
        fail_count = 0
        xml_file = ET.parse(self.path)
        root = xml_file.getroot()
        for news in root:
            blocks = [list(news.attrib.values())[0]]
            for j in news:
                blocks.append(j.text)
            count += 1
            try:
                self.create_content(blocks)
            except (NameError, ValueError, IndexError, UserWarning, ImportWarning, TypeError, AttributeError):
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
        if len(content) > 0:
            success_path = OutputPath()
            with open(success_path.get_success_file(), "a+") as f:
                f.write(content)


class WordsCSVPublisher:
    @staticmethod
    def words_csv_writer(publication):
        content = publication.get_content()
        if len(content) > 0:
            txt = re.findall(r'\w+', content.lower())
            word_dict = dict(zip(txt, [txt.count(i) for i in txt]))
            output_path = OutputPath()
            with open(output_path.get_csv_words_file(), 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter="-")
                for key, value in word_dict.items():
                    writer.writerow([key, value])


class LettersCSVPublisher:
    @staticmethod
    def list_of_dict_upper_lower_case(text):
        txt = re.sub(r'[^\w-]', '', text)
        lowercase_letters = []
        uppercase_letters = []
        for i in txt:
            if i.islower():
                lowercase_letters.append(i)
            if i.isupper():
                uppercase_letters.append(i.lower())

        lowercase_dict = dict(zip(lowercase_letters, [lowercase_letters.count(i) for i in lowercase_letters]))
        uppercase_dict = dict(zip(uppercase_letters, [uppercase_letters.count(i) for i in uppercase_letters]))

        mylist = [lowercase_dict.copy(), uppercase_dict.copy()]
        return mylist

    @staticmethod
    def count_all_symbols_in_text(text):
        return len(list(text))

    @staticmethod
    def add_letters_to_csv(csv_path, input_json, count_all_text):
        with open(csv_path, 'a+', newline='', encoding='utf-8') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for key, value in input_json.items():
                not_none_values = [0 if v is None else v for v in value]
                count_lower = not_none_values[0]
                count_upper = not_none_values[1]
                count_all = count_lower + count_upper
                percentage = round((count_all * 100 / count_all_text), 2)
                writer.writerow(
                    {'letter': key, 'count_all': count_all, 'count_uppercase': count_upper, 'percentage': percentage})

    def letters_csv_writer(self, publication):
        content = publication.get_content()
        if len(content) > 0:
            letters_list = self.list_of_dict_upper_lower_case(content)
            count = self.count_all_symbols_in_text(content)
            dict_with_list = merge_dictionary_list(letters_list)
            output_path = OutputPath()
            self.add_letters_to_csv(output_path.get_csv_letters_file(), dict_with_list, count)


class FailPublisher:
    @staticmethod
    def fail_publish(publication):
        content = publication.get_fail_content()
        if len(content) > 0:
            fail_path = OutputPath()
            with open(fail_path.get_fail_file(), "a+") as f:
                f.write(content)


class FailJSONPublisher:
    @staticmethod
    def fail_json_publish(publication):
        content = publication.get_fail_content()
        if len(content) > 0:
            fail_json_path = OutputPath()
            with open(fail_json_path.get_fail_json_file(), "w") as f:
                if len(content) > 1:
                    json.dump(content, f, indent=4)
                elif len(content) == 1:
                    json.dump(content[0], f, indent=4)


class FailXMLPublisher:
    @staticmethod
    def fail_xml_publish(publication):
        content = publication.get_fail_content()
        if content is not None:
            fail_xml_path = OutputPath()
            content.write(fail_xml_path.get_fail_xml_file())


class ProcessingResultPublisher:
    @staticmethod
    def result_publish(publication):
        publication.get_processing_result()


class Runner:
    @staticmethod
    def run():
        try:
            newsfeed_publication = PublicationFactory.get()
            if isinstance(newsfeed_publication, TextPublication) is True:
                SuccessPublisher.success_publish(newsfeed_publication)
                WordsCSVPublisher.words_csv_writer(newsfeed_publication)
                letters_csv = LettersCSVPublisher()
                letters_csv.letters_csv_writer(newsfeed_publication)
                FailPublisher.fail_publish(newsfeed_publication)
                ProcessingResultPublisher.result_publish(newsfeed_publication)
            elif isinstance(newsfeed_publication, JSONPublication) is True:
                SuccessPublisher.success_publish(newsfeed_publication)
                WordsCSVPublisher.words_csv_writer(newsfeed_publication)
                letters_csv = LettersCSVPublisher()
                letters_csv.letters_csv_writer(newsfeed_publication)
                FailJSONPublisher.fail_json_publish(newsfeed_publication)
                ProcessingResultPublisher.result_publish(newsfeed_publication)
            elif isinstance(newsfeed_publication, XMLPublication) is True:
                SuccessPublisher.success_publish(newsfeed_publication)
                WordsCSVPublisher.words_csv_writer(newsfeed_publication)
                letters_csv = LettersCSVPublisher()
                letters_csv.letters_csv_writer(newsfeed_publication)
                FailXMLPublisher.fail_xml_publish(newsfeed_publication)
                ProcessingResultPublisher.result_publish(newsfeed_publication)
            else:
                SuccessPublisher.success_publish(newsfeed_publication)
                WordsCSVPublisher.words_csv_writer(newsfeed_publication)
                letters_csv = LettersCSVPublisher()
                letters_csv.letters_csv_writer(newsfeed_publication)
        except (NameError, ValueError) as name_err:
            print(f"Invalid input, please try again. {name_err}")
        except UserWarning as warn_err:
            print(f"Expiration date must be greater than or equal to current date. {warn_err}")
        except (FileNotFoundError, TypeError) as file_err:
            print(f"No such file or directory. {file_err}")
        except ImportWarning as none_err:
            print(f"Input can't be empty. {none_err}")


Runner.run()
