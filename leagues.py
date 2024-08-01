from bs4 import BeautifulSoup
import requests
from database_management.connection import varzehs3 
q = varzehs3()

html = requests.get (r"https://www.varzesh3.com/football/league/6/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86").text
soup = BeautifulSoup (html , "html.parser")
diffrent_leagues = soup.find("ul" , class_="ent-list-box")
list_items = diffrent_leagues.find_all("li")
for i in list_items :
    link = i.find("a").get("href")
    
    html1 = requests.get (f"https://www.varzesh3.com{link}").text
    soup = BeautifulSoup (html , "html.parser")

    conntainer_items_ = soup.find ("table" , class_= "league-standing football-standing")

    conntainer_items_1 = conntainer_items_.find("tbody")
    conntainer_items_2 = conntainer_items_1.find_all("tr")
    no_header = 0
    for i in conntainer_items_2 :
        try :
                
            team_specs = i.find("a").get("href").split("/")
            team_pk = team_specs[-2]
            team_name = team_specs[-1]
            image = i.find("img").get("src")
            brief = i.find_all("td" , class_="brief-mode")

            bazi = brief[0].text
            tafazol = brief[1].text
            emtiaz = brief[2].text
            
            complete = i.find_all("td" , class_="complete-mode")
            bord = complete[0].text
            mosavi = complete[1].text
            bakht = complete[2].text
            gol = complete[3].text

            bazi_akhir = i.find ("td" , class_="last-five").text
            q.add_to_leagues(team_pk , team_name , image , bazi , tafazol , emtiaz , bord , mosavi , bakht , gol , bazi_akhir)
            print("done")
        except :
                    
            print ("duplicate primary key skipping") 

