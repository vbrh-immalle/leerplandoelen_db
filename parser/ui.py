
def yes_or_no(question="", default=False):
    prompt = ""
    if default:
        prompt = question + ' (Y/n) '
    else:
        prompt = question + ' (y/N) '
    while 1:
        reply = input(prompt)
        if len(reply.strip()) == 0:
            return default
        elif reply.lower()[0] == 'y':
            return True
        elif reply.lower()[0] == 'n':
            return False
        else:
            print("Please answer y or no or press enter for default.")
