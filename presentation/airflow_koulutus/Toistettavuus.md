* Liittyy kiinteästi idempotenssi-ajatukseen
* Jos huomataan jokin virhe aiemmin kehitetyssä prosessoinnissa tai halutaan lisätä ulostuloparametrien määrää lisäämällä prosessointilogiikkaa, raakadatan pitää olla tallessa jotta voidaan suorittaa uudelleenprosessointi eli **backfill**
* Raakadatan (eli syötteen) pitää olla muuttumatonta, jotta saman operaation ajaminen uudelleen tuottaa saman tuloksen
* Välttämätöntä dataputken toimivuudelle
   - mahdoton operoida, jos esim. double counting- tai muut tilaan liittyvät ongelmat ovat läsnä
* Myös johdetun, prosessoidun datan on oltava muuttumatonta, jos "alavirrassa" (downstream) olevat prosessoinnit ovat riippuvaisia johdetusta datasta