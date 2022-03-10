[English below](#beta-anonymizer)

# Anonymeiddiwr Beta

Pwrpas yr anonymeiddiwr hwn yw tynnu gwybodaeth bersonol allan o ddata Cymraeg, yn ogystal ag allan o ddata cyfochrog Saesneg-Cymraeg megis cofion cyfieithu. Y nod yw hwyluso rhannu a dosbarthu data hwnnw at ddibenion hyfforddi modelau iaith (gan gynnwys modelau cyfieithu peirianyddol) drwy leddfu pryderon ynglŷn â rhannu data cyffredinol sy'n cynnwys enwau pobl, enwau lleoedd ac yn y blaen. Sylwer nad yw'r Anonymeiddiwr eto'n addas ar gyfer dogfennau sensitif sy'n cynnwys data gwirioneddol bersonol fel cofnodion meddygol ac ati.

Ceir dau Anonymeiddiwr yn y pecyn hwn:

1. Anonymeiddiwr Data Cyfochrog
1. Anonymeiddiwr Data Cymraeg

## Anonymeiddiwr Data Cyfochrog

Defnyddir tri dull i anonymeiddio gan yr Anonymeiddiwr Data Cyfochrog:

1. Defnyddir technegau Adnabod Endidau Enwol (NER) i adnabod yr endidau sydd wedi’u henwi yn y data (e.e. "John Davies") a’u cyfnewid am label yr endid (e.e. "PERSON"). Canlyniad hynny yw newid:

> "John Davies agreed with the decision.       Cytunodd John Davies â’r penderfyniad."

i

> PERSON agreed with the decision.       Cytunodd PERSON â’r penderfyniad."

Y labeli endidau a ddefnyddir ar hyn o bryd yw: PERSON, GPE, LOC a DATE.

2. Defnyddir tagiwr rhannau ymadrodd Cymraeg i adnabod unrhyw enwau priod a fethwyd gan y cam blaenorol. Mae'r dull hwn yn cuddio'r enw priod gan roi XPROPNX yn ei le, ond nid yw'n dethol label endid priodol ar ei gyfer.

3. Yn olaf, gwaredir unrhyw segment sy'n parhau i fod yn broblemus.

Golyga’r trydydd dull hwn o waredu segmentau fod maint y data allbwn yn a gynhyrchir gan yr Anonymeiddiwr yn llai o ran maint na’r data gwreiddiol. Mae’r union wahaniaeth maint rhwng y data mewnbwn a’r data allbwn yn amrywio yn ôl cynnwys y data, ond gyda’n ffeil prawf o 719,997 segment sensitif, cafwyd allbwn o 291,130 segment, sy’n cynrychioli 40% o’r data gwreiddiol. Mae anonymeiddio yn gyfaddawd rhwng goranonymeiddio ar un llaw a pheidio ag anonymeiddio endidau a ddylid fod wedi cael eu hanonymeiddio ar y llaw arall. Gobeithiwn fod ein gosodiadau gweddol geidwadol ni yn galluogi rhannu a defnyddio llawer o ddata na fyddai wedi bod modd ei ddosbarthu fel arall.

Dyma enghraifft o segmentau cyfochrog sydd wedi cael eu hanonymeiddio gan yr Anonymeiddiwr:

PERSON believes it may be more common than the literature indicates  
*Mae PERSON yn credu y gall fod yn fwy cyffredin na mae'r llenyddiaeth yn ei awgrymu.*

Who does it affect?  
*Ar bwy mae'n effeithio?*

This virus causes fever, swollen spleen, sore throat, and inflamed lymph nodes.  
*Mae'r firws hwn yn achosi twymyn, dueg chwyddedig, dolur gwddf, a nodau lymff llidus.*

The signal receptors can be affected by things like intoxication with hallucinogens, migraine headaches, and tumors in the brain, headaches, and PERSON viral infection (glandular fever).  
*Gall pethau fel meddwdod gyda rhithbeiriau, cur pen meigryn a thiwmorau yn yr ymennydd, cur pen, a haint firaol PERSON (twymyn y chwarennau) effeithio ar y  derbynyddion signalau.*

Other receivables - taxation recoverable  
*Symiau derbyniadwy eraill - treth adferadwy*

ORG and PERSON  
*ORG a PERSON*

Have you experienced something similar?  
*A ydych wedi profi rhywbeth tebyg?*

Lets experiment!  
*Dewch i ni arbrofi!*

Want to feel and out of body experience?  
*Ydych eisiau teimlo sut beth yw profiad tu allan i'r corff?*  

I’m going to give you several demonstrations, then in groups, I would like you to try them out for yourselves!  
*Rwy'n mynd i arddangos nifer o bethau i chi, yna mewn grwpiau, hoffwn i chi roi cynnig arnynt eich hunain!*

PERSON a British psychiatrist first published the name in DATE  
*PERSON, seiciatrydd Prydeinig, a gyhoeddodd yr enw am y tro cyntaf ym DATE.*

## Anonymeiddiwr Data Cymraeg
Ar hyn o bryd mae'r Anonymeiddiwr Data Cymraeg yn gweithredu ar sail tagiau rhannau ymadrodd yn unig tra'n bod ni'n paratoi gwell cydran Adnabod Endidau ar gyfer y Gymraeg. Defnyddir y tagiwr rhannau ymadrodd Cymraeg i adnabod unrhyw enwau priod a'u cuddio drwy roi XPROPNX yn eu lle. Ni ddetholir label endid priodol ar eu cyfer ar hyn o bryd.

Dyma enghraifft o destun a anonymeiddiwyd gan yr Anonymeiddiwr Data Cymraeg:

Nofel ar gyfer plant a'r arddegau gan XPROPNX XPROPNX XPROPNX yw O Na!
Roedd o’n unig felly mi ddoth o nôl ata i.
Mae e’n giciwr da iawn.
A fydd hi'n gallu dod o hyd iddo?
Drama ysgafn gan XPROPNX XPROPNX yw XPROPNX o XPROPNX.
Gwaeddodd XPROPNX yn druenus, a chiliodd tuag ataf fi.
Pecyn o ddeg llyfr Cyfres XPROPNX am Byth!
dywedwch chi pryd fyddwch chi'n barod
poenodd
Fi’n canu fe nawr pob tro fi'n dreifio lawr i weld XPROPNX.
Rwan, cymer dy gyllell a rhwyma hi wrth flaen yr ede.
Mae copi o'r hunangofiant wedi ei gadw fel llawysgrif yn Llyfrgell Prifysgol XPROPNX.

Ceir ffeil enghreifftiol o allbwn anonymeiddio ein Corpws CC0 yn `anonymized_cc0_cy_conc_covost.txt` . 

## Rhybudd
Nid yw’r Anonymeiddiwr hwn yn addas ar gyfer data personol sensitif. Ni fwriadwyd yr Anonymeiddiwr hwn ar gyfer ei ddefnyddio gyda dogfennau sy’n cynnwys data sensitif personol a phreifat megis cofnodion iechyd unigolion. Fe’i bwriadwyd yn bennaf fel haen ychwanegol o ddiogelwch i alluogi cyrff cyhoeddus i fod yn fwy hyderus i rannu cynnwys dogfennau cyffredinol sydd o natur ansensitif, ond sydd efallai yn cynnwys enwau aelodau o staff ac ati y byddai’n well peidio eu rhannu. **Y ffordd orau o sicrhau na chaiff cynnwys dogfennau sensitif eu rhannu yw i adnabod a nodi sensitifrwydd dogfennau cyn eu cyfieithu ac i beidio a chynnwys unrhyw ddogfennau sensitif o fewn cof cyfieithu cyffredinol. Nid yw’r Anonymeiddiwr yn disodli’r angen am bolisi diogeledd data cadarn.**

## Cyfarwyddiadau Gosod a Defnyddio'r Anonymeiddiwr
Mae’r Anonymeiddiwr Beta yn raglen Python sydd angen Python 3.8 neu'n ddiweddarach i redeg. Mae'n rhaid rhedeg yr Anonymeiddiwr ar y llinell orchymyn. Rhaid i chi hefyd fod wedi gosod pecyn llyfrgell spaCy o flaen llaw (gweler https://spacy.io/usage), ac argymhellwn lwytho’r model mawr (en_web_core_lg) i lawr er mwyn pweru’r Adnabod Endidau. Ar gyfer galluogi'r ochr Gymraeg, rhaid gosod y ffeil `cy` sy'n gynwysiedig o fewn ffolder `lang` eich gosodiad chi o spaCy. Mae'r tagio rhannau ymadrodd Cymraeg yn defnyddio'r model Cymraeg sy'n gynwysiedig gyda'r pecyn hwn. 

### Anonymeiddiwr Data Cyfochrog
Mae’r anonymeiddiwr hwn yn disgwyl ffeil `.csv` fel ffeil fewnbwn, gyda’r testun Saesneg wedi ei labeli fel y golofn ‘source’ a’r testun Cymraeg fel y golofn ‘target’, a chyda thab yn eu gwahanu.

I’w defnyddio, ewch i leoliad y ffeil a theipio:

`anonymize_ency.py input_file.csv  output_file.csv`

gan ddefnyddio enw eich ffeil yn hytrach nag `input_file.csv`, a’r enw y dymunwch ei roi ar y ffeil allbwn yn lle `output_file.csv`.

### Anonymeiddiwr Data Cymraeg

Mae’r anonymeiddiwr hwn yn disgwyl ffeil testun plaen `.txt` fel ffeil fewnbwn, gydag un frawddeg Gymraeg i bob llinell.

I’w defnyddio, ewch i'r lleoliad lle y gosodwyd y ffeil `anonymize_cy.py` a theipio:

`anonymize_cy.py input_file.txt  output_file.txt`

gan ddefnyddio enw eich ffeil yn hytrach nag `input_file.txt`, a’r enw y dymunwch ei roi ar y ffeil allbwn yn lle `output_file.txt`.

## Datblygiadau sydd i ddod
Fersiwn beta gychwynnol o’r Anonymeiddiwr yw hwn. Gobeithiwn ei ddatblygu ymhellach dros y misoedd nesaf er mwyn codi hyder yr algorithm anonymeiddio fel bod modd anonymeiddio rhagor o endidau segmentau yn hytrach na gwaredu’r segment gyfan. I wneud hynny, byddwn yn gwella’r Adnabod Endidau Saesneg ymhellach trwy ei hyfforddi ar ddata sy’n cynnwys endidau unigryw Cymreig. Bwriadwn hefyd gyhoeddi ffrwyth ein harbrofion gyda chyfnewid enwau endidau (e.e. cyfnewid ‘John Davies’ am enw arall ar hap (e.e ‘Keith Williams’), yn hytrach na’u cyfnewid am labeli endidau fel ‘PERSON’. Y gobaith yw y bydd hyn yn galluogi'r brawddegau a anonymeiddiwyd i fod yn well data hyfforddi ar gyfe modelau iaith yn y dyfodol.



# Beta Anonymizer
The purpose of this anonymizer is to remove personal information from Welsh-language data, and from parallel English-Welsh data such as translation memories. The aim is to facilitate the sharing and distribution of such data for the purpose of training language models (including in particular machine translation models) by assuaging fears about sharing general data which may include person names, place names etc. Note that this Anonymizer is not suitable for use on sensitive documents which include truly personal data such as medical records and so on.

There are two anonymizer in this collection:

1. Parallel Data Anonymizer
1. Welsh-Language Data Anonymizer

## Parallel Data Anonymizer

Three different methods are used by the Parallel Data Anonymizer:

1. Named Entity Recognition (NER) is used to identify entities occuring in the data (e.g. "John Davies") which can then be substituted by their entity type (e.g. "PERSON"). This results in changing:

> "John Davies agreed with the decision.       Cytunodd John Davies â’r penderfyniad."

to

> PERSON agreed with the decision.       Cytunodd PERSON â’r penderfyniad."

Currently, the following entities are used: PERSON, GPE, LOC a DATE.

2. Additionally, a Welsh-language part of speech tagger is used to identify any proper nouns that may have benn missed by the previous step. These are replaced by the text 'XPROPNX', but no entity type is assigned.

3. Lastly, any remaining problematic segments are simply discarded.

Golyga’r trydydd dull hwn o waredu segmentau fod maint y data allbwn yn a gynhyrchir gan yr Anonymeiddiwr yn llai o ran maint na’r data gwreiddiol. Mae’r union wahaniaeth maint rhwng y data mewnbwn a’r data allbwn yn amrywio yn ôl cynnwys y data, ond gyda’n ffeil prawf o 719,997 segment sensitif, cafwyd allbwn o 291,130 segment, sy’n cynrychioli 40% o’r data gwreiddiol. Mae anonymeiddio yn gyfaddawd rhwng goranonymeiddio ar un llaw a pheidio ag anonymeiddio endidau a ddylid fod wedi cael eu hanonymeiddio ar y llaw arall. Gobeithiwn fod ein gosodiadau gweddol geidwadol ni yn galluogi rhannu a defnyddio llawer o ddata na fyddai wedi bod modd ei ddosbarthu fel arall.

Dyma enghraifft o segmentau cyfochrog sydd wedi cael eu hanonymeiddio gan yr Anonymeiddiwr:

PERSON believes it may be more common than the literature indicates  
*Mae PERSON yn credu y gall fod yn fwy cyffredin na mae'r llenyddiaeth yn ei awgrymu.*

Who does it affect?  
*Ar bwy mae'n effeithio?*

This virus causes fever, swollen spleen, sore throat, and inflamed lymph nodes.  
*Mae'r firws hwn yn achosi twymyn, dueg chwyddedig, dolur gwddf, a nodau lymff llidus.*

The signal receptors can be affected by things like intoxication with hallucinogens, migraine headaches, and tumors in the brain, headaches, and PERSON viral infection (glandular fever).  
*Gall pethau fel meddwdod gyda rhithbeiriau, cur pen meigryn a thiwmorau yn yr ymennydd, cur pen, a haint firaol PERSON (twymyn y chwarennau) effeithio ar y  derbynyddion signalau.*

Other receivables - taxation recoverable  
*Symiau derbyniadwy eraill - treth adferadwy*

ORG and PERSON  
*ORG a PERSON*

Have you experienced something similar?  
*A ydych wedi profi rhywbeth tebyg?*

Lets experiment!  
*Dewch i ni arbrofi!*

Want to feel and out of body experience?  
*Ydych eisiau teimlo sut beth yw profiad tu allan i'r corff?*  

I’m going to give you several demonstrations, then in groups, I would like you to try them out for yourselves!  
*Rwy'n mynd i arddangos nifer o bethau i chi, yna mewn grwpiau, hoffwn i chi roi cynnig arnynt eich hunain!*

PERSON a British psychiatrist first published the name in DATE  
*PERSON, seiciatrydd Prydeinig, a gyhoeddodd yr enw am y tro cyntaf ym DATE.*

## Anonymeiddiwr Data Cymraeg
Ar hyn o bryd mae'r Anonymeiddiwr Data Cymraeg yn gweithredu ar sail tagiau rhannau ymadrodd yn unig tra'n bod ni'n paratoi gwell cydran Adnabod Endidau ar gyfer y Gymraeg. Defnyddir y tagiwr rhannau ymadrodd Cymraeg i adnabod unrhyw enwau priod a'u cuddio drwy roi XPROPNX yn eu lle. Ni ddetholir label endid priodol ar eu cyfer ar hyn o bryd.

Dyma enghraifft o destun a anonymeiddiwyd gan yr Anonymeiddiwr Data Cymraeg:

Nofel ar gyfer plant a'r arddegau gan XPROPNX XPROPNX XPROPNX yw O Na!
Roedd o’n unig felly mi ddoth o nôl ata i.
Mae e’n giciwr da iawn.
A fydd hi'n gallu dod o hyd iddo?
Drama ysgafn gan XPROPNX XPROPNX yw XPROPNX o XPROPNX.
Gwaeddodd XPROPNX yn druenus, a chiliodd tuag ataf fi.
Pecyn o ddeg llyfr Cyfres XPROPNX am Byth!
dywedwch chi pryd fyddwch chi'n barod
poenodd
Fi’n canu fe nawr pob tro fi'n dreifio lawr i weld XPROPNX.
Rwan, cymer dy gyllell a rhwyma hi wrth flaen yr ede.
Mae copi o'r hunangofiant wedi ei gadw fel llawysgrif yn Llyfrgell Prifysgol XPROPNX.

Ceir ffeil enghreifftiol o allbwn anonymeiddio ein Corpws CC0 yn `anonymized_cc0_cy_conc_covost.txt` . 

## Rhybudd
Nid yw’r Anonymeiddiwr hwn yn addas ar gyfer data personol sensitif. Ni fwriadwyd yr Anonymeiddiwr hwn ar gyfer ei ddefnyddio gyda dogfennau sy’n cynnwys data sensitif personol a phreifat megis cofnodion iechyd unigolion. Fe’i bwriadwyd yn bennaf fel haen ychwanegol o ddiogelwch i alluogi cyrff cyhoeddus i fod yn fwy hyderus i rannu cynnwys dogfennau cyffredinol sydd o natur ansensitif, ond sydd efallai yn cynnwys enwau aelodau o staff ac ati y byddai’n well peidio eu rhannu. **Y ffordd orau o sicrhau na chaiff cynnwys dogfennau sensitif eu rhannu yw i adnabod a nodi sensitifrwydd dogfennau cyn eu cyfieithu ac i beidio a chynnwys unrhyw ddogfennau sensitif o fewn cof cyfieithu cyffredinol. Nid yw’r Anonymeiddiwr yn disodli’r angen am bolisi diogeledd data cadarn.**

## Cyfarwyddiadau Gosod a Defnyddio'r Anonymeiddiwr
Mae’r Anonymeiddiwr Beta yn raglen Python sydd angen Python 3.8 neu'n ddiweddarach i redeg. Mae'n rhaid rhedeg yr Anonymeiddiwr ar y llinell orchymyn. Rhaid i chi hefyd fod wedi gosod pecyn llyfrgell spaCy o flaen llaw (gweler https://spacy.io/usage), ac argymhellwn lwytho’r model mawr (en_web_core_lg) i lawr er mwyn pweru’r Adnabod Endidau. Ar gyfer galluogi'r ochr Gymraeg, rhaid gosod y ffeil `cy` sy'n gynwysiedig o fewn ffolder `lang` eich gosodiad chi o spaCy. Mae'r tagio rhannau ymadrodd Cymraeg yn defnyddio'r model sy'n gynwysiedig gyda'r pecyn hwn. 

### Anonymeiddiwr Data Cyfochrog
Mae’r anonymeiddiwr hwn yn disgwyl ffeil `.csv` fel ffeil fewnbwn, gyda’r testun Saesneg wedi ei labeli fel y golofn ‘source’ a’r testun Cymraeg fel y golofn ‘target’, a chyda thab yn eu gwahanu.

I’w defnyddio, ewch i leoliad y ffeil a theipio:

`anonymize_ency.py input_file.csv  output_file.csv`

gan ddefnyddio enw eich ffeil yn hytrach nag `input_file.csv`, a’r enw y dymunwch ei roi ar y ffeil allbwn yn lle `output_file.csv`.

### Anonymeiddiwr Data Cymraeg

Mae’r anonymeiddiwr hwn yn disgwyl ffeil testun plaen `.txt` fel ffeil fewnbwn, gydag un frawddeg Gymraeg i bob llinell.

I’w defnyddio, ewch i'r lleoliad lle y gosodwyd y ffeil `anonymize_cy.py` a theipio:

`anonymize_cy.py input_file.txt  output_file.txt`

gan ddefnyddio enw eich ffeil yn hytrach nag `input_file.txt`, a’r enw y dymunwch ei roi ar y ffeil allbwn yn lle `output_file.txt`.

## Datblygiadau sydd i ddod
Fersiwn beta gychwynnol o’r Anonymeiddiwr yw hwn. Gobeithiwn ei ddatblygu ymhellach dros y misoedd nesaf er mwyn codi hyder yr algorithm anonymeiddio fel bod modd anonymeiddio rhagor o endidau segmentau yn hytrach na gwaredu’r segment gyfan. I wneud hynny, byddwn yn gwella’r Adnabod Endidau Saesneg ymhellach trwy ei hyfforddi ar ddata sy’n cynnwys endidau unigryw Cymreig. Bwriadwn hefyd gyhoeddi ffrwyth ein harbrofion gyda chyfnewid enwau endidau (e.e. cyfnewid ‘John Davies’ am enw arall ar hap (e.e ‘Keith Williams’), yn hytrach na’u cyfnewid am labeli endidau fel ‘PERSON’. Y gobaith yw y bydd hyn yn galluogi'r brawddegau a anonymeiddiwyd i fod yn well data hyfforddi ar gyfe modelau iaith yn y dyfodol.

