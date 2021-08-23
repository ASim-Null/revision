# Remove fruits from basket2 that are present in basket1
for item in basket1:
    if item in basket2:
        basket2.remove(item)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

# Transfer fruits from basket1 to basket2
while len(basket1)>len(basket2):
    item_to_transfer = basket1.pop()
    basket2.append(item_to_transfer)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

#Operations on sets - all items which are in XX and XY:

#Storing Data in a Dictionary:
#Calculate the value of z coordinates using the coordinates of x and y:
circ_parab = dict()


    for x in range_x:
        for y in range_y:        
            # Calculate the value for z
            z = x**2 + y**2
            # Create a new key for the dictionary
            key = (x,y)
            # Create a new key-value pair      
            circ_parab[x,y] = z
        
 """
 String indexing and concatenation

You are presented with one of the earliest known encryption techniques - Caesar cipher. It is based on a simple shift of each letter in a message by a certain number of positions down the given alphabet. For example, given the English alphabet, a shift of 1 for 'xyz' would imply 'yza' and vice versa in case of decryption. Notice that 'z' becomes 'a' in this case.

Thus, encryption/decryption requires two arguments: text and an integer key denoting the shift (key = 1 for the example above).

Your task is to create an encryption function given the English alphabet stored in the alphabet string.
"""

def encrypt(text, key):
  
    encrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]

    return encrypted_text

# Check the encryption function with the shift equals to 10
print(encrypt("datacamp", 10))

"""
You are given the variable text storing the following string 'StRing ObJeCts haVe mANy inTEResting pROPerTies'.

Your task is to modify this string in such a way that would result in 'string OBJECTS have MANY interesting PROPERTIES' 
(every other word in text is uppercased and lowercased, otherwise). You will obtain this result in three steps.

"""

# Create a word list from the string stored in text
word_list = text.split()

for i in range(len(word_list)):
    if (i +1) % 2 == 0:
        word_list[i] = word_list[i].upper()
    else:
        word_list[i] = word_list[i].lower()
new_text= ' '.join(word_list)
print(new_text)

"""

Fixing string errors in a DataFrame

You are given the heroes dataset containing the information on different comic book heroes. However, you'll need to make some refinements in order to use this dataset further.

Comparing Eye color, Hair color, and Skin color columns, you can see that strings in the Hair color columns are capitalized, whereas in other two the strings are lowercased.

Moreover, some rows in the Gender column contain a spelling error (Fmale instead of Female).

Your task is to make the strings in the Hair column lowercased and to fix the spelling error in the Gender column.

"""
# Make all the values in the 'Hair color' column lowercased
heroes['Hair color'] = heroes['Hair color'].str.lower()
  
# Check the values in the 'Hair color' column
print(heroes['Hair color'].value_counts())

# Substitute 'Fmale' with 'Female' in the 'Gender' column
heroes['Gender'] = heroes['Gender'].str.replace('Fmale','Female')

# Check if there is no occurences of 'Fmale'
print(heroes['Gender'].value_counts())
