from scrapli.driver.core import JunosDriver
import textfsm
from ntc_templates import *


dev = {
    "host": "192.168.154.128",
    "port": 32769,
    "auth_username": "lab",
    "auth_password": "lab123",
    "transport": "telnet",
}

def CreateConnection(device):
    with JunosDriver(**device) as conn:
       # conn.send_command('cli')
        cards = conn.send_command('show chassis hardware detail')
    return cards.result


if __name__ == "__main__":
    print(CreateConnection(dev))