## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

Pridal som model Random FOrest classifier (v main.py - pri komentaroch #Uloha1)

Pre ladenie  parametrov som pouzil grid search s parametrami:
n_estimators: 50, 100,200
max_depth : none,5,10
min_samples_split: 2,5,10
min_samples_leaf : 1,2,4


### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Doplnil som metriku PRecision - vyjadruje podiel spravne klasivikovanych pozitivnych pripadov zo vsetkych, ktore boli oznacene ako pozitivne
Zmeny som robil v main.py , experiment.py , model_trainer.py ...ak som na nic nezabudol, tak vsetky vsetky su vzdy pri komentu #uloha2 
### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.
Grafy vytvorene pocas behu sa ukladaju do saved_plots priecinku
uprava  a pridanie definicie v base_plotter.py a experiment_plotter.py pod #uloha3 poznamkami
### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

pocet replikacii som dal na 30
Oba modely dosahuju vysoke hodnoty vsetkych metrik.
Logistic Regresion  ich dosahuje vo vacsine o trochu lepsie a stabilnejsie nez Random frorest.
Z grafov hustoty rozdelenia vidiet ako hodnoty pri logistic regression su posunute viac doprava cize vyssia prenost a skore.
Matice vyjadruju ze random forest robi viac chyb typu false negative oproti Logistic regression
V zavere Logistic regression ma lepsie hodnoty ,cize je to vhodnejsi model

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
