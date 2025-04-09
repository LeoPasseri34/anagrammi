import copy
from time import time
from functools import lru_cache

class Model:
    def __init__(self):
        self.lista_soluzioni  = []
        self.set_soluzioni = set()

    def calcola_anagrammi(self, parola: str):
        self.lista_soluzioni = []
        self.set_soluzioni = []
        self._ricorsione("", parola)
        return self.set_soluzioni


    @lru_cache(maxsize=None)
    def _ricorsione(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            #print(parziale)
            self.set_soluzioni.add(parziale)
        else:
            for i in range(len(rimanenti)):
                parziale += rimanenti[i]
                #chiamare la ricorsione con parziale e tutte le lettere rimanenti meno lettera
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
                self._ricorsione_list(parziale, nuove_rimanenti)
                parziale = parziale[:-1]


    def calcola_anagrammi_list(self, parola: str):
        self.lista_soluzioni = []
        self._ricorsione_list([], parola)
        #"dog" ['d', 'o', 'g']
        return self.lista_soluzioni


    def _ricorsione_list(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            #print(parziale)
            self.lista_soluzioni.append(copy.deepcopy(parziale))
        else:
            for i in range(len(rimanenti)):
                parziale.append(rimanenti[i])
                #chiamare la ricorsione con parziale e tutte le lettere rimanenti meno lettera
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
                self._ricorsione_list(parziale, nuove_rimanenti)
                parziale.pop()


if __name__ == "__main__":
    model = Model()
    start = time()
    risultato = model.calcola_anagrammi_list("dog")
    end = time()
    print(f"Elapsed time: {end-start}")
    #risultato = model.calcola_anagrammi("casa")
    print(risultato)