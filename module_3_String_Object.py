import re

raw_text = """homEwork:
tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. 
"""

# Exclude all punctuation
new_raw_text = re.sub(r'[^\w\s]', '', raw_text)
# Count all spaces. \W - not word characters (without punctuation - it's spaces)
number_of_space = len(re.findall(r'\W', new_raw_text))

print("Number of whitespace characters in this text: " + str(number_of_space))

# Replacement actions
is_iz = raw_text.lower().replace(' iz ', ' is ')
delete_tab = is_iz.replace('\t', '')
# Add '\n\n' after ':' for defining new paragraph
add_new_line = delete_tab.replace(':', ':\n\n')
delete_space = add_new_line.replace('\xa0', '')

# If word + "" is written together, then split them
add_space = None
if re.findall(r'\w+[“]', delete_space):
    add_space = delete_space.replace('“', ' “')

delete_double_space = add_space.replace('  ', ' ')
delete_space_dot = delete_double_space.replace('. ', '.')

# Create empty list for normalize sentences
normalize_sentences = []
# Create empty list for sentence with last words of each existing sentences
last_word_list = []

# Iterate text, find '\n\n' as marker of paragraph and split. After splitting one of the '\n' will be removed
for i in delete_space_dot.split('\n'):
    # Create list with sentences of each paragraph. '.' - marker of sentence. After splitting '.' will be removed
    find_sentences = [sentence for sentence in i.split('.')]
    for s in find_sentences:
        # Iterate list with sentences and capitalize each of them
        capitalize_sentences = s.capitalize()
        # Find sentences with length > = 1.
        # If last word in the sentence contains punctuation after it, then exclude punctuation.
        if len(capitalize_sentences) >= 1:
            if re.findall(r'\W$', capitalize_sentences):
                exclude_punctuation = re.sub(r'[^\w\s]', '', capitalize_sentences)
                word_list = exclude_punctuation.split()
            else:
                word_list = capitalize_sentences.split()
            last_word = word_list[-1]
            last_word_list.append(last_word)
        # Two empty values in the list are marker of new paragraph
        # (1st paragraph -> ['Homework:', '', '', 'This is your homework'] <- 2nd paragraph)
        normalize_sentences.append(capitalize_sentences)

# Collect last words in the sentence
last_word_sentence = ' '.join(last_word_list)
# We need to add sentence with last words of each existing sentences after 3rd paragraph
# (if 'Homework:' is 1st paragraph)
# Two empty values in the list are marker of new paragraph
# 1st paragraph '1', '2', 2nd paragraph '3', '4', 3rd paragraph '5', '6',
# It means that we should find the fifth empty value and add sentence before it
index_empty_value = [i for i, val in enumerate(normalize_sentences) if len(val) == 0]
# Insert sentence with last words of each existing sentences after 3rd paragraph
normalize_sentences.insert(index_empty_value[4], last_word_sentence)
# adding a sentence to the end of the text looks much better:
# normalize_sentences.append(last_word_sentence)

# Add dots and collect sentences in the list
normalize_sentences_with_dot = []
for c in normalize_sentences:
    # Check if we don't have another punctuation before adding dot
    if len(c) >= 1 and len(re.findall(r'\W$', c)) == 0:
        st_new = c + '.'
        normalize_sentences_with_dot.append(st_new)
    else:
        normalize_sentences_with_dot.append(c)

# Collect all sentences in the text. 3 spaces are marker of new paragraph
normalize_text = ' '.join(normalize_sentences_with_dot).replace('   ', '\n\n\t')
print("\nNormalized text:\n\n" + str(normalize_text))
