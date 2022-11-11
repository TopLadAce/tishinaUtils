from itertools import chain, repeat


def isValidInput(promptText: str, failText: str, validInputs: list) -> str:
    """Checks if the user input a valid choice."""

    # Make fail text still show the prompt
    # Combine both functions into one

    def inputInOptions(reply: str) -> bool:
        """Checks if input is within valid inputs, returns bool."""
        reply = reply.lower()
        return reply in validInputs

    for value in validInputs:
        validInputs[validInputs.index(value)] = str(value) if value.isdigit() else value.lower()

    if not failText:
        failText = promptText

    prompts = chain([promptText], repeat(failText))
    replies = map(input, prompts)
    validResponse = next(filter(inputInOptions, replies)).lower()

    return validResponse


def isValidInt(promptText: str, failText: str, validInputs: list) -> int:
    """Checks if int input is valid. If validInputs is empty, just checks if an int has been input."""

    def inputInOptions(reply: str):
        """Checks if input is within valid inputs, returns bool."""
        return reply in validInputs and reply.isdigit() if validInputs else reply.isdigit()

    if not failText:
        failText = promptText
    # Chain uses prompt text as initial pop up, once exhausted, moves onto fail text.
    # Repeat when not given a loop amount will loop endlessly, works when prompting fail text.
    prompts = chain([promptText], repeat(failText))
    replies = map(input, prompts)
    validResponse = next(filter(inputInOptions, replies))

    return int(validResponse)


def isValid(promptText: str, validInputs: list, failText: str, inputType: str) -> str:
    match inputType:
        case 'int':
            typeFunc = int
        case 'float':
            typeFunc = float
        case 'string':
            typeFunc = str
        case _:
            # Need some sort of error for case someone sets up wrong?
            pass
    userInput = input(promptText)
    try:
        typeFunc(userInput)
    except TypeError:
        pass
    while userInput not in validInputs:
        userInput = input(f'{failText}\n{promptText}')
        try:
            typeFunc(userInput)
        except TypeError:
            pass

    return userInput

