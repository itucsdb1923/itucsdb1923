import psycopg2 as dbapi2
from settings import DB_URL as url


def checkLogin(name, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            try:
                statement = """SELECT PASSWORD FROM USERS WHERE NAME = %s"""
                cursor.execute(statement, (name,))
                p = cursor.fetchone()[0]
                connection.commit()
                return True if p == password else False
            except:
                return False

def createUser(name, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO USERS (NAME, PASSWORD) VALUES (%s, %s)"""
            cursor.execute(statement, (name, password))


def createList(name, date, userid):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO LIST (NAME, DATE, USERID) VALUES (%s, %s, %s)"""
            cursor.execute(statement, (name, date, userid))
            connection.commit()


def getMovies():
    movies = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID FROM MOVIE"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, description, year, imdb_score, score, votes, director_id in a:
                x = {"item_id": item_id, "title": title, "description": description,
                     "year": year, "imdb_score": imdb_score, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (director_id,))
                x["director"] = cursor.fetchone()[0]
                statement = """SELECT NAME FROM PERSON JOIN CASTING ON (CASTING.ACTORID = PERSON.ID) WHERE (MOVIEID = %s)"""
                cursor.execute(statement, (item_id,))
                cast = cursor.fetchall()
                a = []
                for c in cast:
                    a.append(c[0])
                x["cast"] = a
                movies.append(x.copy())
                print('  {}'.format(movies))
    return movies


def getBooks():
    books = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, PAGENUMBER, SCORE, VOTES, AUTHORID FROM BOOK"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, description, year, page_num, score, votes, author_id in a:
                x = {"item_id": item_id, "title": title, "description": description,
                     "year": year, "page_num": page_num, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (author_id,))
                x["author"] = cursor.fetchone()[0]
                statement = """SELECT NAME FROM GENRE JOIN BOOKGENRE ON (BOOKGENRE.GENREID = GENRE.ID) WHERE (bOOKID = %s)"""
                cursor.execute(statement, (item_id,))
                cast = cursor.fetchall()
                a = []
                for c in cast:
                    a.append(c[0])
                x["genre"] = a
                books.append(x.copy())
                print('  {}'.format(books))
    return books


def getMusics():
    musics = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, ALBUM, YR, SCORE, VOTES, SINGERID FROM MUSIC"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, album, year, score, votes, singer_id in a:
                x = {"item_id": item_id, "title": title, "album": album,
                     "year": year, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (singer_id,))
                x["singer"] = cursor.fetchone()[0]
                musics.append(x.copy())
                print('  {}'.format(musics))
    return musics


def getMovie(movie_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID FROM MOVIE WHERE ID = %s"""
            cursor.execute(statement, (movie_id,))
            a = cursor.fetchall()
            (item_id, title, description, year,
             imdb_score, score, votes, director_id) = a[0]
            x = {"item_id": item_id, "title": title, "description": description,
                 "year": year, "imdb_score": imdb_score, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (director_id,))
            x["director"] = cursor.fetchone()[0]
            statement = """SELECT NAME FROM PERSON JOIN CASTING ON (CASTING.ACTORID = PERSON.ID) WHERE (MOVIEID = %s)"""
            cursor.execute(statement, (item_id,))
            cast = cursor.fetchall()
            a = []
            for c in cast:
                a.append(c[0])
            x["cast"] = a
            print('  {}'.format(x))
    return x


def getBook(book_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, PAGENUMBER, SCORE, VOTES, AUTHORID FROM BOOK WHERE ID = %s"""
            cursor.execute(statement, (book_id,))
            a = cursor.fetchall()
            (item_id, title, description, year,
             page_num, score, votes, author_id) = a[0]
            x = {"item_id": item_id, "title": title, "description": description,
                 "year": year, "page_num": page_num, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (author_id,))
            x["author"] = cursor.fetchone()[0]
            statement = """SELECT NAME FROM GENRE JOIN BOOKGENRE ON (BOOKGENRE.GENREID = GENRE.ID) WHERE (bOOKID = %s)"""
            cursor.execute(statement, (item_id,))
            cast = cursor.fetchall()
            a = []
            for c in cast:
                a.append(c[0])
            x["genre"] = a
            print('  {}'.format(x))
    return x


def getMusic(music_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, ALBUM, YR, SCORE, VOTES, SINGERID FROM MUSIC WHERE ID = %s"""
            cursor.execute(statement, (music_id,))
            a = cursor.fetchall()
            (item_id, title, album, year, score, votes, singer_id) = a[0]
            x = {"item_id": item_id, "title": title, "album": album,
                 "year": year, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (singer_id,))
            x["singer"] = cursor.fetchone()[0]
            print('  {}'.format(x))
    return x


def getLists():
    lists = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, NAME, DATE, USERID FROM LIST ORDER BY DATE DESC"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, name, date, user_id in a:
                x = {"item_id": item_id, "name": name, "date": date}
                statement = """SELECT NAME FROM USERS WHERE (ID = %s)"""
                cursor.execute(statement, (user_id,))
                x["user"] = cursor.fetchone()[0]
                lists.append(x.copy())
                print('  {}'.format(lists))
    return lists
