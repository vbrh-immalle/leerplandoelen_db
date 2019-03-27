# Configuratie

## Pipenv instructies

Volgende instructies werden initieel uitgevoerd om o.a. de `Pipfile` te maken:

    pipenv install flask

Om alle modules te installeren uit de pipfile, doe:

    pipenv install

En om uit te voeren wordt overgeschakeld naar de shell waarin alle modules uit `Pipfile` aanwezig zijn:

    pipenv shell

## Maken van de database

Met de parser moet eerst de database-file gemaakt worden!
Zie [Parser](../parser)

## Opmerking over VSCode

Om VSCode goed met pipenv te laten werken, moet de map `webui` als hoofdmap geopend worden in VSCode.
(Dit gebeurt waarschijnlijk op basis v.d. aanwezigheid van `Pipfile` of `Pipfile.lock`.)

VSCode gebruikt graag een **linter**.
De gekozen linter wordt enkel gebruikt in de gekozen Pipenv-omgeving en dus gedownload via de `Pipfile`.

Met het `CTRL+SHIFT+P`-commando `select linter` kan eventueel een andere linter gekozen worden.

De gebruikte linter wordt in de `Pipfile` opgeslagen onder de hoofding `[dev-packages]`.

Om de dev-packages te installeren, doe je:

```
pipenv install --dev
```


# Code

## Main

### Flask opstarten

`Debug=True` wordt meegegeven met de `run`-method van het `app`-object, zodat wanneer `.py`-files
gesaved worden, automatisch de server de files opnieuw zal inladen. We krijgen ook meer foutmeldingen
te zien.

### Routes

De route `/` returnt een string met wat HTML-code.

De route `/competenties` maakt gebruik van de **database-laag** om
objecten terug te krijgen op basis van de **model-classes**.
Deze objecten worden dan aan een eenvoudig HTML-template doorgegeven waarmee we in de browser de competenties weergeven.

De route `/deelcompetenties` werkt gelijkaardig.

De route `/competentie/<nummer>` zal alle deelcompetenties van een competentie tonen.
Deze routes worden in het template gebruikt als doel voor hyperlinks in het competentie-overzicht!

De naamgeving van de routes is bewust kort gehouden omdat dit ook verschijnt in de
publiek zichtbare URL's.

## Database-laag

In `leerplandb.py` wordt de database-laag geïmplementeerd.
Alle data die de applicatie nodig heeft wordt hier met SQL-queries uit de database gehaald
en in objecten gestoken.

De objecten worden gemaakt op basis van zogenaamde **model-classes**.
Deze model-classes maken het werken met de data in Python gemakkelijker dan rechtstreeks
met database-objecten te moeten werken.

In de database-laag kiezen we bij voorkeur voor duidelijke (volledige) functie-namen.

## Probleem: globale variabelen

In een flask-applicatie wordt elke HTTP-request in een aparte thread opgestart.
Hierdoor kunnen geen globale variabelen (zoals voor de database-connectie) gebruikt worden.
Dit geeft dan volgende error:

```
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 20584 and this is thread id 7424.
```

Een eenvoudige oplossing is om bij elk request de database-connectie opnieuw te openen
maar dit is eigenlijk niet aangewezen o.w.v. performantie.

Een betere oplossing is gebruik te maken van het speciale `g`-object dat Flask voorziet.
Dit is een variabele die voor elk request opnieuw gemaakt wordt. Het wordt hier gebruikt
om de database-connectie in op te slaan zodat voor elk request maar 1 connectie met de
database nodig is.

