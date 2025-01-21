
```markdown
# Risolutore di Equazioni di Primo e Secondo Grado

Questo script Python permette di risolvere equazioni algebriche di primo e secondo grado, calcolando le soluzioni reali in base ai coefficienti forniti dall'utente.

## Funzionalità

- **Equazioni di primo grado** (forma `b*x + c = 0`): Il programma risolve equazioni di primo grado quando `a = 0`.
- **Equazioni di secondo grado** (forma `a*x² + b*x + c = 0`): Il programma calcola il discriminante (delta) e fornisce le soluzioni reali distinte, coincidenti o nessuna soluzione, a seconda del valore di delta.
- **Interazione utente**: L'utente inserisce i coefficienti dell'equazione e il programma restituisce le soluzioni. L'utente può continuare a risolvere nuove equazioni o terminare il programma.

## Come Usare

1. Clona questo repository o scarica il file `risolutore_equazioni.py`.
2. Esegui il programma con Python:
   ```bash
   python risolutore_equazioni.py
   ```
3. Inserisci i coefficienti `a`, `b` e `c` quando richiesto.
4. Il programma calcolerà le soluzioni dell'equazione e ti permetterà di risolverne altre o di uscire digitando "exit".

## Esempio di Utilizzo

```
Inserisci coefficiente a: 1
Inserisci coefficiente b: -3
Inserisci coefficiente c: 2
Equazione di II grado:
Soluzioni reali e distinte
x1 = 2.0
x2 = 1.0
```

### Opzioni di uscita:
- Puoi uscire dal programma digitando `exit`.

## Requisiti

- Python 3.x
- Nessuna libreria esterna richiesta (utilizza solo la libreria standard `os`).

```
