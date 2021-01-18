import requests
import json
Base_Url='http://127.0.0.1:8000/'
t=1
while(t):
    n=int(input(("Press 1 to book a slot, Press 2 to view bookings, Press 3 to cancel a booking slot, Press 4 to exit: ")))
    if n==1:
        s=input("Enter slot number and name: ")
        l=s.split(" ")
        slot=int(l[0])
        name=l[1]
        d={"slot": slot,"name": name}
        r=requests.post(Base_Url+'booking',json=d)
        print(r.json())
    if n==2:
        r=requests.get(Base_Url+'booking')
        print(r.json())
    if n==3:
        s=input("Enter slot number and name: ")
        l=s.split(" ")
        slot=int(l[0])
        name=l[1]
        d={"slot": slot,"name": name}
        r=requests.post(Base_Url+'cancel',json=d)
        print(r.json())
    if n==4:
        t=0
        