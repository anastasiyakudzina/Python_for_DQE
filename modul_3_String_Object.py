import re

raw_text = """homEwork:
tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. 
"""

new_raw_text = re.sub(r'[^\w\s]', '', raw_text)
number_of_space = len(re.findall(r'\W', new_raw_text))

print("Number of whitespace characters in this text: " + str(number_of_space))

is_iz = raw_text.lower().replace(' iz ', ' is ')
delete_tab = is_iz.replace('\t', '')
add_new_line = delete_tab.replace(':', ':\n\n')
delete_space = add_new_line.replace('\xa0', '')

add_space = None
if re.findall(r'\w+[“]', delete_space):
    add_space = delete_space.replace('“', ' “')

delete_double_space = add_space.replace('  ', ' ')
delete_space_dot = delete_double_space.replace('. ', '.')

normalize_sentences = []
last_word_list = []

for i in delete_space_dot.split('\n'):
    find_sentences = [sentence for sentence in i.split('.')]
    for s in find_sentences:
        capitalize_sentences = s.capitalize()
        if len(capitalize_sentences) >= 1 and re.findall(r'\w+$', capitalize_sentences):
            word_list = capitalize_sentences.split()
            last_word = word_list[-1]
            last_word_list.append(last_word)
        elif len(capitalize_sentences) >= 1 and re.findall(r'\W$', capitalize_sentences):
            exclude_punctuation = capitalize_sentences.split(str((re.findall(r'\W$', capitalize_sentences))[0]))[0]
            word_list = exclude_punctuation.split()
            last_word = word_list[-1]
            last_word_list.append(last_word)

        normalize_sentences.append(capitalize_sentences)

last_word_sentence = ' '.join(last_word_list)
normalize_sentences.insert(8, last_word_sentence)
# adding a sentence to the end of the text looks much better:
# normalize_sentences.append(last_word_sentence)

normalize_sentences_with_dot = []
for c in normalize_sentences:
    if len(c) >= 1 and c.find(":") == -1:
        st_new = c + '.'
        normalize_sentences_with_dot.append(st_new)
    else:
        normalize_sentences_with_dot.append(c)

normalize_text = ' '.join(normalize_sentences_with_dot).replace('   ', '\n\n\t')
print("\n\nNormalized text:\n\n" + str(normalize_text))
