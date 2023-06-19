from bs4 import BeautifulSoup
import requests


def get_content(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        tag_searched = soup.find_all(tag_selected)
        tag_content = [tag_selected.text for tag_selected in tag_searched if tag_selected.text]
        return tag_content
    else:
        print('Error codigo: ', res.status_code)

url = input("Put here the url you want to spy: ")
tag_selected = input("What kind of tag do you want to look? - ")
url_content = get_content(url)

for text in url_content:
    print(text)

print (len(url_content))
# documentation = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start"


