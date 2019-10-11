vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
var = 1
x = True
y = True
gibberish = ""

while (x==True):
    print("This is a gibberish translator")

    while var == 1:
        #User enters sentence and syllables
        original = input("Give me a word please : ")

        syl1 = input("Enter the first syllable: ")

        syl2 = input("Enter the second syllable: ")

        #Check to see if string is valid
        if len(original) <= 2:
            print("Please enter a valid word")
        else:
            var += 2

    #conversion process
    for i in range(len(original)):
        char = original[i]
        gibberish += char
        if char in vowels:
            gibberish += syl1
    print("You originally entered: ", original)
    print("Your new word is: ", gibberish)

    play_again = input("Would you like to play again? y/n: ")
    if play_again == 'n':
        break
    elif play_again == 'y':
        x = True