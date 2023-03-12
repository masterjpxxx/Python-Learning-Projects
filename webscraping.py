#This python program generates information from the Github user inputted
#Step 1 Download and import Beautiful Soup and Requests Library
#Step 2 Ask the user for the Github username
#Step 3 Scrape the Github profile using the username provided
#Step 4 Display the information needed

import requests
from bs4 import BeautifulSoup as bs

github_user = input("What is the Github user account? ")
github_url = 'https://github.com/'+github_user

r = requests.get(github_url)
soup = bs(r.content, 'html.parser')
profile_name = soup.find('span',{'class': 'vcard-fullname', 'itemprop': 'name'})
profile_image = soup.find('img', {'class' : 'avatar-user'})['src']

print(profile_name.text)
print(profile_image)