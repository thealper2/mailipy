import sys
import smtplib
import colorama
import argparse
from mailipy_config import email, password

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

SERVERS = {
	'gmail': '',
	'yahoo': '',
	'outlook': '',
}

PORT = 0

def send_mail(server="", count="", subject="", message="", target=""):
	try:
		msg = f'From {email}\nTo: {target}\nSubject {subject}\n{message}\n'
		srv = smtplib.SMTP(SERVERS[server], PORT)

		srv.ehlo()
		srv.starttls()
		srv.ehlo()
		srv.login(email, password)

		try:
			for i in range(count):
				srv.sendmail(email, target, msg)
				print(f'{Fore.GREEN}[+] [{i}] Email Send! From: {email} To: {Target}{Fore.RESET}')
			srv.close()

		except Exception as err:
			print(f'{Fore.RED}[!] Sending Error: {err}{Fore.RESET}')

	except Exception as e:
		print(f'{Fore.RED}[!] Error: {e}{Fore.RESET}')


def list_servers():
	print(f'{Fore.YELLOW} [-] List of servers:{Fore.RESET}')
	for keys, value in SERVERS.items():
		print(f'{Fore.YELLOW}[*] {keys}{Fore.RESET}')


# server count subject message target
argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('--target', required=False, type=str, help='')
argument_parser.add_argument('--server', required=False, type=str, help='')
argument_parser.add_argument('--count', required=False, type=int, help='')
argument_parser.add_argument('--subject', required=False, type=str, help='')
argument_parser.add_argument('--message', required=False, type=str, help='')
argument_parser.add_argument('--list', required=False, action='store_true', help='')
arg = argument_parser.parse_args()

if (arg.target == None and arg.server == None and arg.count == None and arg.subject == None and arg.message == None and arg.list):
	list_servers()

elif (arg.target != None and arg.server != None and arg.count != None and arg.subject != None and arg.message != None and not arg.list):
	send_mail(server=arg.server, count=arg.count, subject=arg.subject, message=arg.message, target=arg.target)
