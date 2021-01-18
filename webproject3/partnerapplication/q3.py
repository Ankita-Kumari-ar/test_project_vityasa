import requests
import json
Base_Url='http://127.0.0.1:8000/'
ENDPOINT="plot"
t=1
while(t):
    s=input("Enter x coordinate and y coordinate of point: ")
    l=s.split(" ")
    x=int(l[0])
    y=int(l[1])
    d={"x": x,"y": y}
    r=requests.post(Base_Url+ENDPOINT,json=d)
    print(r.json())
    t=int(input(("Press 1 to continue and  Press 0 to exit: ")))
        