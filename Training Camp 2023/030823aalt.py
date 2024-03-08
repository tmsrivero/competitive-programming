class Nodo:
    def __init__(self):
        self.ave()
        self.finpalabra = False
class Trie:

    def _init_(self):
        self.raiz = Nodo()

    def insert(self, palabra=str) -> None:
        puntero = self.root

        for letra in palabra:
            if letra not in puntero.ave:
                puntero.ave[letra] = Nodo()
            puntero = puntero.ave[letra]
        puntero.finpalabra = True

    def busqueda(self, palabra: str) -> bool:
        puntero = self.raiz
        for letra in palabra:
            if letra not in puntero.ave:
                return False
            puntero = puntero.ave[letra]

    def startsWith(self, prefijo, str) -> bool:
        puntero = self.raiz
        for letra in prefijo:
            if letra not in puntero.ave:
                return False
            puntero = puntero.ave[letra]

        return True

q = int(input())

for i in range(q):
    mn= input().split()
    m = mn[0]
    if len(mn)>1:
        n = mn[1]
    
    if m=="1":
        Trie.insert(0,n)