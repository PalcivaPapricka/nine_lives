# **Game Design Document - Nine Lives**

Repozitár obsahuje prototyp hry Nine-lives vytvorenej v Pygame, ktorá bola vytvorená ako záverečný projekt v predmete objektové technológie. 

**Autor**: Viktor Kramár

**Vybraná téma**: Losing to win

---
## **1. Úvod**
Ako tému svojho projektu som si zvolil Losing to win. Hráč ovláda mačku, ktorá sa snaží uloviť v každom leveli myš. Každý level obsahuje rôzne prekážky, skoky a pasce, ktoré musí mačka prekonať. Keď mačka zomrie, na mieste jej smrti zostane hrob, ktorý slúži ako nová platforma ktorú môže hráč využiť. Každá smrť mení úroveň, čím umožňuje vytvoriť nové cesty na prekonanie prekážok. Hráč musí strategicky využívať smrť mačky, aby sa dostal ďalej v hre. 

### **1.1 Inšpirácia**
<ins>**Life Goes On: Done to Death**</ins>

Life Goes On: Done to Death je komicky morbídna plošinovka, v ktorej vediete hrdinských rytierov k ich zániku a používate mŕtve telá na riešenie hádaniek. Mocný kráľ, ktorý chce žiť večne, posiela svoju armádu rytierov, aby našla Pohár života. Na tejto výprave budete vyvolávať rytiera za rytierom, aby vás brutálne obetovali. Napichnite rytierov na hroty, aby ste vytvorili bezpečnú cestu. Chyťte rytiera na pílovom kotúči, aby ste pristáli telom na gombíku. Zmrazte rytierov do blokov ľadu, aby ste sa dostali do vyšších miest.

### **1.2 Herný zážitok**
Cieľom hry je, aby hráč v každom leveli ulovil myš pričom si pomocou vlastnej smrti vytvára nové plošiny podla vlastnej potreby. 

### **1.3 Vývojový softvér**
- **Pygame-CE**: zvolený programovací jazyk.
- **INteliJ IDEA**: vybrané IDE.
- **Pixabay, Freesound**: zdroje royalty-free zvukových efektov.
- **Aseprite**: pixel-art program na tvorbu herných assetov.
---
## **2. Koncept**

### **2.1 Prehľad hry**
Cieľom hry je, aby hráč dostal do ciela (ulovil myš). Každá smrť mačky mení prostredie tým, že na mieste úmrtia zanechá hrob, ktorý slúži ako nová platforma. Hráč môže túto mechaniku využiť na vytvorenie ciest, ktoré mu umožnia dosiahnuť predtým nedostupné miesta a efektívnejšie chytať myši. Úspešné prežitie a strategické využitie vlastných úmrtí sú kľúčom k postupu hrou.

### **2.2 Interpretácia témy (Smrť ako súčasť hry)**
V hre je smrť neoddeliteľnou súčasťou postupu. Každý hrob, ktorý zostane po mačke, sa stáva trvalou súčasťou úrovne a umožňuje hráčovi lepšie sa pohybovať po mape. Hráč tak musí premýšľať dopredu, kde sa mu oplatí „obetovať sa“, aby si vytvoril cestu k ďalším myšiam alebo bezpečným miestam.

### **2.3 Základné mechaniky**
- **Hroby ako platformy**:  po smrti mačky na mieste zostane hrob, ktorý hráč môže využiť na pohyb a prekonávanie prekážok.
- **Myši ako hlavný cieľ**: hráč musí chytať myši ktoré sa objavujú na konkrétnych miestach.
- **Hráč môže strategicky umierať**: smrť nie je trest, ale nástroj na vytvorenie nových ciest a zlepšenie pozície v úrovni.

### **2.4 Návrh tried**
- **Main**: trieda, v ktorej sa bude nachádza hlavný gameloop.
- **Player**: trieda reprezentujúca hráča, ovládanie hráča, vykreslenie postavy a kolízie.
- **World**: trieda levelu, vykreslenie spritov a layoutu levelu.
---
## **3. Grafika**
Všetky assety použité v hre som vytvoril sám pomocou pixel-art programu Aseprite. Pri tvorbe som sa zameral na jednoduchý, ale výrazný vizuálny štýl, ktorý podporuje atmosféru hry. Každý objekt, animácia a prostredie boli kreslené manuálne.

---
## **4. Zvuk**
Použité zvukové efekty pochádzajú z royalty-free zdrojov, ako je Pixabay, a boli starostlivo vybrané tak, aby ladili s atmosférou hry. Niektoré zvukové efekty boli upravené a doladené pomocou zvukového editora, aby lepšie zapadali do celkového audio dizajnu. 

---
## **5. Herný zážitok**

### **5.1 Používateľské rozhranie**
Užívatelské rozhranie je jednoduché, hlavná obrazovka obsahuje možnosť začat hru a možnosť hru ukončiť. 

### **5.2 Ovládanie**
Hráč ovláda postavu pomocou klávesnice:

<ins>**Klávesnica**</ins>
- **Šípky**: pohyb hráča do strán.
- **Medzerník**: skok.
- **R**: reset aktuálneho levelu.

---
