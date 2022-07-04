import requests

url = 'https://peakvisor.com/photo/Issyk-Kul-Region.jpg'

res = requests.get(url)

name = "photos/photo1.jpg"

with open(name, "wb") as file:
    file.write(res.content)