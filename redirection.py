import requests

u=input("Enter the url in correct format ")
pay="http://google.com/"
r=u+pay
req=requests.get(r)
print("the request is ",r)
out=req.status_code

print(out)