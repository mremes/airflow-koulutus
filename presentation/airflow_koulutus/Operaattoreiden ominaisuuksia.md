* Operaattori-instanssi (tarkemmin, `TaskInstance`) voi saada tiloja:
    - `queued` – laitettu jonoon
    - `running` – ajossa
    - `success` – onnistunut, ei virheitä
    - `failed` – epäonnistunut, ei yritetä uudelleen
    - `up_for_retry` – epäonnistunut, mutta yritetään vielä uudestaan
    - `removed` - poistettu
    - `skipped` - ohitettu, kun on ajauduttu toiseen haaraan
    - `shutdown` - tauolla tai muuta hämärää tapahtunut
* Operaattorit voivat olla
    - "perustaoperaattoreita", joissa ajettava Python-koodi on kokonaan omaa käsialaa, 
    - yhdistelmä muita operaattoreita tai
    - yhdistelmä koukkuja (yhteyksiä palveluihin) ja operaattoreita.

* Operaattorit eivät jaa yleensä dataa keskenään, patsi `XCom`in välityksellä. Kuitenkin on suositeltavaa, että tässä tapauksessa yhdistetään operaattorit, sillä `XCom`in kanssa on ollut yhteisön palautteen perusteella ongelmia (allekirjoittanut ei ole joutunut `XCom`ia käyttämään).

* Ne voidaan asettaa altaaseen, jolloin altaan määrittelemän arvon K verran operaattori-instansseja voi olla ajossa samanaikaisesti
    - tällä vältetään esim. tietokantapalvelun kuormittuminen, jos sen käyttöön liittyy quotoja
    - operaattoreille voidaan antaa prioriteetti, jolloin tärkeämmät, korkeamman prioriteetin omaavat työt pääsevät ajoon nopeammin
* Muuten ajossa olevien operaattoreiden määrää rajottaa konfiguraation parallelismi-asetukset