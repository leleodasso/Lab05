# Add whatever it is needed to interface with the DB Table corso
from networkx.classes import selfloop_edges
import UI.view as view
from database.DB_connect import get_connection, DBConnect


class CorsoDao:

    def getAllNomiCorsi(self):
        cnx=get_connection()
        cursor = cnx.cursor()

        query = """select nome from corso"""
        cursor.execute(query)

        nomiCorsi=[]
        for row in cursor:
            nomiCorsi.append(row[0])

        cursor.close()
        cnx.close()
        return nomiCorsi

    def getCodCorso(self, nomeCorso):
        cnx = get_connection()
        cursor = cnx.cursor(buffered=True)

        query = """SELECT codins FROM corso WHERE nome = %s"""
        cursor.execute(query, (nomeCorso,))

        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result

    def getElencoMatricoleCorso(self, codCorso):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = """SELECT matricola FROM iscrizione WHERE codins = %s"""
        cursor.execute(query, (codCorso,))

        result = cursor.fetchall()

        cursor.close()
        cnx.close()

        return result

    def getMatricolaNomeStudente(self, matric):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = """SELECT nome, cognome, matricola FROM studente WHERE matricola = %s"""
        cursor.execute(query, (matric,))

        result = cursor.fetchall()

        cursor.close()
        cnx.close()

        return result







