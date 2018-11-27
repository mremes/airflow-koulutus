![AirflowArchitecture.png](resources/E4CB15522E345C35A37A707415B2CCD4.png =805x616)
https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
# Käyttöliittymä
![AirflowUI.png](resources/A95965FCD6027AE4BE733DC1A31C0AD8.png =1436x602)
* `airflow webserver` käynnistää webpalvelimen, joka avaa käyttöliittymän porttiin 8080 ja kuuntelee porttiin tulevia käskyjä
* käyttöliittymä näyttää metatietokannan tilan
* webpalvelin kirjoittaa käyttäjältä tulevia käskyjä metadatatietokantaan, joista muut Airflow-prosessit (erityisesti `scheduler`) sitten tarvittaessa aktivoituvat
* asetukset määriteltävissä `airflow.cfg`-konfiguraatiotiedostossa
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
# Metadatatietokanta
* Airflow koko tila on säilössä metatietokannassa
* Airflown komponentit lukevat ja kirjoittavat tähän yhteen tietokantaan
* On suositeltavaa käyttää jotain muuta kuin SQLiteä, joka on oletustietokanta
    - tyypillinen kanta on esimerkiksi Postgres, joko itse tai pilvipalvelun hallinoimana

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Scheduler & workers
* käynnistetään komennolla `airflow scheduler`
* etsii työt, joita pitää suorittaa ja asettaa ne suoritettavaksi Executorille, joka sitten hallitsee työprosesseja eli workereita
* käynnistää työt aikataulun mukaisesti sen jälkeen kun schedule_interval on päättynyt
* kun työ on ajastettu ajettavaksi päivittäin, niin työ ajaa päivän loputtua
* varmistaa töiden olevan ajossa tai valmiina kuluvaan kellonaikaan nähden
* kirjoittaa kantaan, jos SLA ei ole täyttynyt
* `airflow.cfg`-konfiguraatiossa määritellään schedulerin ja executorin asetukset



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>





