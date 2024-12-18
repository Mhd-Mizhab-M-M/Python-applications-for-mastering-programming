#!/usr/bin/env python
# coding: utf-8

# In[6]:


def displayOuterlayerInterface():
    # Define colors using ANSI escape codes
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"

    # Outer layer (colored flaps)
    print(f" _______________________ {RESET}")
    print(f"| {GREEN} _______     {RED}_______{RESET}  |")
    print(f"| {GREEN}|       {GREEN}|   {RED}|       {RED}|{RESET} |")
    print(f"| {GREEN}| GREEN {GREEN}|   {RED}|  RED  {RED}|{RESET} |")
    print(f"| {GREEN}|_______{GREEN}|   {RED}|_______{RED}|{RESET} |")  # Innermost layer (where the fortune will be)
    print(f"| {RESET}                      |")
    print(f"| {BLUE} _______     {YELLOW}_______{RESET}  |")
    print(f"| {BLUE}|       {BLUE}|   {YELLOW}|       {YELLOW}|{RESET} |")
    print(f"| {BLUE}| BLUE  {BLUE}|   {YELLOW}| YELLOW{YELLOW}|{RESET} |")
    print(f"| {BLUE}|_______{BLUE}|   {YELLOW}|_______{YELLOW}|{RESET} |")
    print(f"|_______________________{RESET}|")

def displayOddlayerInterface():
    # Define colors using ANSI escape codes
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"

    # Outer layer (colored flaps)
    print(f" _______________________ {RESET}")
    print(f"| {GREEN} _______     {RED}_______{RESET}  |")
    print(f"| {GREEN}|       {GREEN}|   {RED}|       {RED}|{RESET} |")
    print(f"| {GREEN}|   1   {GREEN}|   {RED}|   3   {RED}|{RESET} |")
    print(f"| {GREEN}|_______{GREEN}|   {RED}|_______{RED}|{RESET} |")  # Innermost layer (where the fortune will be)
    print(f"| {RESET}                      |")
    print(f"| {BLUE} _______     {YELLOW}_______{RESET}  |")
    print(f"| {BLUE}|       {BLUE}|   {YELLOW}|       {YELLOW}|{RESET} |")
    print(f"| {BLUE}|   5   {BLUE}|   {YELLOW}|   7   {YELLOW}|{RESET} |")
    print(f"| {BLUE}|_______{BLUE}|   {YELLOW}|_______{YELLOW}|{RESET} |")
    print(f"|_______________________{RESET}|")

def displayEvenlayerInterface():
    # Define colors using ANSI escape codes
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"

    # Outer layer (colored flaps)
    print(f" _______________________ {RESET}")
    print(f"| {GREEN} _______     {RED}_______{RESET}  |")
    print(f"| {GREEN}|       {GREEN}|   {RED}|       {RED}|{RESET} |")
    print(f"| {GREEN}|   2   {GREEN}|   {RED}|   4   {RED}|{RESET} |")
    print(f"| {GREEN}|_______{GREEN}|   {RED}|_______{RED}|{RESET} |")  # Innermost layer (where the fortune will be)
    print(f"| {RESET}                      |")
    print(f"| {BLUE} _______     {YELLOW}_______{RESET}  |")
    print(f"| {BLUE}|       {BLUE}|   {YELLOW}|       {YELLOW}|{RESET} |")
    print(f"| {BLUE}|   6   {BLUE}|   {YELLOW}|   8   {YELLOW}|{RESET} |")
    print(f"| {BLUE}|_______{BLUE}|   {YELLOW}|_______{YELLOW}|{RESET} |")
    print(f"|_______________________{RESET}|")


# In[7]:


def displayNum(colour):
    odd = [1,3,5,7]
    even = [2,4,6,8]
    existColour = ["GREEN","YELLOW","BLUE","RED"]
    if colour in existColour:
        if len(colour) in odd:
            displayOddlayerInterface()
        elif len(colour) in even:
            displayEvenlayerInterface()
        else:
            raise Exception("Incorrect Number chosen")
    else:
        raise Exception("Incorrect Colour chosen")


# In[8]:


def printContentsLayer(num):
    import time
    contents = {
    1: "Why don't scientists trust atoms? Because they make up everything!",
    2: "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    3: "Parallel lines have so much in common. It's a shame they'll never meet.",
    4: "I used to play piano by ear, but now I use my hands.",
    5: "My dog used to chase people on a bike a lot. It got so bad I had to take his bike away.",
    6: "I'm reading a book about anti-gravity. It's impossible to put down!",
    7: "I'm on a seafood diet. I see food and I eat it.",
    8: "I asked my dad for a loan and he said, 'Sure, as long as you pay me back with interest.' I said, 'That's cool, I'll write you a letter when I get back.'"
    }
    print("YOU GOT\n")
    print(".\n")
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(contents[num])


# In[9]:


import cProfile
def main():
    print("Welcome to Tip Top !")
    displayOuterlayerInterface()
    chosen_colour = input("Enter the colour to be chosen :")
    displayNum(chosen_colour)
    chosen_number = int(input("Enter the number to be chosen :"))
    print("\n")
    printContentsLayer(chosen_number)
cProfile.run('main()')


# In[17]:


School_schedule = {
    "Monday": ["Math", "Science", "English"],
    "Tuesday": ["History", "Math", "Art"],
    "Wednesday": ["Science", "English", "PE"],
    "Thursday": ["Math", "History", "Art"],
    "Friday": ["Science", "English", "PE"]
}
print(School_schedule.get("Monday",[]))  # Handle case where day might not be present

