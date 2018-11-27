## Connections
* Connectionit ovat yhteysolioita, joita voi luoda ja muokata käyttöliittymästä

* Niille annetaan palvelusta riippuen osoite, käyttäjätunnus ja salasana, avain

* Hookit antavat connection-olion kutsulla `get_connection()`, joka on yliajettava metodi `BaseHook`-luokassa

* Jos ei halua käyttää käyttöliittymää yhteysolioiden luomiseen, sama onnistuu ympäristömuuttujien avulla (lisätietoja dokumentaatiossa)

## Variables

* Variablet ovat ympäristömuuttujien kaltaisia arvoja, joita voi käyttää koodissa `airflow.models.Variable`-luokan avulla
* `api_key = Variable.get('api key')`
* Hyödyllisyys on siinä, että konfiguraatiota voi muuttaa käyttöliittymästä
* DAG:iin voi lisätä esimerkiksi uusia haaroja `Variable`-arvojen avulla, kuten esimerkistä saamme kohta nähdä

## Poolit
* Poolit rajoittavat töiden rinnakkain ajamista
* Ne ovat hyödyllisiä, kun kohdepalvelussa on jokin rinnakkaisuusrajoitus tai  halutaan muusta syystä käyttää resursseja maltillisesti (esimerkiksi yksi kantakysely kerrallaan)