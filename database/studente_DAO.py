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

    def getCodinsStudente(self, matr):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT codins FROM iscrizione WHERE matricola = %s"""
        cursor.execute(query, (matr,))

        result = cursor.fetchall()

        cursor.close()
        cnx.close()

        return result

    def getCorso(self, codiCorso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)

        query = """SELECT nome, codins FROM corso WHERE codins = %s"""
        query = cursor.execute(query, (codiCorso,))

        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result