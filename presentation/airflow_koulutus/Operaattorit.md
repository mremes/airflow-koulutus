## Yleistä

"Stabiilit" moduulit: `airflow.operators`
Yhteisön kehittelemät operaattorit: `airflow.contrib.operators`

* Operaattorit ovat DAG:n työn yksiköitä (solmuja), joita ajetaan DAG:n ajastamaan aikaan. Operaattorit määrittelevät miten ja mitä ajetaan.

* Operaattorien väliset riippuvuussuhteet määritellään DAG-tiedostossa.

* Operaattorit voivat ajaa eri koneilla kun käytetään `CeleryExecutor`ia.