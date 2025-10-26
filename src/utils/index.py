from datetime import datetime

# Metodo pubblico (senza underscore)
def getDateString():
    return datetime.strftime(_getDate(),"%Y/%m/%d %H:%M:%S")

# Metodo privato (con undescore): non viene suggerito ma è comunque utilizzabile
def _getDate():
    return datetime.now()

# Se una funzione non è inclusa in __all__, non viene importata con from modulo import *, ma può ancora essere importata direttamente.
__all__ = ["getDateString"]
