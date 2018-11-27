* Airflow’n sisällä työt (Job) annetaan täytäntöönpanijan (Executor) ajettavaksi määrättyyn aikaan
* Töitä on mm. seuraavanlaisia (tämä ei ole niin olennaista tietoa, mutta auttaa virheiden paikantamisessa jos sellaisia ilmaantuu):
    - `SchedulerJob` – hallitsee yksittäisen aktiivisen DAG:n tahdittamista
    - `BackfillJob` – hallitsee yksittäisen DAG:n ”täyttämistä”
    - `LocalTaskJob` – hallitsee yksittäisen TaskInstance’n ajamista
* Executoreita on seuraavanlaisia:
    - `SequentialExecutor` – ajetaan yhdessä lokaalissa prosessissa peräkkäin (suositellaan vain testikäyttöön)
    - `LocalExecutor` – ajetaan lokaalisti rinnakkain `subprocess` kirjaston avulla
    - `CeleryExecutor` – ajetaan hajautetusti rinnakkain Celeryssä