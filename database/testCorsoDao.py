from corso_DAO import CorsoDao
from studente_DAO import StudenteDao
# Creazione di un'istanza della classe CorsoDao
daoC = CorsoDao()
daoS = StudenteDao()

# Chiamata del metodo per recuperare i dati

listaCorsi=daoC.getAllNomiCorsi()
print(listaCorsi)





listaSud=daoS.getAllStudenti()
print(listaSud)

matricola_target=int("146101")
for s in listaSud:
    if s['matricola'] == matricola_target:
        studente = s
        print("\n"+str(studente["nome"]))
        break

codiceCorso=daoC.getCodCorso("Economia aziendale")
print(codiceCorso[0])

elencoMatricoleCorso = daoC.getElencoMatricoleCorso("09AQGNG")
for el in elencoMatricoleCorso:
    print(el[0])

studente = daoC.getMatricolaNomeStudente("189920")
print(studente)

codiceCorsi=daoS.getCodinsStudente(154817)
for el in codiceCorsi:
    print(el["codins"])
    corso = daoS.getCorso(el["codins"])
    print(corso)
