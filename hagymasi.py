
sentences = []


for mondat in range(5):
    sentence = input("Írj be mondatokat!")
    sentences.append(sentence)
    

sentence_with_most_spaces = ''
max_space_count = 0


for sentence in sentences:
    space_count = 0
    for letter in sentence:
        if letter == ' ':
            space_count += 1
            
    if space_count > max_space_count:
        space_count = max_space_count
        sentence_with_most_spaces = sentence


print(f"A legtöbb szóközt tartalmazó mondat: {sentence_with_most_spaces}")
