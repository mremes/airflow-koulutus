## Yleistä

Templatoinnin avulla voidaan luoda ajettavasta työstä parametrisoitu, jolloin ajettavan ohjelman argumentit, ajettava SQL-query tms. perustuu ajoon tai DAG:iin liittyviin parametreihin.

Airflow tarjoaa käyttäjälle juurikin ajoon liittyviä muuttujia:
* `{{ ds }}` – ajopäivä muodossa YYYY-MM-DD
* `{{ next_ds }}` – edellinen _ajopäivä_ samassa muodossa
   - eli jos ajetaan kerran viikossa niin `next_ds` on ds - delta\_7\_päivää
* `{{ yesterday_ds }}` – ajopäivää _edeltävä päivä_ samassa muodossa
* `{{ ds_nodash }}` – ajopäivä muodossa YYYYMMDD
* `{{ var.api_key }}` – variable `api_key`
* ...

... ja funktioita (makroja):
* `{{ macros.ds_add }}` – lisää päivään delta\_n\_päivää
* `{{ macros.time }}` – aikamoduuli
* ...