definitions = {
    "quit": {
        "alias": ["quit", "exit", "quit()", "exit()"],
        "description": [
            "Exits the current session.",
            "• If '-na' is included, then it will automatically exit without confirming.",
            "• If 'c' is included,  then it will clear the console, then exit without confirming."
        ],
        "usage": "quit <optional-args>"
    },
    "clear": {
        "alias": ["clear", "clean", "cls"],
        "description": [
            "Clears the current console screen."
        ],
        "usage": "clear"
    },
    "restart": {
        "alias": ["restart", "re"],
        "description": [
            "Restarts the current console.",
            "• Increments version number by 1."
        ],
        "usage": "restart"
    },
    "version": {
        "alias": ["version", "ver"],
        "description": [
            "Gets the current version, and outputs it to the console.",
            "• If a number is included after the command, it sets the version, and then outputs it to console."
        ],
        "usage": "version <optional-arg>"
    },
    "toast": {
        "alias": ["toast", "nty", "notify"],
        "description": [
            "Make a routine for notifying user after a certain amount of time."
        ],
        "usage": "toast <time(seconds)> <message>"
    },
    "help": {
        "alias": ["help", "?"],
        "description": [
            "This is a contextual command.",
            "• Append command names to get information about that command."
        ],
        "usage": "help '<command>'"
    },
    "list": {
        "alias": ["cmdlist", "commands", "cmd", "cmds", "list"],
        "description": [
            "This ouputs all help messages."
        ],
        "usage": "list"
    }
}

def commandHelp(commandName="help"):
    for key, value in definitions.items():
        if commandName in value["alias"]:
            commandName = key
            break
    g = ""
    if commandName == '':
        commandName = "help"
    if commandName not in definitions.keys():
      g += f"• '{commandName}' not found. Using default output.\n\n"  
      commandName = "help"
    h = definitions.get(commandName)
    g += f"Name: '{commandName}'\nAliases:"
    for alias in h["alias"]:
        g += f"   • {alias}"
    g += "\nDescription: \n"
    for line in h["description"]:
        g += f"\t{line}\n"
    g += "\nUsage: "+h["usage"]+"\n"
    return g

def displayCommands(colNum=20):
    for key in definitions.keys():
        print(commandHelp(key)+"-"*colNum+"\n")
        cont = input("Press Enter to continue, or input 'e' to stop output. ")
        if cont != "":
            break