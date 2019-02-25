"""
# repeats elements in seq, dup times in a new list
seq = [1,'hello', 3]
def stutter(seq, dup):
    b = list()
    for i in range(len(seq)):
        for x in range(0,dup):
            b.append(seq[i])
    return b
print(stutter(seq,4))
"""

def longest_without_repeat(text):
    global no_repeat_strings_set
    no_repeat_strings_set = set()
    character_check_set = set()
    for i in range(0,len(text)-1,1):
        character_check_set = set()
        character_check_set.add(text[i])
        j = i
        while (j + 1 < len(text)) and (text[j+1] not in character_check_set):
            character_check_set.add(text[j+1])
            j += 1
        no_repeat_strings_set.add(text[i:j+1])
    global longest_string
    longest_string = ""
    for strings in no_repeat_strings_set:
        if len(strings) > len(longest_string):
            longest_string = strings
    return longest_string
longest_without_repeat("nowisthetimeforallgoodmentocomeinaidfortheircountry")
print(f"The longest substring that does not have repeated characters \
in the entered string is '{longest_string}' and it is {len(longest_string)} characters long.")