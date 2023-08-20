from bs4 import BeautifulSoup
import time
import pandas as pd
import requests



START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs" 
browser = webdriver.Chrome("/Users/akshitas/Akshita/WhiteHatJr/Projects/Project 127") 
browser.get(START_URL) time.sleep(10)

scraped_data = []

def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
          
            for td_tag in td_tags:
                try: 
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
            scraped_data.append(temp_list)



bright_star_table = soup.find("table", attrs={"class", "wikitable"})

table_body = bright_star_table.find('tbody')

table_rows = table_body.find_all('tr')

for row in table_rows:
    table_cols = row.find_all('td')
    print(table_cols)

    temp_list = []

    for col_data in table_cols:
        print(col_data.text)

        data = col_data.text.strip()
        print(data)

        temp_list.append(data)

    scraped_data.append(temp_list)

stars_data = []

for i in range(0,len(scraped_data)):

    stars_name = scraped_data[i][1]
    mass = scraped_data[i][5]
    distance = scraped_data[i][3]
    lum = scraped_data[i][7]
    radius = scraped_data[i][6]

    required_data = [stars_name, mass, distance, lum, radius ]
    stars_data.append(required_data)
    
    headers = ['stars_name', 'mass', 'distance', 'lum', 'radius']
    star_df_1 = pd.DataFrame(stars_data, columns = headers)
    star_df_1.to_csv('scraped_data.csv', index = True, index_label="id")