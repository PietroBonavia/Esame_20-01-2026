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
    def get_nodi(n_album):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                    select distinct a.id as id, a.name as name , count(*) as tot
                    from artist a, album al
                    where a.id = al.artist_id 
                    group by artist_id 
                    having tot >= %s
                    """
        cursor.execute(query, (n_album,))
        for row in cursor:
            result.append((row['id'], row['tot']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_archi():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                        select al1.artist_id as id1, al2.artist_id as id2, count(distinct t1.genre_id ) as peso
                        from album al1, album al2, track t1, track t2
                        where al1.id = t1.album_id and al2.id = t2.album_id 
                              and t1.genre_id = t2.genre_id 
                              and al1.artist_id < al2.artist_id
                        group by al1.artist_id, al2.artist_id 
                        """
        cursor.execute(query)
        for row in cursor:
            result.append((row['id1'], row['id2'], row['peso']))
        cursor.close()
        conn.close()
        return result

