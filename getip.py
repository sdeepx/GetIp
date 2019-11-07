from socket import *
from sys import *


class GetIp:

    def __init__(self):
        try:
            try:
                self.socket = socket(AF_INET, SOCK_STREAM)
                print("[+] Connection successfully created->")
            except error as err:
                print("[-] Connection failed with error %s " % err)

            self.port = 80

            try:
                self.host = gethostbyname(input(" : "))
            except gaierror as ge:
                print("There was an error resolving the host or check your internet connection %s " % ge)
                exit()

            self.socket.connect((self.host, self.port))
            print("Ip -> %s " % self.host)

        except error:
            print("Something went wrong: %s " % error)


if __name__ == '__main__':
    GetIp()
