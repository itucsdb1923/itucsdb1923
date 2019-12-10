import psycopg2 as dbapi2
from settings import DB_URL as url


# Check if the original password matches with the given one
def checkLogin(username, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            try:
                statement = """SELECT PASSWORD FROM USERS WHERE USERNAME = %s"""
                cursor.execute(statement, (username,))
                pw = cursor.fetchone()[0]
                connection.commit()
                return True if pw == password else False
            except:
                return False


def changePassword(username, password, new_password):
    if checkLogin(username, password):
        with dbapi2.connect(url) as connection:
            with connection.cursor() as cursor:
                try:
                    statement = """UPDATE USERS SET PASSWORD = %s WHERE (USERNAME = %s)"""
                    cursor.execute(statement, (new_password, username))
                    connection.commit()
                    return True
                except:
                    return False
    else:
        return False


def createUser(username, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            try:
                statement = """INSERT INTO USERS (USERNAME, PASSWORD) VALUES (%s, %s)"""
                cursor.execute(statement, (username, password))
                return True
            except:
                return False


def createList(name, date, username):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO LIST (NAME, DATE, USERNAME) VALUES (%s, %s, %s)"""
            cursor.execute(statement, (name, date, username))
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


def deleteListItem(type, itemId, listId):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """DELETE {}LIST WHERE (({}ID = %s) AND (LISTID = %s))""".format(
                type, type)
            cursor.execute(statement, (itemId, listId))
            connection.commit()


def getListItems(listId, limit=-1, offset=-1):
    items = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """select bkl.listid, 'book' as itemtype, bk.id as itemid, bk.title, bk.score, bk.imageurl
                            from booklist bkl inner join book bk on bkl.bookid = bk.id where listid = %s 
                            union all
                            select msl.listid, 'music' as itemtype, ms.id as itemid, ms.title, ms.score, ms.imageurl
                            from musiclist msl inner join music ms on msl.musicid = ms.id where listid = %s 
                            union all
                            select mvl.listid, 'movie' as itemtype, mv.id as itemid, mv.title, mv.score, mv.imageurl
                            from movielist mvl inner join movie mv on mvl.movieid = mv.id where listid = %s
                            """

            if limit > 0:
                statement += "limit " + str(limit)
            if offset > 0:
                statement += " offset " + str(offset)

            cursor.execute(statement, (listId, listId, listId))
            data = cursor.fetchall()

            for list_id, item_type, item_id, title, score, image in data:
                items.append({
                    "item_type": item_type,
                    "item_id": item_id,
                    "title": title,
                    "score": score,
                    "image": image
                })

    return items


def getUserLists(username):
    lists = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """select id, "name", date, username from list
                            where username = '""" + username + """' order by date desc"""
            cursor.execute(statement)
            data = cursor.fetchall()
            for id, name, date, username in data:
                list = {"list_id": id, "name": name,
                        "date": date, "user": username,
                        "items": getListItems(id)
                        }
                lists.append(list.copy())

    return lists


def getMovies():
    movies = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, IMAGEURL, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID FROM MOVIE"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, description, image, year, imdb_score, score, votes, director_id in a:
                movie = {"item_id": item_id, "title": title, "description": description, "image": image,
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
            statement = """SELECT ID, TITLE, DESCRIPTION, IMAGEURL, YR, PAGENUMBER, SCORE, VOTES, AUTHORID FROM BOOK"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, description, image, year, page_num, score, votes, author_id in a:
                book = {"item_id": item_id, "title": title, "description": description, "image": image,
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
            statement = """SELECT ID, TITLE, IMAGEURL, ALBUM, YR, SCORE, VOTES, SINGERID FROM MUSIC"""
            cursor.execute(statement)
            a = cursor.fetchall()
            for item_id, title, image, album, year, score, votes, singer_id in a:
                music = {"item_id": item_id, "title": title, "image": image, "album": album,
                         "year": year, "score": score, "votes": votes}
                statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
                cursor.execute(statement, (singer_id,))
                music["singer"] = cursor.fetchone()[0]
                musics.append(music.copy())
    return musics


def getMovie(movie_id):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """SELECT ID, TITLE, DESCRIPTION, IMAGEURL, YR, IMDBSCORE, SCORE, VOTES, DIRECTORID FROM MOVIE WHERE ID = %s"""
            cursor.execute(statement, (movie_id,))
            a = cursor.fetchall()
            (item_id, title, description, image, year,
             imdb_score, score, votes, director_id) = a[0]
            movie = {"item_id": item_id, "title": title, "description": description, "image": image,
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
            statement = """SELECT ID, TITLE, DESCRIPTION, IMAGEURL, YR, PAGENUMBER, SCORE, VOTES, AUTHORID FROM BOOK WHERE ID = %s"""
            cursor.execute(statement, (book_id,))
            a = cursor.fetchall()
            (item_id, title, description, image, year,
             page_num, score, votes, author_id) = a[0]
            book = {"item_id": item_id, "title": title, "description": description, "image": image,
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
            statement = """SELECT ID, TITLE, IMAGEURL, ALBUM, YR, SCORE, VOTES, SINGERID FROM MUSIC WHERE ID = %s"""
            cursor.execute(statement, (music_id,))
            a = cursor.fetchall()
            (item_id, title, image, album, year,
             score, votes, singer_id) = a[0]
            music = {"item_id": item_id, "title": title, "image": image, "album": album,
                     "year": year, "score": score, "votes": votes}
            statement = """SELECT NAME FROM PERSON WHERE (ID = %s)"""
            cursor.execute(statement, (singer_id,))
            music["singer"] = cursor.fetchone()[0]
    return music


def getLists():
    lists = []
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """select id, "name", date, username from list order by date desc"""
            cursor.execute(statement)
            data = cursor.fetchall()
            for id, name, date, username in data:

                list = {"list_id": id, "name": name,
                        "date": date, "user": username,
                        "items": getListItems(id, limit=4)
                        }

                lists.append(list.copy())

    return lists
