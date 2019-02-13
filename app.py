import requests
import itertools

API_URL = 'https://owlbot.info/api/v2/dictionary/'
# user_in_string = input("Enter words separated by a space: ")

input_list = ['acronym', 'creator', 'tool']  # [word.strip() for word in user_in_string.split()]
print(input_list)

# Creates the dictionary where the synonyms will be linked to the inputted term.
linked_synonyms = {}

# gets the json data from thesaurus and parses through the output for the synonyms before adding them to a dict
for word in input_list:
    synonym_list = []
    r = requests.get(f'https://tuna.thesaurus.com/pageData/{word}')
    for synonym in r.json()['data']['definitionData']['definitions'][0]['synonyms']:
        synonym_list.append(synonym['term'])
    linked_synonyms[word] = synonym_list

print(linked_synonyms)

# Takes each synonym value and finds the product of all the rest.
# TODO: include the original user terms in the itertools.product
product_of_all_synonyms = list(itertools.product(linked_synonyms['acronym'], linked_synonyms['creator'], linked_synonyms['tool']))

# Inputs a list of synonyms in sets of 3 and slices them according to a desired count.
# TODO: Refactor to allow for more than than 3 terms.
def sliced_synonym(list_of_synonyms, count):
    concatenated_synonyms = {}
    for term in list_of_synonyms:
        sliced = term[0][:count] + term[1][:count] + term[2][:count]
        concatenated_synonyms[sliced] = term
    return concatenated_synonyms


single_sliced = sliced_synonym(product_of_all_synonyms, 1)
double_sliced = sliced_synonym(product_of_all_synonyms, 2)
triple_sliced = sliced_synonym(product_of_all_synonyms, 3)

print(single_sliced)
print(double_sliced)
print(triple_sliced)


def dictionary_check(created_words):
    checked_words = {}
    for key in created_words.keys():
        s = requests.get(API_URL + key)
        if not s.json():
            print(f'{key} is not a word.')
            continue
        print(f'{key} is an English word.')
        checked_words[key] = created_words[key]
    return checked_words


check1 = dictionary_check(single_sliced)
check2 = dictionary_check(double_sliced)
check3 = dictionary_check(triple_sliced)
print(check1)

# TODO: review why these two print empty dictionaries.
print(check2)
print(check3)
