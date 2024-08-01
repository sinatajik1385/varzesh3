import psycopg2
import json

class varzehs3 () :
    def __init__(self):
        self.con = psycopg2.connect(host = "localhost",dbname = "varzesh3",port = "5432",user = "sina",password = "123") 
        self.curr = self.con.cursor()
    def add_to_news (self , primary_key , title , content2 , which_team2 , views_data_int ) :
        self.curr.execute(f"""
        INSERT INTO pk_databank (p_key , data_type)
        VALUES ({primary_key} , 'news');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO news_views (p_key , views)
        VALUES ({primary_key} , {views_data_int});
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO news_content (p_key , title , content)
        VALUES ({primary_key} , '{title}' , '{content2}');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO news_leagues (p_key , which_league)
        VALUES ({primary_key} , '{which_team2}');
        """)
        self.con.commit()

    def add_to_video (self , primary_key , title , time ,link, views_int) :
        self.curr.execute(f"""
        INSERT INTO pk_databank (p_key , data_type)
        VALUES ({primary_key} , 'video');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO video_content (p_key , title)
        VALUES ({primary_key} , '{title}');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO video_link (p_key , link)
        VALUES ({primary_key} , '{link}');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO video_time_views (p_key , time , views)
        VALUES ({primary_key} , '{time}' , {views_int});
        """)
        self.con.commit()
    def add_to_leagues (self , team_pk , team_name , image , bazi , tafazol , emtiaz , bord , mosavi , bakht , gol , bazi_akhir) :
        self.curr.execute(f"""
        INSERT INTO pk_databank (p_key , data_type)
        VALUES ({team_pk} , 'leagues');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO league_team_specs (p_key , team_name , image)
        VALUES ({team_pk} , '{team_name}' , '{image}');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO league_last_five_games (p_key , last_five_games)
        VALUES ({team_pk} , '{bazi_akhir}');
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO league_complete (p_key , bord , mosavi , bakht , gol)
        VALUES ({team_pk} , {bord} , {mosavi} , {bakht} , {gol});
        """)
        self.con.commit()
        self.curr.execute(f"""
        INSERT INTO league_brief (p_key , bazi , tafazol , emtiaz)
        VALUES ({team_pk} , {bazi} , {tafazol} , {emtiaz});
        """)
        self.con.commit()
    def check_if_exists (self , pk) :
        self.curr.execute(f"""
        select * from pk_databank 
        where p_key = {pk};
        """)
        result = self.curr.fetchall()
        if result :
            return True
        else :
            return False
    def select_news(self,pk,limit,offset , show_all) :
        if show_all == False :
            self.curr.execute(f"""
            select pk_databank.p_key , data_type , views , title , content , which_league  from pk_databank
            join news_views
            on news_views.p_key = pk_databank.p_key
            join news_content
            on news_content.p_key = pk_databank.p_key
            join news_leagues
            on news_leagues.p_key = pk_databank.p_key
            where pk_databank.p_key = {pk}
            limit {limit} offset {offset};
            """)
            my_query = json.dumps(self.curr.fetchone())
            return my_query
        else : 
            self.curr.execute(f"""
            select pk_databank.p_key , data_type , views , title , content , which_league  from pk_databank
            join news_views
            on news_views.p_key = pk_databank.p_key
            join news_content
            on news_content.p_key = pk_databank.p_key
            join news_leagues
            on news_leagues.p_key = pk_databank.p_key;
            """)
            my_query = json.dumps(self.curr.fetchall())
            return my_query
    def select_video (self,pk,limit,offset , show_all) :
        if show_all == False :
            self.curr.execute(f"""
            select pk_databank.p_key , data_type , title , link , time , views from pk_databank
            join video_content
            on video_content.p_key = pk_databank.p_key
            join video_link
            on video_link.p_key = pk_databank.p_key
            join video_time_views
            on video_time_views.p_key = pk_databank.p_key
            where pk_databank.p_key = {pk}
            limit {limit} offset {offset};
            """)
            my_query = json.dumps(self.curr.fetchone())
            return my_query
        else : 
            self.curr.execute(f"""
            select pk_databank.p_key , data_type , title , link , time , views from pk_databank
            join video_content
            on video_content.p_key = pk_databank.p_key
            join video_link
            on video_link.p_key = pk_databank.p_key
            join video_time_views
            on video_time_views.p_key = pk_databank.p_key;
            """)
            my_query = json.dumps(self.curr.fetchall())
            return my_query
    def select_leagues (self,pk,limit,offset , show_all) :
        if show_all == False :
            self.curr.execute(f"""
            select pk_databank.p_key  , data_type  , team_name  , image  , last_five_games  bord  , mosavi  , bakht  , gol  , bazi , tafazol , emtiaz from pk_databank
            join league_team_specs
            on league_team_specs.p_key = pk_databank.p_key
            join league_last_five_games
            on league_last_five_games.p_key = pk_databank.p_key
            join league_complete
            on league_complete.p_key = pk_databank.p_key
            join league_brief
            on league_brief.p_key = pk_databank.p_key
            where pk_databank.p_key = {pk}
            limit {limit} offset {offset};
            """)
            my_query = json.dumps(self.curr.fetchone())
            return my_query
        else :
            self.curr.execute(f"""
            select pk_databank.p_key  , data_type  , team_name  , image  , last_five_games  bord  , mosavi  , bakht  , gol  , bazi , tafazol , emtiaz from pk_databank
            join league_team_specs
            on league_team_specs.p_key = pk_databank.p_key
            join league_last_five_games
            on league_last_five_games.p_key = pk_databank.p_key
            join league_complete
            on league_complete.p_key = pk_databank.p_key
            join league_brief
            on league_brief.p_key = pk_databank.p_key;
            """)
            my_query = json.dumps(self.curr.fetchall())
            return my_query
    def delete_news (self, pk) :
        self.curr.execute(f"""
        
        delete from news_views
        where p_key = {pk};
        
        delete from news_content
        where p_key = {pk};
        
        delete from news_leagues
        where p_key = {pk};
        
        delete from pk_databank
        where p_key = {pk};
        """)
        self.con.commit()
    def delete_video (self, pk) :
        self.curr.execute(f"""
        
        delete from video_content
        where p_key = {pk};
        
        delete from video_link
        where p_key = {pk};
        
        delete from video_time_views
        where p_key = {pk};
        
        delete from pk_databank
        where p_key = {pk};
        """)
        self.con.commit()
    def delete_leagues (self, pk) :
        self.curr.execute(f"""
        
        delete from league_team_specs
        where p_key = {pk};
        
        delete from league_last_five_games
        where p_key = {pk};
        
        delete from league_complete
        where p_key = {pk};
        
        delete from league_brief
        where p_key = {pk};
        
        delete from pk_databank
        where p_key = {pk};
        
        """)
        self.con.commit()
    def check_if_exists_delete (self , pk , datatype) : 
        self.curr.execute (f"""
        select * from pk_databank 
        where p_key = {pk} and data_type = '{datatype}'
        """)
        if self.curr.fetchone() : 
            return True
        else :
            return False
    def delete_everything (self) :
        self.curr.execute(f"""
        delete from table Pk_databank ;
        delete from table news_content ;
        delete from table news_views ;
        delete from table news_leagues ;
        delete from table video_content ;
        delete from table video_link ;
        delete from table video_time_views ;
        delete from table league_team_specs ;
        delete from table league_brief ;
        delete from table league_complete ;
        delete from table league_last_five_games ;
        """)
varzehs3()
