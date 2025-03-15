import colorama
from colorama import Fore,Back,Style
import os
colorama.init()

name = input(Fore.BLUE + "Enter the name of the file you would like your ids in(add file extension add the end\neg: ids.txt): ")
inp = int(input(Fore.GREEN + "Enter the first range you would like your user ids(eg:100): "))
inp1 = int(input(Fore.LIGHTGREEN_EX + "Enter the second range you would like your user ids(eg:1000): "))
print(Fore.RED + f"Generating a file with user ids from {inp} to {inp1}")

with open(name,"w") as f:
    for i in range(inp,inp1):
        f.write(f"{str(i)}\n")
    print(Fore.GREEN + f"{name} has been sucessfully generated at {os.getcwd()}\\{name}")

