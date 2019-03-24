import sqlite3

conn = sqlite3.connect('thesaurus.db')
c = conn.cursor()

# c.execute('''CREATE TABLE thesaurus (word varchar(255), synonyms text)''')

with open('thesaurus/moby/mthes/mobythes.aur', 'r') as f:
    for line in f:
        split = tuple(line.replace('\n', "").split(',', 1))
        print(f'{split[0]}: {split[1]}')
        c.execute(f'INSERT INTO thesaurus (word, synonyms) VALUES (?,?)', split)

conn.commit()
