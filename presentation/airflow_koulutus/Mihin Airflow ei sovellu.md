* Tosiaikasovellukset
   - töiden käynnistäminen kestää sekunteja
   - peräkkäisten ajojen välinen aika on minimissään yksi minuutti (`*/1 * * * *`)
* Yksinkertaiset sovellukset
   - ei liene kannattavaa pystytää systeemiä, jos on vain yksi eräajettava skripti
   - `cron` riittää tähän
* Airflow on kompromissi
  - läpinäkyvyys, monialustaisuus, hallittavuus > nopeus