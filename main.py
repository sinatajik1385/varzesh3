from fastapi import FastAPI
from fastapi import *
from multi_threading import do_stuff
from password_checker import check_password_and_user as auth
from database_management.connection import varzehs3
app = FastAPI()
#web scraping
@app.get("/web_scrape") 
def doing_things (password : str , user : str) :
    if auth(passwd= password , user= user) :
        do_stuff()
        return {"response" : "web scraping"}
    else : 
        raise HTTPException (status_code= 400 , detail= "wrong username or password")
# select & add scripts
@app.post("/add_to_news")
def add_to_news (primary_key : int ,
                 title :str | None = None ,
                 content : str | None = None ,
                 which_team : str | None = None ,
                 views_data_int : int | None = None) :
    q = varzehs3()
    if q.check_if_exists(primary_key) : 
        raise HTTPException (status_code= 400 , detail= "primary key already exists")
    else : 
        q.add_to_news(primary_key , title , content , which_team , views_data_int)
        return {"response" : "added to news"}
    
@app.get ("/select_news")
def select_news (primary_key : int, limit : int , offset : int, show_all : bool) :
    q = varzehs3()
    if q.check_if_exists(primary_key) :
        
        return q.select_news(primary_key ,limit , offset , show_all)
        
    else : 
        raise HTTPException (status_code= 400 , detail= "primary key already exists")

    

@app.post("/add_to_video")
def add_to_news (primary_key : int ,
                 title : str | None = None ,
                 time : str | None = None ,
                 link : str | None = None,
                 views : int |None = None) :
    q = varzehs3()
    if q.check_if_exists(primary_key) : 
        raise HTTPException (status_code= 400 , detail= "primary key already exists")
    else : 
        q.add_to_video(primary_key , title , time , link , views)
        return {"response" : "added to vide0=o"}

@app.get ("/select_video")
def select_news (primary_key : int, limit : int , offset : int, show_all : bool) :
    q = varzehs3()
    if q.check_if_exists(primary_key) :
        
        return q.select_video(primary_key , limit , offset , show_all)
        
    else : 
        raise HTTPException (status_code= 400 , detail= "primary key already exists")

    

@app.post("/add_to_leagues")
def add_to_news (pk : int,
                 team_name : str |None = None ,
                 image : str | None = None ,
                 bazi : int | None = None ,
                 tafazol : int |None = None ,
                 emtiaz :int | None = None ,
                 bord :int |None = None,
                 mosavi : int |None = None ,
                 bakht : int |None = None ,
                 gol : int |None = None ,
                 bazi_akhir :str |None = None) :
    q = varzehs3()
    if q.check_if_exists(pk) : 
        raise HTTPException (status_code= 400 , detail= "primary key already exists")
    else : 
        q.add_to_leagues(pk , team_name , image , bazi , tafazol , emtiaz , bord , mosavi , bakht , gol , bazi_akhir)
        return {"response" : "added to leagues"}
    
@app.get ("/select_leagues")
def select_news (primary_key : int , limit : int , offset : int , show_all : bool) :
    q = varzehs3()
    if q.check_if_exists(primary_key) :
        
        return q.select_leagues(primary_key , limit , offset , show_all)
    else : 
        raise HTTPException (status_code= 400 , detail= "primary key already exists")
# update & delete
@app.get("/delete_news")
def delete_news (pk : int ) : 
        datatype = "news"
        q = varzehs3()
        if q.check_if_exists_delete(pk , datatype) :
            q.delete_news(pk )
            return {"response" : f"{pk} has been deleted from the {datatype} table"}
        else :
            raise HTTPException (status_code= 404 , detail= "row does not exist")

@app.get("/delete_video")
def delete_video (pk : int ) : 
        datatype = "video"
        q = varzehs3()
        if q.check_if_exists_delete(pk , datatype) :
            q.delete_video(pk )
            return {"response" : f"{pk} has been deleted from the {datatype} table"}
        else :
            raise HTTPException (status_code= 404 , detail= "row does not exist")

@app.get("/delete_leagues")
def delete_leagues (pk : int ) : 
        datatype = "leagues"
        q = varzehs3()
        if q.check_if_exists_delete(pk , datatype) :
            q.delete_leagues(pk )
            return {"response" : f"{pk} has been deleted from the {datatype} table"}
        else :
            raise HTTPException (status_code= 404 , detail= "row does not exist")
        
@app.get("/delete_everything")
def delete_everything (user : str , paswword : int ) : 
    q = varzehs3()
    if auth(user=user , passwd=paswword) : 
        q.delete_everything()
        return {"response" : "deleted everything"}
    else : 
        raise HTTPException (status_code= 400 , detail= "wrong username or password")
    
@app.get ("/update_news")
def update_news (primary_key : int ,
                 title :str | None = None ,
                 content : str | None = None ,
                 which_team : str | None = None ,
                 views_data_int : int | None = None) : 
    q = varzehs3()
    datatype = "news"
    if q.check_if_exists_delete(primary_key , datatype) :
        q.delete_news(primary_key )
        q.add_to_news(primary_key , title , content , which_team , views_data_int)
        return {"response" : f"{primary_key} has been updated from the {datatype} table"}
    else :
        raise HTTPException (status_code= 404 , detail= "row does not exist")

@app.get ("/update_videos")
def update_videos(primary_key : int ,
                 title : str | None = None ,
                 time : str | None = None ,
                 link : str | None = None,
                 views : int |None = None):
    q = varzehs3()
    datatype = "video"
    if q.check_if_exists_delete(primary_key , datatype) :
            q.delete_video(primary_key )
            q.add_to_video(primary_key , title , time , link , views)
            return {"response" : f"{primary_key} has been deleted from the {datatype} table"}
    else :
        raise HTTPException (status_code= 404 , detail= "row does not exist")
    
@app.get ("/update_leagues")
def update_leagues(pk : int,
                 team_name : str |None = None ,
                 image : str | None = None ,
                 bazi : int | None = None ,
                 tafazol : int |None = None ,
                 emtiaz :int | None = None ,
                 bord :int |None = None,
                 mosavi : int |None = None ,
                 bakht : int |None = None ,
                 gol : int |None = None ,
                 bazi_akhir :str |None = None):
    q = varzehs3()
    datatype = "leagues"
    if q.check_if_exists_delete(pk , datatype) :
        q.delete_leagues(pk )
        q.add_to_leagues(pk , team_name , image , bazi , tafazol , emtiaz , bord , mosavi , bakht , gol , bazi_akhir)
        return {"response" : f"{pk} has been deleted from the {datatype} table"}
    else :
        raise HTTPException (status_code= 404 , detail= "row does not exist")
