from typing import Any
from win10toast import ToastNotifier

from library import clean, exit, restart, version, newList, toast, timeConvert
from platform import system
import os, time

bull = ""

def main():
    version.updateVersion()
    clearCommand = "cls" if system().lower() == "windows" else "clear"
    t = ToastNotifier()
    try:
        run = True
        clean.clean(clearCommand)
        print(r"lex-shell { version: "+version.getVersion()+r" }")
        while run:
            origState = input("> ")
            listState = origState.split(" ")
            statement = origState.lower().split(" ")
            match statement[0]:
                case "quit" | "exit" | "exit()" | "quit()":
                    try:
                        run = exit.askExit(clearCommand, statement[1])
                    except IndexError:
                       run = exit.askExit(clearCommand)
                        
                case "clear" | "cls" | "clean":
                    clean.clean(clearCommand)
                
                case "restart":
                    print(f"Restarting...")
                    time.sleep(0.25)
                    
                    restart.restart()
                case "version" | "ver":
                    try:
                        if statement[1] is not None:
                            version.setVersion(statement[1])
                            print("Set",version.getVersion()+"\n")
                    except:
                        print(version.getVersion()+"\n") 
                
                case "toast" | "nty" | "notify":
                    try:
                        toast.start(int(statement[1]), statement[2:])
                    except (ValueError, IndexError):
                        print(f"• Usage: \n\t• toast <seconds> <message>")
                        
                case default:
                    if len(listState) != 1: # create a class that extends list, with custom repr
                        print(newList.returnNewList(listState)+" is not a valid command.\n\t")
                    else:
                        print("'"+listState[0] + "' is not a valid command.\n")
                    
    except KeyboardInterrupt:
        if exit.askExit(clearCommand) == True:
            main()
            
if __name__ == '__main__':
    main()