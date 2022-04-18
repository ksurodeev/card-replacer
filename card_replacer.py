from socket import create_connection
from sqlite3 import DataError
from textwrap import wrap
from scrapli.driver.core import JunosDriver
from textfsm import clitable
from functools import wraps
from datetime import date
import re




dev = {
    "host": "192.168.154.128",
    "port": 32769,
    "auth_username": "lab",
    "auth_password": "lab123",
    "transport": "telnet",
}


class Router():
    '''
    Class for connect and retrieve information from device.
    '''
    def __init__(self, device):
        self.host = device["host"]
        self.port = device["port"]
        self.device = device

    def __str__(self):
        return f"Router: {self.host}" 

    def __repr__(self):
        return f"Router ('{self.device}')"

    def SwapTheCard(self, fpc_num):
        '''
        Make some actions for safety card swap.
        '''
        command1 = 'show chassis fpc ' + str(fpc_num)


        def _CreateConnection(self, command):
            with JunosDriver(**self.device) as conn:
                cmd_result = conn.send_command(command)
            return cmd_result

        def _ParseTemplate(self, cmd_result):
            cli = clitable.CliTable('index', 'templates')
            attr = {'Command': 'show chassis hardware'}
            cli.ParseCmd(cmd_input=cmd_result, attributes=attr)
            return cli

        def _CreateOldStateFile(self):
            filename = 'old state' + str(date.fromtimestamp)
            with open(filename, 'w') as file:
                commands = ['show chassis hardware detail', 'show chassis alarms', 'show system uptime', 'show chassis routing-engine', 'show interfaces terse']
                with JunosDriver(**self.device) as connect:
                    result = connect.send_commands(commands)
                for r in result:    
                    file.writelines(r.result)

        #create file before works
        card_state = _CreateConnection(self, command=command1)  
        match = re.search(r'\s+\d+\s+(?P<state>\w+).*', card_state.result)
        print(match)
        if match.group('state') == 'Online':
            pass
        else:
            raise DataError("Card is already offline, please check the card")



if __name__ == "__main__":
    R1 = Router(dev)
    R1.SwapTheCard(0)