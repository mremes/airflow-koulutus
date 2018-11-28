* Idempotenssi tarkoittaa sitä, että saman työn ajaminen uudelleen ja uudelleen tuottaa aina saman tuloksen riippumatta siitä, kuinka monta kertaa työ ajetaan
* Idempotenssi liittyy kiinteästi funktionaalisen ohjelmoinnin ajatukseen funktion puhtaudesta ja sivuvaikutuksettomuudesta

* Ei-idempotentti funktio:
```js
int counter = 0;
int get_next() {
  return ++counter;
}
```
* Idempotentti funktio:

```
int get_next(int counter) {
  return counter + 1;
}
```

* Idempotenteilla operaatioilla vältetään palautusten (rollback) tarve
   - vrt. pseudo-SQL-lauseita:
   
   ```sql
   UPDATE person
   SET age = age + 1
   WHERE birthday = today
   ```
   
   ```sql
   INSERT INTO person_{today}
   SELECT name, birthday, IF(birthday = today, age + 1, age)
   FROM person
   ```
   
   - jos 1. esimerkin taulu halutaan palauttaa siihen tilaan, missä taulu oli 5 päivää sitten, se vaatii melko monimutkaista rollback-logiikkaa (pitää kehittää käänteiset kyselyt)
   - sen lisäksi, jos ajetaan 1. esimerkin operaatio kaksi kertaa, päädytään virheelliseen tulokseen (double counting)
   - 2. esimerkin tapauksessa riittää, että haetaan `person_{today - 5 päivää}` -taulu
   - double counting -ongelmaa ei esiinny 2. esimerkin tapauksessa
   
* Eli vielä kerran: `UPDATE`-, `APPEND`- ja `DELETE`-operaatiot ovat **vaarallisia**, koska ne **muuttavat tilaa**
* Suositaan siis yliajamista ja redudanssia – sillä on toki olemassa seuraavaksi esiteltävä vaihtoehtoiskustannus

* Idempotenssin heikkous datan prosessoinnin tapauksessa:
   - joudutaan käyttämään tilaa historian tallentamiseen
    - toisaalta, tiedon säilytys on melkoisen halpaa nykypäivänä
    - historiatiedon säilytys on tosin koettu tarpeelliseksi analytiikkaa varten