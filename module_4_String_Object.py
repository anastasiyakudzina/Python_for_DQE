import re


def count_spaces(text):
    new_raw_text = re.sub(r'[^\w\s]', '', text)
    number_of_space = len(re.findall(r'\W', new_raw_text))
    print("\nNumber of whitespace characters in this text: " + str(number_of_space))


def replace_common_problem(text):
    is_iz = text.lower().replace(' iz ', ' is ')
    delete_tab = is_iz.replace('\t', '')
    add_new_line = delete_tab.replace(':', ':\n\n')
    delete_2_new_line = add_new_line.replace('\n\n\n\n', '\n\n')
    delete_space = delete_2_new_line.replace('\xa0', '')
    add_space = None
    if re.findall(r'\w+[“]', delete_space):
        add_space = delete_space.replace('“', ' “')
    delete_double_space = add_space.replace('  ', ' ')
    delete_space_dot = delete_double_space.replace('. ', '.')
    return delete_space_dot


def create_capitalizing_sentences(text):
    normalize_sentences = []
    for i in text.split('\n'):
        find_sentences = [sentence for sentence in i.split('.')]
        for s in find_sentences:
            capitalize_sentences = s.capitalize()
            normalize_sentences.append(capitalize_sentences)
    return normalize_sentences


def create_last_word_sentence(text):
    last_word_list = []
    for i in text.split('\n'):
        find_sentences = [sentence for sentence in i.split('.')]
        for s in find_sentences:
            capitalize_sentences = s.capitalize()
            last_word_list.append(find_last_word_in_sentence(capitalize_sentences))
    return last_word_list


def find_last_word_in_sentence(capitalize_sentences):
    if len(capitalize_sentences) >= 1:
        if re.findall(r'\W$', capitalize_sentences):
            exclude_punctuation = re.sub(r'[^\w\s]', '', capitalize_sentences)
            word_list = exclude_punctuation.split()
        else:
            word_list = capitalize_sentences.split()
        last_word = word_list[-1]
        return last_word


def add_last_word_sentence_to_text(last_word_list, main_sentences_list):
    not_none_values = [i for i in last_word_list if i is not None]
    last_word_sentence = ' '.join(not_none_values)
    index_empty_value = [i for i, val in enumerate(main_sentences_list) if len(val) == 0]
    main_sentences_list.insert(index_empty_value[4], last_word_sentence)
    return main_sentences_list


def add_dot_and_paragraph_into_text(full_text_list):
    normalize_sentences_with_dot = []
    for c in full_text_list:
        if len(c) >= 1 and len(re.findall(r'\W$', c)) == 0:
            st_new = c + '.'
            normalize_sentences_with_dot.append(st_new)
        else:
            normalize_sentences_with_dot.append(c)
    return ' '.join(normalize_sentences_with_dot).replace('   ', '\n\n\t')


raw_text = """homEwork:
tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. 
"""
prepared_text = replace_common_problem(raw_text)
list_capitalizing_sentence = create_capitalizing_sentences(prepared_text)
list_last_words = create_last_word_sentence(prepared_text)
full_text = add_last_word_sentence_to_text(list_last_words, list_capitalizing_sentence)
text_with_dot_and_paragraph = add_dot_and_paragraph_into_text(full_text)

if __name__ == '__main__':
    count_spaces(raw_text)
    print("\nNormalized text:\n\n" + str(text_with_dot_and_paragraph))
