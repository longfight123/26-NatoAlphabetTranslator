# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas as pd
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
"""

This script translates a user typed word and
creates a list of phonetic code words.

This script requires that 'pandas' be installed within the Python
environment you are running this script in.

"""

#TODO 1. Create a dictionary in this format:

import pandas as pd

dataframe = pd.read_csv('./nato_phonetic_alphabet.csv')
NATO_dict = {row['letter']:row['code'] for index, row in dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def translate_to_phonetic():
    """Takes a user input and translates to phonetic
    code words.

    Prints a list of the phonetic code words.
    """
    word = input('What is the word?').upper()
    try:
        NATO_list = [NATO_dict[character] for character in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        translate_to_phonetic()
    else:
        print(NATO_list)

translate_to_phonetic()