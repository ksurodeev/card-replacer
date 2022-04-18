from scrapli.driver.core import JunosDriver
from textfsm import clitable



dev = {
    "host": "192.168.154.128",
    "port": 32770,
    "auth_username": "lab",
    "auth_password": "lab123",
    "transport": "telnet",
}

def CreateConnection(device):
    with JunosDriver(**device) as conn:
        cards = conn.send_command('show chassis hardware')
    return cards.result

def ParseTemplate(data):
    cli = clitable.CliTable('index', 'templates')
    attr = {'Command': 'show chassis hardware'}
    cli.ParseCmd(cmd_input=data, attributes=attr)
    return cli


if __name__ == "__main__":
    cards = CreateConnection(dev)
    card_parsed = ParseTemplate(cards)
    print(card_parsed)