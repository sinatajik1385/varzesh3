"""
#delete clauses
drop table Pk_databank cascade;
drop table news_content cascade;
drop table news_views cascade;
drop table news_leagues cascade;
drop table video_content cascade;
drop table video_link cascade;
drop table video_time_views cascade;
drop table league_team_specs cascade;
drop table league_brief cascade;
drop table league_complete cascade;
drop table league_last_five_games cascade;



CREATE TABLE IF NOT EXISTS Pk_databank(
    p_key integer NOT NULL PRIMARY KEY , 
    data_type varchar);




CREATE TABLE IF NOT EXISTS news_content(
    p_key integer NOT NULL PRIMARY KEY,
    title character varying(100)  NOT NULL,
    content character varying);


ALTER TABLE news_content
    ADD CONSTRAINT fk_news_content_to_Pk_databank 
    FOREIGN KEY (p_key) REFERENCES Pk_databank  (p_key);




CREATE TABLE IF NOT EXISTS news_views(
    p_key integer NOT NULL PRIMARY KEY,
    views integer);


ALTER TABLE news_views
    ADD CONSTRAINT fk_news_views_to_Pk_databank 
    FOREIGN KEY (p_key) REFERENCES Pk_databank   (p_key);




CREATE TABLE IF NOT EXISTS news_leagues(
    p_key integer NOT NULL PRIMARY KEY,
    which_league character varying(30));


ALTER TABLE news_leagues
    ADD CONSTRAINT fk_news_leagues_to_Pk_databank  
    FOREIGN KEY (p_key) REFERENCES Pk_databank    (p_key);


"""----------------------"""

CREATE TABLE IF NOT EXISTS video_content(
    p_key integer NOT NULL PRIMARY KEY,
    title character varying(50)  NOT NULL);


ALTER TABLE video_content
    ADD CONSTRAINT fk_video_content_to_Pk_databank 
    FOREIGN KEY (p_key) REFERENCES Pk_databank  (p_key);




CREATE TABLE IF NOT EXISTS video_link(
    p_key integer NOT NULL PRIMARY KEY,
    link character varying );


ALTER TABLE video_link
    ADD CONSTRAINT fk_video_link_to_Pk_databank  
    FOREIGN KEY (p_key) REFERENCES Pk_databank   (p_key);




CREATE TABLE IF NOT EXISTS video_time_views(
    p_key integer NOT NULL PRIMARY KEY,
    time character varying ,
    views integer );


ALTER TABLE video_time_views
    ADD CONSTRAINT fk_video_time_views_to_Pk_databank  
    FOREIGN KEY (p_key) REFERENCES Pk_databank   (p_key);
"""


"""----------------------"""


"""
CREATE TABLE IF NOT EXISTS league_team_specs(
    p_key integer NOT NULL PRIMARY KEY,
    team_name character varying ,
    image character varying);


ALTER TABLE league_team_specs
    ADD CONSTRAINT fk_league_team_specs_to_Pk_databank 
    FOREIGN KEY (p_key) REFERENCES Pk_databank  (p_key);


CREATE TABLE IF NOT EXISTS league_brief(
    p_key integer NOT NULL PRIMARY KEY,
    bazi integer ,
    tafazol integer ,
    emtiaz character varying);

ALTER TABLE league_brief
    ADD CONSTRAINT fk_league_brief_to_Pk_databank  
    FOREIGN KEY (p_key) REFERENCES Pk_databank   (p_key);

CREATE TABLE IF NOT EXISTS league_complete(
    p_key integer NOT NULL PRIMARY KEY,
    bord integer ,
    mosavi integer ,
    bakht integer ,
    gol integer);


ALTER TABLE league_complete
    ADD CONSTRAINT fk_league_complete_to_Pk_databank  
    FOREIGN KEY (p_key) REFERENCES Pk_databank   (p_key);

    
CREATE TABLE IF NOT EXISTS league_last_five_games(
    p_key integer NOT NULL PRIMARY KEY,
    last_five_games varchar);

ALTER TABLE league_last_five_games
    ADD CONSTRAINT fk_league_last_five_games_to_Pk_databank  
    FOREIGN KEY (p_key) REFERENCES Pk_databank   (p_key);    
"""

