import psycopg2 as dbapi2
from settings import DB_URL as url


# Check if the original password matches with the given one
def checkLogin(username, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            try:
                statement = """SELECT PASSWORD FROM USERS WHERE NAME = %s"""
                cursor.execute(statement, (username,))
                pw = cursor.fetchone()[0]
                connection.commit()
                return True if pw == password else False
            except:
                return False


def createUser(username, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO USERS (NAME, PASSWORD) VALUES (%s, %s)"""
            cursor.execute(statement, (username, password))


def createList(name, date, userid):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO LIST (NAME, DATE, USERID) VALUES (%s, %s, %s)"""
            cursor.execute(statement, (name, date, userid))
            connection.commit()


# add a list item with given type to a list.
# type should be one of these: "BOOK", "MUSIC", "MOVIE"
def addListItem(type, itemId, listId):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO {}LIST ({}ID, LISTID) VALUES (%s, %s)""".format(
                type, type)
            cursor.execute(statement, (itemId, listId))
            connection.commit()


def getList(listId):
    response = {"list_id": listId, "items": []}
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """select 'bk-' || cast(bkl.bookid as varchar(10)) as itemid, bk.title, bk.score
                            from booklist bkl inner join book bk on bkl.bookid = bk.id where listid = %s 
                            union all
                            select 'ms-' || cast(msl.musicid as varchar(10)) as itemid, ms.title, ms.score
                            from musiclist msl inner join music ms on msl.musicid = ms.id where listid = %s 
                            union all
                            select 'mv-' || cast(mvl.movieid as varchar(10)) as itemid, mv.title, mv.score
                            from movielist mvl inner join movie mv on mvl.movieid = mv.id where listid = %s"""

            cursor.execute(statement, (listId, listId, listId))
            data = cursor.fetchall()

            for item_id, title, score in data:
                response["items"].append({
                    "item_id": item_id,
                    "title": title,
                    "score": score,
                })

    return response


def getMovies():
    movies = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID FROM MOVIE"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, description, year, imdb_score, score, votes, director_id in a:
                movie = {"item_id": item_id, "title": title, "description": description,
                         "year": year, "imdb_score": imdb_score, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (director_id,))
                movie["director"] = cursor.fetchone()[0]
                statement = """SELECT NAME FROM PERSON JOIN CASTING ON (CASTING.ACTORID = PERSON.ID) WHERE (MOVIEID = %s)"""
                cursor.execute(statement, (item_id,))
                cast = cursor.fetchall()
                a = []
                for c in cast:
                    a.append(c[0])
                movie["cast"] = a
                movies.append(movie.copy())
    return movies


def getBooks():
    books = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, PAGENUMBER, SCORE, VOTES, AUTHORID FROM BOOK"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, description, year, page_num, score, votes, author_id in a:
                book = {"item_id": item_id, "title": title, "description": description,
                        "year": year, "page_num": page_num, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (author_id,))
                book["author"] = cursor.fetchone()[0]
                statement = """SELECT NAME FROM GENRE JOIN BOOKGENRE ON (BOOKGENRE.GENREID = GENRE.ID) WHERE (bOOKID = %s)"""
                cursor.execute(statement, (item_id,))
                cast = cursor.fetchall()
                a = []
                for c in cast:
                    a.append(c[0])
                book["genre"] = a
                books.append(book.copy())
    return books


def getMusics():
    musics = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, ALBUM, YR, SCORE, VOTES, SINGERID FROM MUSIC"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, album, year, score, votes, singer_id in a:
                music = {"item_id": item_id, "title": title, "album": album,
                         "year": year, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (singer_id,))
                music["singer"] = cursor.fetchone()[0]
                musics.append(music.copy())
    return musics


def getMovie(movie_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID FROM MOVIE WHERE ID = %s"""
            cursor.execute(statement, (movie_id,))
            a = cursor.fetchall()
            (item_id, title, description, year,
             imdb_score, score, votes, director_id) = a[0]
            movie = {"item_id": item_id, "title": title, "description": description,
                     "year": year, "imdb_score": imdb_score, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (director_id,))
            movie["director"] = cursor.fetchone()[0]
            statement = """SELECT NAME FROM PERSON JOIN CASTING ON (CASTING.ACTORID = PERSON.ID) WHERE (MOVIEID = %s)"""
            cursor.execute(statement, (item_id,))
            cast = cursor.fetchall()
            a = []
            for c in cast:
                a.append(c[0])
            movie["cast"] = a
    return movie


def getBook(book_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, YR, PAGENUMBER, SCORE, VOTES, AUTHORID FROM BOOK WHERE ID = %s"""
            cursor.execute(statement, (book_id,))
            a = cursor.fetchall()
            (item_id, title, description, year,
             page_num, score, votes, author_id) = a[0]
            book = {"item_id": item_id, "title": title, "description": description,
                    "year": year, "page_num": page_num, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (author_id,))
            book["author"] = cursor.fetchone()[0]
            statement = """SELECT NAME FROM GENRE JOIN BOOKGENRE ON (BOOKGENRE.GENREID = GENRE.ID) WHERE (bOOKID = %s)"""
            cursor.execute(statement, (item_id,))
            cast = cursor.fetchall()
            a = []
            for c in cast:
                a.append(c[0])
            book["genre"] = a
    return book


def getMusic(music_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, ALBUM, YR, SCORE, VOTES, SINGERID FROM MUSIC WHERE ID = %s"""
            cursor.execute(statement, (music_id,))
            a = cursor.fetchall()
            (item_id, title, album, year, score, votes, singer_id) = a[0]
            music = {"item_id": item_id, "title": title, "album": album,
                     "year": year, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (singer_id,))
            music["singer"] = cursor.fetchone()[0]
    return music


def getLists():
    lists = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, NAME, DATE, USERID FROM LIST ORDER BY DATE DESC"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, name, date, user_id in a:
                list = {"item_id": item_id, "name": name, "date": date}
                statement = """SELECT NAME FROM USERS WHERE (ID = %s)"""
                cursor.execute(statement, (user_id,))
                list["user"] = cursor.fetchone()[0]
                lists.append(list.copy())
    return lists
