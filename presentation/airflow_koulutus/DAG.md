* kokoelma tehtäviä, jotka halutaan ajaa jossain tietyssä järjestyksessä, tietyillä ehdoilla
* Directed Acyclic Graph, suunnattu syklitön verkko
   - yksittäisessä solmussa vieraillaan enintään kerran
   - solmut järjestetty topologisesti
   - riippuvuudet suoritetaan ensin
* DAG:n avulla mallinnetaan työnkulun töiden järjestys ja riippuvuussuhteet
* DAG:t ajastetaan ajettavaksi johonkin aikaan (cron-tyyliin, esim. päivittäin tai joka toinen tunti varttia yli)

# DAG:it koodina
* konfiguraatio Python-koodina
* data scientisteilla ja muilla ei-softadevaajilla matalampi kynnys automatisoida töitään ja laittaa johonkin aikaan ajettavaksi
    - saattaa vaatia data engineerin tekemään viimeisen silauksen tekemisen työlle, mutta speksi on paljon helpommin kuvattavissa DAG:ien avulla
* Pythonin laaja kirjastojen kirjo – joka on tuttu data scientisteille – käytettävissä
* itse laskenta voidaan suorittaa muussa ympäristössä tai palvelussa
* kattavat API:t pilvipalveluihin

```python

import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

args = dict(owner='matti',
            start_date=airflow.utils.dates.days_ago(2))

dag = DAG(dag_id='example', 
          default_args=args, 
          schedule_interval='0 0 * * *')

run_me_first = BashOperator(task_id='run_me_first', 
                            bash_command='echo "Let\'s start!"', 
                            dag=dag)

run_me_last = DummyOperator(task_id='run_me_last', dag=dag)

for i in range(3):
    task_id = 'i_am_{}_in_the_loop'.format(str(i))
    cmd = 'echo "I am task number {}." && sleep 1'.format(str(i))
    
    task = BashOperator(task_id=task_id, 
                        bash_command=cmd,
                        dag=dag)
    
    run_me_first >> task
    task >> run_me_last
```
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

![Screen Shot 2018-11-27 at 19.29.12.png](resources/A5E0CEB97423F36A30E146EEA1598569.png =880x400)
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>