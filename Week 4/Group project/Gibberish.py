#Assignment 1: Gibberish game
#Written by Hugh O'Carroll-Macri, C17316046
#11/10/2019
x = True
while (x==True):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    var = 1
    y = True
    gibberish = ""

    #Explanation of the rules
    print("You must enter a sentence and then you will be asked to enter two syllables,")
    print("the first vowel in your sentence will have your first syllable added on to it,")
    print("after that each vowel will be replaced by your second syllable and then your new")
    print("gibberish word will be presented to you")

    while var == 1:
        #User enters sentence and syllables
        original = input("Please enter your sentence: ")

        syl1 = input("Enter the first syllable: ")

        syl2 = input("Enter the second syllable: ")

        #Check to see if string is valid
        if len(original) <= 2:
            print("Please enter a valid word")
        else:
            var += 2

    #First vowel has first syllable added onto it
    for i in range(len(original)):
        char = original[i]
        gibberish += char
        if char in vowels:
            gibberish += syl1
            x = i + 1
            break

    #Every other vowel gets the second syllable added to it
    for i in range(x, len(original)):
        char = original[i]
        gibberish += char
        if char in vowels:
            gibberish += syl2

    #Presenting original and new sentence
    print("You originally entered: ", original)
    print("Your new word is: ", gibberish)

    play_again = input("Would you like to play again? y/n: ")
    if play_again == 'n':
        break
    elif play_again == 'y':
        x = True