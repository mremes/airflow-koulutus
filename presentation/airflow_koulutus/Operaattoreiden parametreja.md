* `task_id` - operaattorin tunniste
* `owner` - operaattorin omistaja
* `retries` – uudelleenyritysten määrä (oletus: 0)
* `retry_delay` – uudelleenyritysten välinen aika
* `retry_exponential_backoff` – korotetaanko uudelleenyritysaikaa eksponentiaalisesti
* `start_date` – ensimmäinen päivä kun ajetaan työ (oletus: DAG:n  aloitusaika)
* `end_date` – viimeinen päivä kun ajetaan työ
* `depends_on_past` – edellisen ajosyklin vastaava työ pitää olla ajettuna ennen tämän työn ajamista
* `priority_weight` – prioriteetti
* `sla` – operaattorin palvelutasosopimus (esim. pitää suoriutua 2 minuutissa, muuten lähetetään SLA violation sähköposti)
* `execution_timeout` – maksimi ajoaika, jonka ylittyessä tapetaan työ