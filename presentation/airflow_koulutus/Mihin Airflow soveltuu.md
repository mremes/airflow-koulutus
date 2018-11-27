* Extract-Transform-Loadin toteutus
   - Extract – Airflow'n avulla on helppo yhdistää erilaisiin tietokantahallintasysteemeihin
   - Transform – esim. Pythonin dataprosessointi kirjastot kuten `pandas` helposti käytettävissä – unohtamatta, että Airflow tarjoaa rajapinnat missä tahansa ajoympäristössä ajettuun ohjelmaan Dockerin avulla
   - Load – Yhtä helppoa kuin datan lataaminen
* Extract-Transform-Loadin **orkestrointi**
    - ei tehdä mitään työtä omalla raudalla vaan tehdään kaikki datan siirtely ja prosessointi pilvipalveluissa ja pilvipalveluiden välillä
    - laaja kirjo pilvipalveluiden rajapintoja
* Eräajo-tyyliin ajettujen ohjelmien/skriptien monitorointi ja hallinnointi
    - soveltuu täysin `cron`in korvaajaksi
    - versionhallinnoitavissa
* Raportointi
    - rajapinnat sähköpostipalvelimeen, Slackiin, JIRA:an,...
    - taulujen luonti visualisointityökaluja varten
* Data-analyysin tarvitsemien datasettien luominen
   - Airflow soveltuu hyvin data-analyysin ja koneoppimisen automatisoitavissa olevien vaiheiden mallintamiseen (datan keruu, datan puhdistaminen, datan muovaaminen, muovatun datan syöttäminen malliin, mallin testaus, ...)
   - yleinen totuus on, että data scientistit käyttävät 80% datan puhdistukseen ja 20% analyysin tekemiseen