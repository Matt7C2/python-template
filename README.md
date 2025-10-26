# python-template

Progetto di esempio per la configurazione di un progetto in **Python**, utilizzando il gestore di dipendenze **Poetry**.  
[Documentazione ufficiale](https://python-poetry.org/docs/)  
Quest'ultimo è configurato affinchè crei un **ambiente virtuale dedicato** all'interno della cartella di lavoro.

Il progetto è configurato per avviarlo tramite debug attraverso il file:  
**launch.json**  

# Struttura
```
PYTHON-TEMPLATE
├── .venv                               -> ambiente virtuale dedicato creato da python
├── .vscode
│   └── launch.json
├── docker
│   ├── compose-prod.yml
│   └── compose.yml
├── src
│   ├── utils
│   ├── utils2
│   └── index.py                        -> file di partenza del progetto
├── .dockerignore
├── .env                                -> copiato da file .env.example
├── .env.example
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── python-template.code-workspace
└── README.md
```

# Fork
Una volta forkato il progetto è sufficiente a aprirlo con vs code e ricercare:  
`python-template`  

Sostituendolo con il nome desiderato.

Per avviare il progetto dopo averlo scaricato da github è necessario eseguire il comando:  
`poetry install`

Se poetry non è presente è necessario installarlo attraverso:  
`pipx install poetry`

Installate le dipendenze è possibile avviare manualmente con il comando:  
`poetry run python src/index.py`

O premendo **F5** su vscode

## Creazione di un progetto da zero
`poetry init`  
Per inizializzare il progetto. Verranno creati i relativi file di inizializzazione, tra cui **peoject.toml**

`poetry add nome_libreria`  
Per aggiungere una libreria pubblica o privata

## Docker
Sono presenti due file per poter gestire il progetto in un container.

**Dockerfile**  
Contiene le istruzioni per creare l'immagine.  
Per creare l'immagine dalla cartella docker:
`docker image build -t ghcr.io/matt7c2/python-template .`

Per pushare:  
`docker image push ghcr.io/matt7c2/python-template .`

**compose.yml**  
Per avviare il container buildando direttamente l'immagine dal Dockefile.

Dalla cartella root:  
`docker image build -t ghcr.io/matt7c2/python-template -f docker/Dockerfile .`

O senza la build, sfruttando il compose:

* Da dentro la cartella docker:  
`docker compose up --build`

 * Da dentro la cartella root:  
`docker compose -f docker/compose.yml up --build`
