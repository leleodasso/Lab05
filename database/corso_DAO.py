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




