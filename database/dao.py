from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artisti_nodi(n_album):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select a.id, count(*) as num_album
                from artist a, album al
                where a.id = al.artist_id 
                group by a.id 
                having num_album >= %s
                """
        cursor.execute(query, (n_album, ))
        for row in cursor:
            result.append((row['id'], row['num_album']))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def get_archi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct a1.id as a1, a2.id as a2
                from artist as a1, artist as a2, track t1, track t2, album as al1, album as al2
                where a1.id != a2.id and a1.id = al1.artist_id  and a2.id = al2.artist_id and al1.id = t1.album_id and al2.id = t2.album_id 
                and t1.genre_id = t2.genre_id 
                group by a1.id, a2.id
                """
        cursor.execute(query)
        for row in cursor:
            result.append((row['a1'], row['a2']))
        cursor.close()
        conn.close()
        return result

