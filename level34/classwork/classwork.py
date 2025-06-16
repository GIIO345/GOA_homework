def validate_hello(greetings):
    greet=['hello','ciao', 'salut','hallo','hola','ahoj','czesc']
    greetings=greetings.lower()
    return any(i  in greetings for i in greet)

