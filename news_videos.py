from bs4 import BeautifulSoup
import requests
from database_management.connection import varzehs3 
q = varzehs3()
"""news scraping"""
html = requests.get ("https://www.varzesh3.com/").text
soup = BeautifulSoup (html , "html.parser")
def scrape_varzesh3 () :
    conntainers = soup.find_all("li" , class_="text-type")

    for i in conntainers :
        href = i.find("a").get("href")
        if href.split("/")[3] == "news" :
            try :
                    
                primary_key = (i)["data-newsid"]
                title  = (i).text
                link = href
                html1 = requests.get (link).text
                soup1 = BeautifulSoup (html1 , "html.parser")
                views = soup1.find("div" , class_="news-info")
                views1 = views.find_all("span")
                views_data = views1[2].text    
                try :
                    views_data_int = float((views_data.split("K"))[0]) * 1000
                    views_data_int = int(views_data_int)
                except :
                    views_data_int = views_data.split(" ")[0]
                content = soup1.find("div" , class_="news-text")
                content1 = content.find("p")
                content2 = ((content1).text)
                try :
                    which_team = soup.find("div" , class_="suggested-tag")
                    which_team1 = which_team.find("span")
                    which_team2 = ((which_team1).text)
                except : 
                    which_team2 ="unknown"
                
                q.add_to_news(primary_key , title , content2 , which_team2 , views_data_int )
                print("news done")

            except :
                print("duplicate primary key")
        if href.split("/")[3] == "video" :

                    
                primary_key = (i)["data-newsid"]
                title  = (i).text
                link = href
                html1 = requests.get (link).text
                soup1 = BeautifulSoup (html1 , "html.parser")
                metrics = soup1.find("div" , class_="video-info")
                metrics1 = metrics.find_all("span")
                views = metrics1.find("span" , class_="view")
                try :
                    views_int = float((views.split("K"))[0]) * 1000
                    views_int = int(views_int)
                except :
                    views_int = views.split(" ")[0]
                time = metrics.find("span" , class_="date")
                
                q.add_to_video(primary_key , title , time , link,  views_int)
                
    
        else : 
            pass


scrape_varzesh3 ()