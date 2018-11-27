## `Task`
* taskilla dynaamiset parametrit riippuen ajasta ja riippuvuuksista
* siitä tulee ajoaikainen työn instanssi (`Job`)
   - ajetaan jossain ympäristössä
   - onnistuu, epäonnistuu, yrittää uudelleen
   - ajamisesta (execution) ja vuorottamisesta (scheduling) vastaavat erilliset palvelut
* taskeilla voi olla palvelutasosopimus (SLA)
* `TaskInstance`t generoivat lokitiedostoja, joista voi debugata virheitä