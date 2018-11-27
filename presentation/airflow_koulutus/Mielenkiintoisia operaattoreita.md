### Koodinajo-operaattorit

Koodinajo-operaattoreilla voi ajaa koodia jossakin ajoympäristössä. Koodi ajetaan joko lokaalisti, kun käytetään `SequentialExecutor`ia tai `LocalExecutor`ia, tai työklusterissa `CeleryExecutor`ia käytettäessä.

#### BashOperator

`BashOperator` ajaa bash-komennon. Komento voi olla esim. jokin Linux-systeemin komento tai jokin koodirepositoriossa oleva Python-skripti, Java-ohjelma tms. komennon triggeröimä käyttöjärjestelmän prosessi.

Sille voi määrittää ympäristömuuttujat `dict`-objektin konstruktoriin antamalla.

`XCom`iin on mahdollista puskea komennon/skriptin viimeinen ulostulorivi.

#### PythonOperator

`PythonOperator` suorittaa funktion (tai tarkemmin, `callable`-objektin) Python-moduulista tai standardikirjastosta.

Konstruktorissa määritetään nimettömät (args) ja nimetyt (kwargs) argumentit.

Omien argumenttien lisäksi on mahdollista tarjota ajonaikainen konteksti, jossa on tietoja DAG-ajon tiedoista (esim. aika, DAG:n nimi jne.). Tutustutaan Airflow-kontekstiin tarkemmin myöhemmin.

On mahdollista tarjota myös templates parametreja ja renderöitäviä tiedostopäätteitä. Tutustutaan näihinkin myöhemmin.

#### DockerOperator
`DockerOperator` mahdollistaa komennon ajamisen Docker-kontin sisällä. Parametrejä ovat Docker-imagen tunniste, ajettava komento, annettujen CPU:iden/muistin määrä, levyt, ympäristömuuttujat, verkkomoodi, sertifikaatit, ...

Voi myös määrittää, tapetaanko Docker-kontti heti kun komento on ajettu. On siis mahdollista ajaa koodia tosi monessa käyttisympäristössä (Linux RHEL, SLES, Ubuntu, Centos, Windows Server)

#### EmailOperator, SlackOperator

Kun sähköpostipalvelin on määritelty konfiguraatiossa, `EmailOperator`illa on mahdollista lähettää sähköpostiviestejä. Tämä on hyödyllistä, kun esimerkiksi halutaan raportoida jonkun ehdollisen työn valmistumisesta. Syötettävät tiedot ovat kuin tavanomaisesta sähköpostista (otsikko, vastaanottaja, ...)

`SlackAPIOperator`illa pystyy kutsumaan mitä tahansa Slack API:n metodeja. 

`SlackAPIOperator`ista on johdettu `SlackAPIPostOperator`, jolla pystyy lähettämään viestin Slack-kanavalle – mikä lienee yleisin use case.

Templatoituina parametreina kanava, lähettäjän nimi, teksti, liitteet jne.

#### SensorOperator
`SensorOperator` kuuntelee toisessa DAG:issa olevaa työtä. Se on suunniteltu erityisesti DAG:ien välisten riippuvuuksien koodaamiseen. Siitä tulee onnistunut kun sen kuuntelema työ onnistuu