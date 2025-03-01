# Descrizione

Progetto di esempio per la configurazione di un progetto in **Python**, utilizzando il gestore di dipendenze **Poetry**.  
[Documentazione ufficiale](https://python-poetry.org/docs/)  
Quest'ultimo è configurato affinchè crei un ambiente virtuale dedicato all'interno della cartella di lavoro.

Il progetto è configurato per avviarlo tramite debug attraverso il file:  
**launch.json**  

# Avvio
Per avviare il progetto dopo averlo scaricato da github è necessario eseguire il comando:  
`poetry install`

Se poetry non è presente è necessario installarlo attraverso:  
`pipx install poetry`

Installate le dipendenze è possibile avviare manualmente con il comando:  
`poetry run python index.py`

O premendo **F5** su vscode

# Docker
Sono infine presenti i files:

- dockerfile
- compose.yml

Se si vuole provare la relativa immagine docker