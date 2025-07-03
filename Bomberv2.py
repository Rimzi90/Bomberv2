from twilio.rest import Client
import os
import time
import random
from colorama import Fore, init

init(autoreset=True)

# ✅ Your Twilio credentials
account_sid = "ACa7dc2ae4add245f23136abd9dd31a66d"
auth_token = "6bfbf7f1bb2be37f02722a0b5b01bd78"
twilio_number = "+15413293749"

# 🔢 Target number (MUST be verified in Twilio trial)
target_number = input("Enter Verified Target Number (with +92): ")

client = Client(account_sid, auth_token)

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

def banner():
    os.system("clear")
    print(f"""{random.choice(colors)}
██████╗ ██╗███╗   ███╗███████╗██████╗ ██╗
██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║
██████╔╝██║██╔████╔██║█████╗  ██████╔╝██║
██╔═══╝ ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ ██║
██║     ██║██║ ╚═╝ ██║███████╗██║     ██║
╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝
   [☎️ Real Call Bomber | Code by Rimzi 😈]
""")

def make_call():
    try:
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=target_number,
            from_=twilio_number
        )
        print(f"{Fore.GREEN}[✔] Call sent! SID: {call.sid}")
    except Exception as e:
        print(f"{Fore.RED}[✘] Call failed: {e}")

# === MAIN LOOP
while True:
    banner()
    print(f"{Fore.CYAN}Target: {target_number}")
    print(f"{Fore.GREEN}[1] Start Call Bombing")
    print(f"{Fore.RED}[q] Quit\n")

    choice = input(">> ")

    if choice == "1":
        make_call()
        time.sleep(5)
    elif choice.lower() == "q":
        print(f"{Fore.YELLOW}Exiting... Rimzi90 out! 😎")
        break
    else:
        print(f"{Fore.RED}Invalid option! Try again.")
        time.sleep(1)from twilio.rest import Client
import os
import time
import random
from colorama import Fore, init

init(autoreset=True)

# ✅ Your Twilio credentials (don't share publicly!)
account_sid = "ACa7dc2ae4add245f23136abd9dd31a66d"
auth_token = "6bfbf7f1bb2be37f02722a0b5b01bd78"
twilio_number = "+15413293749"

# 🔢 Input target number (MUST be verified on Twilio trial)
target_number = input("Enter Verified Target Number (with +92): ")

client = Client(account_sid, auth_token)

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

def banner():
    os.system("clear")
    print(f"""{random.choice(colors)}
██████╗ ██╗███╗   ███╗███████╗██████╗ ██╗
██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║
██████╔╝██║██╔████╔██║█████╗  ██████╔╝██║
██╔═══╝ ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ ██║
██║     ██║██║ ╚═╝ ██║███████╗██║     ██║
╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝
 [☎️💬 RIMZI Super Bomber v2 | Code by Rimzi90 😈]
""")

def make_call():
    try:
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=target_number,
            from_=twilio_number
        )
        print(f"{Fore.GREEN}[✔] Call sent! SID: {call.sid}")
    except Exception as e:
        print(f"{Fore.RED}[✘] Call failed: {e}")

def send_sms():
    try:
        message = client.messages.create(
            body="👑 Brute by Rimzi90! Call Bombing Active 🔥",
            from_=twilio_number,
            to=target_number
        )
        print(f"{Fore.GREEN}[✔] SMS sent! SID: {message.sid}")
    except Exception as e:
        print(f"{Fore.RED}[✘] SMS failed: {e}")

# === MAIN LOOP
while True:
    banner()
    print(f"{Fore.CYAN}Target: {target_number}")
    print(f"{Fore.GREEN}[1] Start Call Bombing")
    print(f"{Fore.YELLOW}[2] Send SMS")
    print(f"{Fore.RED}[q] Quit\n")

    choice = input(">> ")

    if choice == "1":
        make_call()
        time.sleep(5)
    elif choice == "2":
        send_sms()
        time.sleep(3)
    elif choice.lower() == "q":
        print(f"{Fore.YELLOW}Exiting... Rimzi90 out! 😎")
        break
    else:
        print(f"{Fore.RED}Invalid option! Try again.")
        time.sleep(1)
