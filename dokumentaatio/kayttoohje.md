# Käyttöohje
## Viimesin release
Ohjelman viimeisin [release](https://github.com/vaisajuh/ot-harjoitustyo/releases/tag/loppupalatus) on saatavilla valitsemalla _assets_-osion alta _source_-code.

## Konfigurointi
Talletukseen käytettävää tietokantatiedoston nimeä voi muuttaa, ja se sijaitsee käynnistyskamistossa .env-tiedossa. Tiedosto luodaan automaattisest kansion src 
sisällä sijaitsevaan kansioon data. Tässä kansiossa sijaitsee myös tietokantaan lisättävien tietokantojen nimet CSV-tiedostossa, mutta tämän tiedoston nimeä ei voi
vapaasti muokata, ilman sovelluslogiikan uudelleen muotoilua.

## Ohjelman käynnistäminen
Ohjelman tarvitsemat riippuvuudet käynnistetään komennolla:
<pre>poetry install</pre>
Ohjelma käynnistyy komennolla:
<pre>poetry run invoke start</pre>

## Kirjautuminen
Sovellus käynnistyy seuraavanlaiseen näkymään: <br>
![login](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login.png) <br>
Käyttäjä syöttää kenttiin käyttäjänimen ja salasanan kirjautuakseen sisään. Jos salasana on väärä, niin tästä tulee ilmoitus

## Käyttäjän lisääminen
Uusi käyttäjä lisätään seuravaanlaisessa näkymässä <br>
![add_user](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/add_user.png)<br>
- Käyttäjä valitsee haluamansa tunnuksen ja salasanan syöttämällä ne kenttiin.
  - Tunnuksen tulee olla kolmen ja kahdenkymmenen merkin väliltä
  - Salasanan tulee olla viiden ja kahdenkymmen merkin väliltä
 
Kun tiedot on lisätty kenttiin, niin tiedot saa lisätty tietokantaan painamalla nappia <strong>lisää käyttäjä</strong>. Jos syötteet ovat
oikean pituisia, niin onnistuneesta lisäyksestä tulee ilmoitus ja kentät tyhjenevät. Vääristä syötteistä tulee myös ilmoitus, ja näitä syötteitä
on mahdollista vielä muokata. Takaisin kirjautumisikkunaan pääsee painamalla nappia <strong> palaa edelliseen näkymään</strong>

## Toiminnallisuus
Sisäänkirjautumisen jälkeen aukeaa seuraavanlainen näkymä:<br>
![functionality](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/functionality.png)<br>
Ikkunan toiminallisuus:
- Hae yhteystiedot
  - Kun käyttäjä lisää yhteystiedon tietokantaan, niin tästä aukeaa näkymä yhteystietojen näyttämiseen
- Lisää yhteystieto
  - Mahdollistaa yhteystiedon lisäämiseen tietokantaan
- Kirjaudu ulos
  - Kirjaa käyttäjän ulos sovelluksesta ja vie takaisin kirjautumisikkunaan
 
 ## Yhteystiedon lisääminen
 Seuraavassa näkymä yhteystiedon lisäämiseen:<br>
 ![add_contact](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/add_contact.png)<br>
 Ikkunan toiminallisuus:
 - Nimi
   - Nimen tulee olla vähintään kolme ja enintään kaksikymmentä merkkiä pitkä
 - Osoite
   - Osoitteen tulee olla vähintään kymmenen ja enintään neljäkymmentä merkkiä pitkä
 - Sähköposti
   - Tulee olla vähintää kymmenen ja enintään neljäkymmentä merkkiä pitkä ja tulee olla muodossa x@x.com
 - Puhelinnumero
   - Tulee olla kymmenen ja neljänkymmenen merkin välillä ja tulee sisältää vain numeroita

Kun tiedot on lisätty kenttiin, niin tiedot saa lisättyä tietokantaan painamalla nappia <strong>lisää</strong>. Jos lisäys on onnistunut, niin kentät
tyhjenevät ja onnistuneesta lisäyksestä tulee ilmoitus. Virheellisistä syötteistä tulee ilmoitus ja tiedot jäävät tämän jälkeen muokattavaksi.
Nappi <strong>palaa edelliseen näkymään</strong> vie nimensä mukaisesti takaisin ikkunaan, jossa näkyy ohjelman toiminallisuus.
 
 ## Yhteystietojen näyttäminen
 Seuraavassa näkymä yhteystietojen näyttämiseen: <br>
 ![show](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/show_contacts.png)<br>
 Ikkunan toiminallisuus
 - Poista
   - Käyttäjä valitsee poistettavan yhteystiedon listasta ja poistaa sen nappia painamalla
 - Muokkaa
   - Käyttäjä valitsee muokattavan yhteystiedon listasta ja nappia painamalla avautuu uusi ikkuna muokkausta varten
   - Muokkausta koskee samat säännöt kuin yhteystietoja lisätessä
   - Muokkauksen ollessa valmis painetaan nappia muokkaa
     - Jos muokkaus on onnistunut, niin ikkuna sulkeutuu ja yhtestieto päivittyy
     - Virheellisistä syötteistä tulee ilmoitus ja käyttäjällä on mahdollisuus korjata syötteet
 - Hae
   - Käyttäjä voi hakea yhteystietoja listasta samoilla arvoilla kuin yhtestietoja lisätessä
     - Haku on säädetty hakemaan kaikki yhtestiedot, jossa on samankaltaisia sanoja
       - Tämä tarkoittaa, että jos yksikin kenttä täsmää haettavaan sanaa, niin haetaan samankaltaiset sanat. Tyhjät hakusanat täsmäävät kaikkien yhteystietojen kanssa
 - Palaa edelliseen näkymään
   - Vie käyttäjän takaisin näkymään, jossa ilmenee ohjelman toiminnallisuus
 




