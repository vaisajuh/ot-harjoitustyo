# Käyttöohje

## Konfigurointi
Talletukseen käytettävää tietokantatiedoston nimeä voi muuttaa, ja se sijaitsee käynnistyskamistossa .env-tiedossa. Tiedosto luodaan automaattisest kansion src 
sisällä sijaitsevaan kansioon data. Tässä kansiossa sijaitsee myös tietokantaan lisättävien tietokantojen nimet CSV-tiedostossa, mutta tämän tiedoston nimeä ei voi
vapaasti muokata, ilman sovelluslogiikan uudelleen muotoilua.

## Ohjelman käynnistäminen
Ohjelman tarvitsemat riippvuudet käynnistetään komennolla:
<pre>poetry install</pre>
Ohjelma käynnistyy komennolla:
<pre>poetry run invoke start</pre>

## Kirjautuminen
Sovellus käynnistyy seuraavanlaiseen näkymään: <br>
![logio](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login.png) <br>
Jos käyttäjällä ei ole ennestään käyttäjänimeä ja salasanaa, niin se luodaan ensimmäisen kirjautumisen yhteydessä. Käyttäjänimen ja salasanen tulee olla kolmen ja
kahdenkymmenen merkin väliltä tai siitä tulee ilmoitus. Kun käyttäjäprofiili luodaan, niin samalla nimellä ei ole mahdollista enää luoda toista käytäjäprofiilia
ja väärästä salasanasta tulee ilmoitus.

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
   - Osoitteen tulee olla vähintään viisi ja enintään kaksikymmentä merkkiä pitkä
 - Sähköposti
   - Tulee olla vähintää viisi ja enintään kaksikymmentä merkkiä pitkä ja tulee olla muodossa x@x.com tai tulee ilmoitus
 - Puhelinnumero
   - Tulee olla viiden ja kahdenkymmenen välillä ja tulee sisältää vain numeroita

Kun tiedot on lisätty kenttiin, niin tiedot saa lisättyä tietokantaan painamalla nappia <strong>lisää</strong> <br>
Nappi <strong>palaa edelliseen näkymään</strong> vie nimensä mukaisesti takaisin ikkunaan, jossa näkyy ohjelman toiminallisuus.
 
 ## Yhteystietojen näyttäminen
 Seuraavassa näkymä yhtestietojen näyttämiseen:
 Ikkunassa oikealla hakutoiminto, jolla voi hakea sisäänkirjatuneen käyttäjän henkilökohtaisesta lista yhteystietoja. Syötteiden pituutta ei ole rajoitettu.
 Jos käyttäjä haluaa poistaa yhteystiedon, niin se tapahtuu maalaamalla listasta kyseisen tiedon ja painamalla nappia <strong>poista</strong>. Edelliseen näkymään
 pääsee paimalla nappia <strong>palaa edelliseen näkymään</strong><br>
 ![show](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/show_contacts.png)<br>
 




