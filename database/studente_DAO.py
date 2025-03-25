# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection

class StudenteDao:
    def getAllStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = f"""select * from studente"""
        cursor.execute(query)

        nomiStudenti = []
        for row in cursor:
            nomiStudenti.append(row)

        cursor.close()
        cnx.close()
        return nomiStudenti