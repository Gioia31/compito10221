
'''
Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo. Scrivi un programma che comprenda due funzionalità
- L'operazione per registrare i dati dei partecipanti;
- L'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si
tratta dei nomi dell'elenco, eliminando quelli ai quali la lettera è già stata inviata e che sono registrati
in un apposito elenco. La funzione che produce l'elenco deve anche aggiornare l'elenco dei partecipanti 
ai quali è già stata inviata la lettera.
'''
partecipanti = []
orario_di_prenotazione = []
lista = {}
lettera_spedita = []
lettera_non_spedita =[]
n = 0

n_partecipanti = int(input("Inserisci il numero di partecipanti al convegno "))

for persona in range(n_partecipanti):
    nome = input("Inserisci il nome del partecipante ")
    partecipanti.append(nome)

for persona in partecipanti:
    n+=1
    lista[n] = persona
print(lista)

for persona in partecipanti:
    spedizione_lettera = input("E' stata mandata la lettera a: " + persona + "? ")

    if spedizione_lettera.upper() == "SI" or spedizione_lettera.upper() == "SÌ":
        lettera_spedita.append(persona)
    else:
        lettera_non_spedita.append(persona)
        
print("E' stata mandata la lettera di conferma a: ", lettera_spedita, )
print("Non è stata mandata la lettera di conferma a: ", lettera_non_spedita)
