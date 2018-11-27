* työnkulkujen (workflow) luomiseen, ajastamiseen ja hallinnointiin tarkoitettu alusta
* työnkulut määritellään Python-koodina
* työnkulut ajastetaan niin ikään koodissa käyttäen tuttuja cron-aikatauluja (kerran tunnissa, kerran päivässä, 15 yli joka toinen tunti, jne.)
* työnkulkuja hallinnoidaan pääasiallisesti käyttöliittymän avulla
    - mahdollista toteuttaa suurin osa hallinnointitoimenpiteistä myös komentoriviliittymän avulla, mikä mahdollistaa makrojen tekemisen ja tallentamisen versionhallintaan
<br>
<br>
<br>
<br>
<br>
<br>

# Historia
* Maxime Beauchemin, Airbnb, 2006
* Lähdekoodi avointa alusta saakka
* ASF-projektiksi vuoden 2017 alussa
* +5600 committia, 99 releasea (viimeisin 6 päivää sitten), +10K tähteä GitHubissa
* https://github.com/apache/incubator-airflow#who-uses-apache-airflow
<br>
<br>
<br>
<br>
<br>
<br>

# Miksi Airflow on hyödyllinen?
* vaikka alusta on Python-pohjainen, sillä pystyy ajamaan käytännössä _mitä tahansa_ koodia (esim. Dockerissa)
* **alusta siis toimii liimana erinäisten dataa sekä tuottavien applikaatioiden että dataa säilövien siilojen välillä**
* näiden yhdistäminen voi olla monimutkainen prosessi, mutta sen kuvaamiseen auttaa *riippuvuusverkko*, joka on Airflow'n olennainen konsepti (palataan kohta tähän)
<br>
<br>
<br>
<br>
<br>
<br>

