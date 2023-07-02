import subprocess
import re

First_ip = input("Enter the first IP address: ")
Last_ip = input("Enter the last IP address: ")

def Get_Host(x):
    Dot_Counter = 0
    Pos_Counter = 0
    for i in x:
        if i == ".":
            Dot_Counter = Dot_Counter + 1
        if Dot_Counter == 3:
            return (x[0:Pos_Counter +1], x[Pos_Counter+1: ])
            break
        Pos_Counter += 1

Network, First_Host = Get_Host(First_ip)
Network, Last_Host = Get_Host(Last_ip)

print(Network)
print(First_Host)
print(Last_Host)