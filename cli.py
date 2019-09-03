import assistant

try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

while True:
    text = "\n"
    while True:
        line = input(">")
        line = line.rstrip()
        if line == "":
            break
        if line[-1] == "\\":
            line = line[:-1]
            text += "%s\n" % line
        else:
            text += "%s\n" % line
            break
    if text == "\n":
        break
    text = text.strip()
    argv = text.split(None,1)
    r = assistant.process_message_with_path("cli",argv[0],argv[1])
    print(r)
