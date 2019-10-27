import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    "CREATE TABLE IF NOT EXISTS DUMMY (NUM INTEGER)",
    "INSERT INTO DUMMY VALUES (42)",
]



def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()

# CREATE TABLES------------------------------------------------------------------------

    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE PERSON (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(40) UNIQUE NOT NULL
        )"""
        cursor.execute(statement)
        cursor.close()  
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE MOVIE (
            ID SERIAL PRIMARY KEY,
            TITLE VARCHAR(80),
            DESCRIPTION VARCHAR,
            YR NUMERIC(4),
            IMDBSCORE FLOAT,
            SCORE FLOAT DEFAULT 0.0,
            VOTES INTEGER DEFAULT 0,
            DIRECTORID INTEGER REFERENCES PERSON (ID)
        )"""
        cursor.execute(statement)
        cursor.close()  
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """CREATE TABLE CASTING (
                MOVIEID INTEGER REFERENCES MOVIE (ID),
                ACTORID INTEGER REFERENCES PERSON (ID),
                ORD INTEGER,
                PRIMARY KEY (MOVIEID, ACTORID)
            )"""
            cursor.execute(statement)

    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE BOOK (
            ID SERIAL PRIMARY KEY,
            TITLE VARCHAR(80),
            DESCRIPTION VARCHAR,
            YR NUMERIC(4),
            PAGENUMBER INTEGER,
            SCORE FLOAT DEFAULT 0.0,
            VOTES INTEGER DEFAULT 0,
            AUTHORID INTEGER REFERENCES PERSON (ID)
        )"""
        cursor.execute(statement)
        cursor.close() 

    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE MUSIC (
            ID SERIAL PRIMARY KEY,
            TITLE VARCHAR(80),
            ALBUM VARCHAR(80),
            YR NUMERIC(4),
            SCORE FLOAT DEFAULT 0.0,
            VOTES INTEGER DEFAULT 0,
            SINGERID INTEGER REFERENCES PERSON (ID)
        )"""
        cursor.execute(statement)
        cursor.close() 
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE USER (
            NAME VARCHAR(80) PRIMARY KEY,
            PASSWORD VARCHAR(80)
        )"""
        cursor.execute(statement)
        cursor.close()  
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE LIST (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(80),
            DATE DATETIME,
            USERID INTEGER REFERENCES USER (ID)
        )"""
        cursor.execute(statement)
        cursor.close()  
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE CONTENT (
            USERID INTEGER REFERENCES LIST (ID),
            MOVIEID INTEGER REFERENCES MOVIE (ID) DEFAULT 0,
            BOOKID INTEGER REFERENCES BOOK (ID) DEFAULT 0,
            MUSICID INTEGER REFERENCES MUSIC (ID) DEFAULT 0,
            PRIMARY KEY (USERID, MOVIEID, BOOKID, MUSICID)
        )"""
        cursor.execute(statement)
        cursor.close()  
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE BOOKGENRES (
            BOOKID INTEGER REFERENCES BOOK (ID),
            GENREID INTEGER REFERENCES GENRES (ID) ,
            PRIMARY KEY (USERID, GENREID)
        )"""
        cursor.execute(statement)
        cursor.close()  
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE GENRES (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(80)
        )"""
        cursor.execute(statement)
        cursor.close()   
    
#INSERT DATA--------------------------------------------------------------------------------------

movie_data = [
    {'title': "The Godfather",
     'description': "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
     'year': 1972,
     'imdb_score': 9.2,
     'score': 8.8,
     'votes': 5,
     'director': "Francis Ford Coppola",
     'cast': ["Marlon Brando", " Al Pacino"]},
    {'title': "The Dark Knight",
     'description': "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
     'year': 2008,
     'imdb_score': 9.0,
     'score': 9.2,
     'votes': 3,
     'director': "Christopher Nolan",
     'cast': ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]},
    {'title': "The Lord of the Rings: The Return of the King",
     'description': "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
     'year': 2003,
     'imdb_score': 8.9,
     'score': 9.0,
     'votes': 2,
     'director': "Peter Jackson",
     'cast': ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"]},
    {'title': "Fight Club",
     'description': "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
     'year': 1999,
     'imdb_score': 8.8,
     'score': 9.5,
     'votes': 4,
     'director': "David Fincher",
     'cast': ["Brad Pitt", "Edward Norton"]},
    {'title': "Forrest Gump",
     'description': "The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.",
     'year': 1994,
     'imdb_score': 8.8,
     'score': 8.0,
     'votes': 1,
     'director': "Robert Zemeckis",
     'cast': ["Tom Hanks"]},
    {'title': "Joker",
     'description': "In Gotham City, mentally-troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego.",
     'year': 2019,
     'imdb_score': 8.9,
     'score': 9.0,
     'votes': 1,
     'director': "Todd Phillips",
     'cast': ["Joaquin Phoenix", "Robert De Niro"]},
    {'title': "Inception",
     'description': "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
     'year': 2010,
     'imdb_score': 8.8,
     'score': 7.9,
     'votes': 4,
     'director': "Christopher Nolan",
     'cast': ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]},
    {'title': "Star Wars: The Empire Strikes Back",
     'description': "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader.",
     'year': 1980,
     'imdb_score': 8.7,
     'score': 8.7,
     'votes': 3,
     'director': "Irvin Kershner",
     'cast': ["Mark Hamill", "Harrison Ford"]},
    {'title': "The Matrix",
     'description': "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
     'year': 1999,
     'imdb_score': 8.7,
     'score': 8.8,
     'votes': 5,
     'director': "Lana Wachowski",
     'cast': ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]},
    {'title': "Saving Private Ryan",
     'description': "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
     'year': 1998,
     'imdb_score': 8.6,
     'score': 8.3,
     'votes': 3,
     'director': "Steven Spielberg",
     'cast': ["Tom Hanks", "Matt Damon"]}
]  

book_data = [
    {'title': "Crime and Punishment",
     'description': "Crime and Punishment is a novel by the Russian author Fyodor Dostoevsky. It was first published in the literary journal The Russian Messenger in twelve monthly installments during 1866. It was later published in a single volume.",
     'year': 1989,
     'page_num': 569,
     'score': 8.7,
     'votes': 3,
     'author': "Fyodor Dostoyevsky",
     'genres': ["Psychological Fiction","Philosophical fiction"]},
    {'title': "The Brothers Karamazov",
     'description': "The Brothers Karamazov, also translated as The Karamazov Brothers, is the final novel by the Russian author Fyodor Dostoevsky. Dostoevsky spent nearly two years writing The Brothers Karamazov, which was published as a serial in The Russian Messenger from January 1879 to November 1880.",
     'year': 1880,
     'page_num': 824,
     'score': 7.5,
     'votes': 2,
     'author': "Fyodor Dostoyevsky",
     'genres': ["Philosophical fiction"]},
    {'title': "Harry Potter and the Philosopher's Stone",
     'description': "Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J. K. Rowling",
     'year': 1997,
     'page_num': 223,
     'score': 7.1,
     'votes': 3,
     'author': "J. K. Rowling",
     'genres': ["Novel","Fantasy Fiction"]},
    {'title': "The Da Vinci Code",
     'description': "The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown. It is Brown's second novel to include the character Robert Langdon: the first was his 2000 novel Angels & Demons",
     'year': 2000,
     'page_num': 689,
     'score': 6.9,
     'votes': 5,
     'author': "Dan Brown",
     'genres': ["Conspiracy fiction"]},
    {'title': "The Metamorphosis",
     'description': "The Metamorphosis is a novella written by Franz Kafka which was first published in 1915. One of Kafka's best-known works, The Metamorphosis tells the story of salesman Gregor Samsa who wakes one morning as an insect.",
     'year': 1915,
     'page_num': 78,
     'score': 7.0,
     'votes': 1,
     'author': "Franz Kafka",
     'genres': ["Fantasy Fiction","Absurdist fiction"]},
    {'title': "Snow",
     'description': "Snow is a postmodern novel by Turkish writer Orhan Pamuk. Published in Turkish in 2002, it was translated into English by Maureen Freely and published in 2004.",
     'year': 2002,
     'page_num': 426,
     'score': 7.1,
     'votes': 3,
     'author': "Orhan Pamuk",
     'genres': ["Novel"]},
    {'title': "The Death of Ivan Ilyich",
     'description': "The Death of Ivan Ilyich, first published in 1886, is a novella by Leo Tolstoy, considered one of the masterpieces of his late fiction, written shortly after his religious conversion of the late 1870s.",
     'year': 1886,
     'page_num': 114,
     'score': 8.0,
     'votes': 1,
     'author': "Leo Tolstoy",
     'genres': ["Novel"]},
    {'title': "Why Nations Fail",
     'description': "Why Nations Fail: The Origins of Power, Prosperity, and Poverty, first published in 2012, is a non-fiction book by Armenian-American economist Daron Acemoglu from the Massachusetts Institute of Technology and British political scientist James A. Robinson from the University of Chicago.",
     'year': 2012,
     'page_num': 546,
     'score': 6.5,
     'votes': 2,
     'author': "Daron Acemoglu",
     'genres': ["Economy"]},
    {'title': "Les Miserables",
     'description': "Les Misérables is a French historical novel by Victor Hugo, first published in 1862, that is considered one of the greatest novels of the 19th century. In the English-speaking world, the novel is usually referred to by its original French title",
     'year': 1862,
     'page_num': 783,
     'score': 7.5,
     'votes': 2,
     'author': "Victor Hugo",
     'genres': ["Historical Fiction","Epic"]},
    {'title': "The Hobbit",
     'description': "The Hobbit, or There and Back Again is a children's fantasy novel by English author J. R. R. Tolkien. It was published on 21 September 1937 to wide critical acclaim, being nominated for the Carnegie Medal and awarded a prize from the New York Herald Tribune for best juvenile fiction.",
     'year': 1937,
     'page_num': 310,
     'score': 7.8,
     'votes': 3,
     'author': "J. R. R. Tolkien",
     'genres': ["Epic","Fantasy Fiction","High fantasy"]}
]

music_data = [
    {'title': "Bohemian Rhapsody",
     'album': "A Night at the Opera",
     'year': 1975,
     'score': 9.2,
     'votes': 4,
     'singer': "Queen"},
    {'title': "Hey Jude",
     'album': "Hey Jude",
     'year': 1968,
     'score': 8.9,
     'votes': 5,
     'singer': "The Beatles"},
    {'title': "Billie Jean",
     'album': "Thriller 25",
     'year': 2008,
     'score': 8.9,
     'votes': 4,
     'singer': "Michael Jackson"},
    {'title': "Like A Rolling Stone",
     'album': "Highway 61 Revisited",
     'year': 1965,
     'score': 8.5,
     'votes': 2,
     'singer': "Bob Dylan"},
    {'title': "Highway to Hell",
     'album': "Highway to Hell",
     'year': 1979,
     'score': 8.0,
     'votes': 1,
     'singer': "AC/DC"},
    {'title': "Skyfall ",
     'album': "Skyfall",
     'year': 2012,
     'score': 7.8,
     'votes': 5,
     'singer': "Adele"},
    {'title': "Umbrella",
     'album': "Good Girl Gone Bad: Reloaded",
     'year': 2008,
     'score': 7.7,
     'votes': 4,
     'singer': "Rihanna"},
    {'title': "Miracles",
     'album': "Shake Shook Shaken",
     'year': 2014,
     'score': 8.0,
     'votes': 1,
     'singer': "The Do"},
    {'title': "Halo",
     'album': "I Am... Sasha Fierce",
     'year': 2008,
     'score': 6.7,
     'votes': 4,
     'singer': "Beyonce"},
    {'title': "Derniere Danse",
     'album': "Mini World",
     'year': 2014,
     'score': 7.5,
     'votes': 2,
     'singer': "Indila"}
]




person_ids = {}
genres_ids = {}
with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in movie_data:
            person_names = [item['director']] + item['cast']
            for name in person_names:
                if name not in person_ids:
                    statement = """INSERT INTO PERSON (NAME) VALUES (%s)
                                   RETURNING id"""
                    cursor.execute(statement, (name,))
                    connection.commit()
                    person_id = cursor.fetchone()[0]
                    person_ids[name] = person_id

with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in book_data:
            if item['author'] not in person_ids:
                statement = """INSERT INTO PERSON (NAME) VALUES (%s)
                                RETURNING id"""
                cursor.execute(statement, (item['author'],))
                connection.commit()
                person_id = cursor.fetchone()[0]
                person_ids[item['author']] = person_id    

with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in music_data:
            if item['singer'] not in person_ids:
                statement = """INSERT INTO PERSON (NAME) VALUES (%s)
                                RETURNING id"""
                cursor.execute(statement, (item['singer'],))
                connection.commit()
                person_id = cursor.fetchone()[0]
                person_ids[item['singer']] = person_id     
                    
with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in book_data:
            genres_names = item['genres']
            for genre in genres_names:
                if genre not in genres_ids:
                    statement = """INSERT INTO GENRES (NAME) VALUES (%s)
                                   RETURNING id"""
                    cursor.execute(statement, (genre,))
                    connection.commit()
                    genre_id = cursor.fetchone()[0]
                    genres_ids[genre] = genre_id



with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in movie_data:
            statement = """
                INSERT INTO MOVIE (TITLE, DESCRIPTION, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID)
                           VALUES (%(title)s, %(description)s, %(year)s, %(imdb_score)s, %(score)s, %(votes)s,
                                   %(directorid)s)
                RETURNING id
            """
            item['directorid'] = person_ids[item['director']]
            cursor.execute(statement, item)
            connection.commit()
            movie_id = cursor.fetchone()[0]

            for actor_ord, actor in enumerate(item['cast']):
                statement = """INSERT INTO CASTING (MOVIEID, ACTORID, ORD)
                                            VALUES (%s, %s, %s)"""
                cursor.execute(statement, (movie_id, person_ids[actor],
                                           actor_ord + 1))
                connection.commit()
                
with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in book_data:
            statement = """
                INSERT INTO BOOK (TITLE, DESCRIPTION, YR, PAGENUMBER, SCORE, VOTES, AUTHORID)
                           VALUES (%(title)s, %(description)s, %(year)s, %(page_num)s, %(score)s, %(votes)s,
                                   %(authorid)s)
                RETURNING id
            """
            item['authorid'] = person_ids[item['author']]
            cursor.execute(statement, item)
            connection.commit()
            book_id = cursor.fetchone()[0]

            for genre in (item['genres']):
                statement = """INSERT INTO BOOKGENRES (BOOKID, GENREID)
                                            VALUES (%s, %s)"""
                cursor.execute(statement, (book_id, genres_ids[genre]))
                connection.commit()

with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        for item in music_data:
            statement = """
                INSERT INTO BOOK (TITLE, ALBUM, YR, SCORE, VOTES, SINGERID)
                           VALUES (%(title)s, %(album)s, %(year)s, %(score)s, %(votes)s,
                                   %(singerid)s)
            """
            item['singerid'] = person_ids[item['singer']]
            cursor.execute(statement, item)
            connection.commit()

def add_user(name, password):
    with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        statement = """
            INSERT INTO USER (NAME, PASSWORD)
                        VALUES (%s, %s)
        """
        cursor.execute(statement, name, password)
        connection.commit()

add_user("ismailak", "12321")
add_user("alperenyucal", "123456")
add_user("azizalsancak", "1923")
add_user("ezgiuzun", "00000")
add_user("enginengin", "123456")

def add_list(name, date,userid):
    with dbapi2.connect(url) as connection:
    with connection.cursor() as cursor:
        statement = """
            INSERT INTO LIST (NAME, DATE, USERID)
                        VALUES (%s, %s, %s)
        """
        cursor.execute(statement, name, date, userid)
        connection.commit()

add_list("Begendiklerim",2019-10-27 12:51:54[.123], 1)
add_list("Begendiklerim",2019-10-27 10:51:12[.123], 2)
add_list("Begendiklerim",2019-10-27 11:21:28[.123], 3)
add_list("Begendiklerim",2019-10-27 08:58:46[.123], 4)
add_list("Begendiklerim",2019-10-27 00:21:25[.123], 5)
add_list("Okuduklarım",2019-10-27 12:52:03[.123], 3)
add_list("İzleyeceklerim",2019-10-27 12:00:59[.123], 1) 
add_list("En İyi Rock",2019-10-27 22:22:54[.123], 2)        

#def fiil_list():


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
