import requests

# user_in_string = input("Enter words separated by a space: ")

input_list = ['acronym', 'creator', 'tool']# [word.strip() for word in user_in_string.split()]
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
