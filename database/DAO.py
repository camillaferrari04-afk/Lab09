from database.DB_connect import DBConnect
from model.airport import Airport

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getallairports():

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res=[]

        query ="""SELECT *
                    FROM airports"""

        cursor.execute(query)

        for row in cursor:
            res.append(Airport(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getedges(distmedia):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res = []

        query = """SELECT 
                    IF(f.ORIGIN_AIRPORT_ID < f.DESTINATION_AIRPORT_ID, f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS air1,
                    IF(f.ORIGIN_AIRPORT_ID < f.DESTINATION_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, f.ORIGIN_AIRPORT_ID) AS air2,
                    AVG(f.DISTANCE) AS peso
                FROM 
                    flights f
                GROUP BY 
                    air1, air2
                HAVING 
                    peso > %s"""

        cursor.execute(query, (distmedia,))

        for row in cursor:
            res.append({
            "air1": row["air1"],
            "air2": row["air2"],
            "weight": row["peso"]
            })

        cursor.close()
        cnx.close()

        return res