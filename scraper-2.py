from wiki_scraper import START_URL
import pandas as pd
from bs4 import BeautifulSoup
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL, verify=False)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find_all("table")
temp_list = []


for tr in table[4].find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Name = []
Constellation = []
Distance = []
Mass = []
Radius = []
Discovery_Year = []
# I know the project description didn't include Constellation and Discovery_Year, but I wanted to add them because they seemed useful
for i in range(1, len(temp_list)):
    Name.append(temp_list[i][0])
    Constellation.append(temp_list[i][1])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][8])
    Radius.append([i][9])
    Discovery_Year.append(temp_list[i][13])

dict = {'Name': Name, "Constellation": Constellation, 'Distance': Distance, 'Mass': Mass, 'Radius': Radius, 'Discovery_Year': Discovery_Year}
df = pd.DataFrame(dict)
df.to_csv("brownDwarf.csv")