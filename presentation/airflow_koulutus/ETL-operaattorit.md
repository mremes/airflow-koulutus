ETL-operaattoreilla suoritetaan kantakyselyjä (SQL, HQL) tai datansiirto-operaatioita (MSSQL -> MYSQL, S3 -> Redshift jne.)

Näistä vain pieni osa on `airflow.operators` moduulissa. Valtaosa on `airflow.contrib.operators` moduulissa. Tarkastellaan muutama mielenkiintoinen tapaus.

### JdbcOperator
`JdbcOperator` ajaa SQL-skriptin JDBC-ajuria käyttäen. JDBC-ajuri löytyy valtaosaan käytössä olevista tietokannoista.

SQL:n voi syöttää joko suoraan tekstinä konstruktoriin tai antamalla `.sql`-templaattitiedoston osoite, jonka perusta määritellään DAG-konfiguraatiossa (`templates_path`). Kuten päätellä saattaa, SQL:t ovat templatoitavia.

# MongoTOS3Operator
Siirretään MongoDB-NoSQL-kannasta tieto S3-blobiin. Annetaan Mongon tiedot (connection id, collection, query) ja S3:n tiedot (connection id, bucket, key). Mongo-queryn voi määritellä pipelinena eli ajetaan useampi query peräkkäin ja tallennetaan viimeisin.