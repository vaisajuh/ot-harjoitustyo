# Testausdokumentti
Ohjelmaa on testattu sekä automatisoiduin testein unitestillä että manuaalisesti kehittäjän toimesta.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
Sovelluslogiikasta vastaa luokat <code>HandleUsers</code> ja <code>HandleContacts</code>. <code>HandleUser</code>-luokkaa testataan <code>TestHandleUsers</code>
-luokalla. <code>HandleUsers</code>-luokka saa parametrinaan <code>HandleDatabase</code>-luokan, jonka kautta voidaan testata tämän luokan logiikkaa. <code>HandleContacts</code>-luokkaa testataan <code>TestHandleContact</code>-luokalla, ja myös tämä luokka saa paremetrinaan <code>HandleDataba</code>-luokan, jonka kautta voidaan testata kyseisen luokan logiikkaa.

### Tietokantayhteys
<code>HandleDatabase</code>-luokkaa testataan luokan <code>TestHandleUsers</code> avulla.


### Testauskattavauus
![coverage](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage.png)<br>
Moduuleille config.py ja csv_reader.py ei ole tehty omia testejänsä, koska en nähtyt sitä tarpeelliseksi. Congfig.py sisältää tiedon tietokantatiedoston sijainnista sekä polun csv-tiedostoon, joka sisältää tiedon tietokantaan luotavista tauluista.

## Järkestelmätestaus
Sovellusta on testattu manuaalisesti kehittäjän toimesta

### Asennus ja konfigurointi
Sovellus on asennettu ja sitä on testattu [käyttöohjeen](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) kuvaamalla tavalla linux-ympäristössä.

### Toiminallisuudet
