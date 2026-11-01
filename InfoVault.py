import json
import os
from colorama import Fore, Style
import time

with open("Vault.json", "r", encoding="utf-8") as arc:
    infos = json.load(arc)
def options():
    while True:
        print("1: Write info.\n2: Read info.\n0: Leave")

        option = input("Option: ")
        if option.isdigit():
            try:
                option = int(option)
            except Exception:
                print("Digit a intire number.")
                continue
        else:
            print("Please, write a number")
            continue
        

        if option == 1:
            key = input("\n\ndigit a name: ")
            
            if key in infos:
                print(Fore.RED + f"\n{key} already exists!" + Style.RESET_ALL)
                time.sleep(2)
                print("")
                continue
            else:
                value = input('what have in this?: ')
                infos[key] = value
                with open("Vault.json", "w", encoding="utf-8") as arc:
                    json.dump(infos, arc, indent=4, ensure_ascii=False)
        elif option == 2:
            with open("Vault.json", "r", encoding="utf-8") as arc:
                read = json.load(arc)
                print(Fore.GREEN + f"\n{read}\n" + Style.RESET_ALL)
        elif option == 0:
            print("Leaving...")
            break

        
if __name__ == "__main__":
    options()