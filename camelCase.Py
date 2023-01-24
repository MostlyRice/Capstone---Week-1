"""
Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser". 

Optional extra question: print a warning message if the input will not produce a valid variable name. You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code. 

"""

def banner():
    """ Display program name """ # triple quotes are doc strings
    message = 'Awesome camelCase Program!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

banner()

def main():
    sentence = input('Enter a short sentence to convert to camel case: ')
    sample_special_characters = ['#','+','"'] 

    list_of_words = sentence.split() 
    for special_character in sample_special_characters:
        if special_character in sentence: 
            print("It contains invalid special characters") 
    
    if(list_of_words[0].isdigit()): 
        print("The sentence starts with a number, the name will not be a valid variable name") 
    
    for index,word in enumerate(list_of_words): 
        if index == 0: 
            camel_case = word.lower() 
        else:
            camel_case += word.capitalize() 
    
    print(f'{sentence} in camel case: {camel_case}') 

main()