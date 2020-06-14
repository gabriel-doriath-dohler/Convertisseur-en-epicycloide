# Convertisseur-en-epicycloide
Convertit des images en un tracé par des épicycloïdes.
# Exemple
## Entrée de l'algorithme
![alt text](https://github.com/gabriel-doriath-dohler/Convertisseur-en-epicycloide/blob/master/ens.png?raw=true)
## Détection des bords
![alt text](https://github.com/gabriel-doriath-dohler/Convertisseur-en-epicycloide/blob/master/edge.png?raw=true)
## Calculs des coefficients de fourier pour approximer la coubre par une épicycloïde
## Comparaison (en haut le bord et en bas l'approximation)
![alt text](https://github.com/gabriel-doriath-dohler/Convertisseur-en-epicycloide/blob/master/comparaison.png?raw=true)
## Instruction geogebra et équation
C0  = 0 + 0ί
C1 = C0 + (0.61749410275725169495 + 1.12206575561274135566ί) * exp(25 / 6416.99270864833943051053 * 2  * π * t * ί)
...
C51 = C50 + (-0.70271751593871312203 + -0.28493089952879047111ί) * exp(-25 / 6416.99270864833943051053 * 2  * π * t * ί)
Circle(C0, C1)
...
Circle(C50, C51)

(0.61749410275725169495 + 1.12206575561274135566ί) * ℯ^(-ί * 
-0.02447869895002211318 * t) + (-0.66518137010441591439 + 
0.56385435838735253888ί) * ℯ^(-ί * -0.02349955099202122658 * t) + 
(1.26617648424503936866 + 0.18130018222649590953ί) * ℯ^(-ί * 
-0.02252040303402034344 * t) + (-0.10972558254946596090 + 
-0.99004464192451335780ί) * ℯ^(-ί * -0.02154125507601946030 * t) + 
(0.04539228208879137610 + -1.04506400561632450952ί) * ℯ^(-ί * 
-0.02056210711801857369 * t) + (-1.98357774787150176188 + 
-1.98718375019058379749ί) * ℯ^(-ί * -0.01958295916001769055 * t) + 
(-1.22623992433158535142 + -3.63975960693253952627ί) * ℯ^(-ί * 
-0.01860381120201680741 * t) + (-3.09287383832376505666 + 
-1.43484957952152369920ί) * ℯ^(-ί * -0.01762466324401592080 * t) + 
(0.64550731691786999988 + -1.79066900230769765479ί) * ℯ^(-ί * 
-0.01664551528601503419 * t) + (-2.37098774692305802603 + 
3.03457033141141341304ί) * ℯ^(-ί * -0.01566636732801415105 * t) + 
(1.08886625444930484896 + -1.90286797259276796446ί) * ℯ^(-ί * 
-0.01468721937001326618 * t) + (1.80804575125393895974 + 
2.29234414521445817314ί) * ℯ^(-ί * -0.01370807141201238304 * t) + 
(0.81864442506716961212 + -2.64535011257180530109ί) * ℯ^(-ί * 
-0.01272892345401149816 * t) + (-0.02265257419999542471 + 
6.36208121336397969259ί) * ℯ^(-ί * -0.01174977549601061329 * t) + 
(-7.52478742067080830225 + 11.95768306581036277692ί) * ℯ^(-ί * 
-0.01077062753800973015 * t) + (6.99270782121453127189 + 
11.01139489879690103180ί) * ℯ^(-ί * -0.00979147958000884527 * t) + 
(-10.70572452964706755552 + 5.53773055338592712360ί) * ℯ^(-ί * 
-0.00881233162200796040 * t) + (-6.12037585499857250682 + 
27.92290993868045845261ί) * ℯ^(-ί * -0.00783318366400707553 * t) + 
(-4.39680485842383372841 + -18.24415517828791877264ί) * ℯ^(-ί * 
-0.00685403570600619152 * t) + (63.56194093980822401591 + 
11.97310189008316605452ί) * ℯ^(-ί * -0.00587488774800530664 * t) + 
(-15.83583414295838842634 + 8.71817306315017148677ί) * ℯ^(-ί * 
-0.00489573979000442264 * t) + (-18.71030526427271567513 + 
70.09679835989204832458ί) * ℯ^(-ί * -0.00391659183200353776 * t) + 
(51.98700297200155517885 + 32.30450942576259620864ί) * ℯ^(-ί * 
-0.00293744387400265332 * t) + (-53.01124751305982130134 + 
122.76192982921277518926ί) * ℯ^(-ί * -0.00195829591600176888 * t) + 
(-209.83418024246932986898 + -42.08182846299330748252ί) * ℯ^(-ί * 
-0.00097914795800088444 * t) + (598.65097422003134397528 + 
704.50538300074617836799ί) * ℯ^(-ί * 0.00000000000000000000 * t) + 
(-165.11961255299476647451 + 27.57292381911753764712ί) * ℯ^(-ί * 
0.00097914795800088444 * t) + (18.52660279230076767476 + 
90.69341295266058011748ί) * ℯ^(-ί * 0.00195829591600176888 * t) + 
(54.02765379276590351765 + -28.12387839445759141199ί) * ℯ^(-ί * 
0.00293744387400265332 * t) + (38.24450047721038004056 + 
18.80113587629733729045ί) * ℯ^(-ί * 0.00391659183200353776 * t) + 
(-2.04510720741146423407 + 5.98567050447153992110ί) * ℯ^(-ί * 
0.00489573979000442264 * t) + (-14.05164423648578519987 + 
-37.59787676776928577738ί) * ℯ^(-ί * 0.00587488774800530664 * t) + 
(-22.18200526134494765529 + 11.38887038454280720146ί) * ℯ^(-ί * 
0.00685403570600619152 * t) + (14.47138420549928561343 + 
-10.96053932083680315657ί) * ℯ^(-ί * 0.00783318366400707553 * t) + 
(1.51629707875983199550 + -1.25704498498223071756ί) * ℯ^(-ί * 
0.00881233162200796040 * t) + (-19.72913067122079056048 + 
-0.95710873616344416259ί) * ℯ^(-ί * 0.00979147958000884527 * t) + 
(-0.61502838642025470239 + -5.59262947084663331054ί) * ℯ^(-ί * 
0.01077062753800973015 * t) + (-12.29747285840462112105 + 
3.77594977743187198982ί) * ℯ^(-ί * 0.01174977549601061329 * t) + 
(8.45231955707887472329 + 9.18800955844080924351ί) * ℯ^(-ί * 
0.01272892345401149816 * t) + (8.22833841954273381702 + 
6.56775505830375028182ί) * ℯ^(-ί * 0.01370807141201238304 * t) + 
(-0.22053222726670368425 + -3.62694492140395974289ί) * ℯ^(-ί * 
0.01468721937001326618 * t) + (3.62100011025873103065 + 
-1.12228160694319334389ί) * ℯ^(-ί * 0.01566636732801415105 * t) + 
(-0.23152439423034981703 + -2.90054948711040294640ί) * ℯ^(-ί * 
0.01664551528601503419 * t) + (0.52763800266539706563 + 
1.24562655372782837837ί) * ℯ^(-ί * 0.01762466324401592080 * t) + 
(-0.72388991611807396165 + 1.82004575110275190752ί) * ℯ^(-ί * 
0.01860381120201680741 * t) + (-1.25279434039505233045 + 
-0.69321852821637419684ί) * ℯ^(-ί * 0.01958295916001769055 * t) + 
(-0.28408458300549488396 + -0.50084262579015903505ί) * ℯ^(-ί * 
0.02056210711801857369 * t) + (0.35879672159309311530 + 
0.17035918878723127490ί) * ℯ^(-ί * 0.02154125507601946030 * t) + 
(-0.09481956447736604454 + -0.10793179224924824566ί) * ℯ^(-ί * 
0.02252040303402034344 * t) + (-0.04382045328931117451 + 
-0.71146118395619217800ί) * ℯ^(-ί * 0.02349955099202122658 * t) + 
(-0.70271751593871312203 + -0.28493089952879047111ί) * ℯ^(-ί * 
0.02447869895002211318 * t)

## Dessin sur geogebra
