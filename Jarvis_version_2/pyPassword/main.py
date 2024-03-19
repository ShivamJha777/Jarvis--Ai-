import random
def password_generator(nr_letters, nr_numbers, nr_symbols):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    rm_letters = ""
    rm_numbers = ""
    rm_symbols = ""
    for nl in range(nr_letters):
      rm_letters+= random.choice(letters)
    for nn in range(nr_numbers):
      rm_numbers += random.choice(numbers)
    for ns in range(nr_symbols):
      rm_symbols += random.choice(symbols)
    password_list = []
    password_list+= rm_letters+rm_numbers+rm_symbols
    random.shuffle(password_list)
    passwod = ""
    for i in range(len(password_list)):
      passwod += password_list[i]
    print(f"The randomised password is {passwod}")
    return f"The randomised password is {passwod}"

