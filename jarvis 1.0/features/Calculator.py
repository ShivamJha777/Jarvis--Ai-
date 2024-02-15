import win32com.client
import speech_recognition as sr
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.energy_threshold = 500
        audio = r.listen(source)
        try:
            say('Recognizing')
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}\n')
            return query.lower()
        except Exception as e:
            return 'Some Error Occurred. Sorry from Jarvis'
def calculator():
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2


    should_continue = True
    say('Boss what is the first number you would like to calculate with?Please only say the number you would like to calculate with')
    print('Boss what is the first number you would like to calculate with?Please only say the number you would like to calculate with')
    num1 = take_command()
    try:
        num1 = float(num1)
    except:
        say('Sorry Boss,Some Error Occurred,You will have to maunally write down the number')
        num1 = float(input('Enter the second number you would like to calculate with'))
    while should_continue:
        say('Boss what would you like to do? Multiplication ,division,subtraction or addition?Please only say one of the terms I mentioned right now')
        print('Boss what would you like to do? Multiplication ,division,subtraction or addition?Please only say one of the terms I mentioned right now')
        operation = take_command()
        operation = operation.replace('jarvis','')
        operation = operation.replace('I want to do', '')
        operation = operation.replace('I would like to do', '')
        say('Boss what is the second number you would like to calculate with?Please only say the number you would like to calculate with')
        num2 = take_command()
        try:
            num2 = float(num2)
        except:
            say('Sorry Boss,Some Error Occurred,You will have to maunally write down the number')
            num2 = float(input('Enter the second number you would like to calculate with'))
        if operation == 'multiplication':
            result = multiply(num1,num2)
            say(f'Boss {num1} * {num2} = {result}')
            print(f'Boss {num1} * {num2} = {result}')
        if operation == 'division':
            result = divide(num1,num2)
            say(f'Boss {num1}/{num2} = {result}')
            print(f'Boss {num1}/{num2} = {result}')
        if operation == 'addition':
            result = add(num1,num2)
            say(f'Boss {num1} + {num2} = {result}')
            print(f'Boss {num1} + {num2} = {result}')
        if operation == 'subtraction':
            result = multiply(num1,num2)
            say(f'Boss {num1} - {num2} = {result}')
            print(f'Boss {num1} - {num2} = {result}')
        say(f'Boss would you like to continue calculating with {result} if yes say 1 after I stop speaking or would you like to start a new calculation if yes say 2 after I stop speaking or would you like to quit the calculator if yes say 3 after I stop speaking ')
        choice = take_command()
        if choice == '1':
            num1 = result
        elif choice == '2':
            should_continue = False
            calculator()
        elif choice == '3':
            exit(calculator())
        else:
            say('Sorry Boss some error has occurred.You will to manually write down your choice')
            choice = input('Enter your choice: ')
            if choice == '1':
                num1 = result
            elif choice == '2':
                should_continue = False
                calculator()
            elif choice == '3':
                exit(calculator())
            else:
                say('Boss That is an invalid choice')


calculator()
