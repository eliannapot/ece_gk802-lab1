import requests  # εισαγωγή της βιβλιοθήκης
import datetime

url = input("Insert url\n")  # προσδιορισμός του url

#Αίτημα
with requests.get(url) as response:  # το αντικείμενο response
    #Τύπωση Επικεφαλίδων
    headers = response.headers
    print("Headers are: ", headers)
    
#Λογισμικό
if "Server" in headers:
    serv = headers["Server"]
else:
    serv = "No information provided."
print("\nSoftware used by the server is:", serv)


#Cookies
if "set-cookie" in headers:
    cookies = response.cookies
    for c in cookies:
        name = c.name
        value = c.value
        exp = c.expires
        print("The website uses a cookie with \nName: ", name, "\nValue: ", value, "\nExpiration: ", exp)
else:
    print("The website doesn't use cookies.")
