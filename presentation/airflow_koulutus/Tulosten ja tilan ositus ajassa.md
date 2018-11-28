* Ratkaisuna kuten idempotenssi-esimerkistä saattoi jo päätelläkin, tulosten (erityisesti taulujen) paloittelu esim. päivän jaksoihin.
* Yksinkertaisesti: tulokset ovat muotoa `taulu_YYYYMMDD`

## Huomioita
* Prosessointityöt eivät saa viitata saman päivän saman taulun partitioon
   - ensimmäisellä ajokerralla taulu on tyhjä
   - toisella ajokerralla tulokseen vaikuttaa edellisen ajon tulos
   - -> ei toistettavaa
* Muutenkin olisi hyvä välttää viittaukset saman taulun edellisiin partitioihin jos se on mitenkään mahdollista
   - kumulatiivisissa metriikoissa tämä on kuitenkin välttämätöntä