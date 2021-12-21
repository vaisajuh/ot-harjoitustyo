# Arkkitehtuurikuvaus
## Käyttöliittymä
Käyttöliittymällä on neljä päänäkymää:
- Kirjautuminen
- Uuden käyttäjän luominen
- Ohjelman toiminallisuus
- Yhteystietojen lisääminen
- Yhteystietojen näyttäminen
  - Yhteystietojen muokkaamiselle avautuu vielä oma ikkunansa

Sovelluksessa on kerralla näkyvillä yksi näkymä, ja näkymien näyttämisestä vastaa Ui-luokka. Toiminnallisuudesta tarkemmin alla.

## Sovelluslogiikka

### Luokkavaavio
Kuva esittää sovelluksen käyttölogiikasta vastaavien luokkien suhdetta. <br>
![luokat](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokat1.png)

### Luokka- ja pakkauskaaviot
Allaoleva kaavio kuvaa pakkausten ja luokkien välistä suhdetta. Pakkauksessa <strong>Storage</strong> ja <strong>Reader</strong> olevat luokat injektoidaan ensiksi paketissa database olevaan luokkaan <strong>HandleDatabase</strong>, ja tämä kokonaisuus injektoidaan luokkaan <strong>Main</strong>. Seuraavaksi <strong>Mainiin</strong> vielä liitetään paketissa Session oleva luokka <strong>HandleSession</strong>, ja tämä luokassa <strong>Main</strong> oleva kokonaisuus annetaan paketissa Ui sijaitsevalle luokalle <strong>Ui</strong>, jossa sijaisee sovelluksen käyttöliittymä.<br>
![pakkaus](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/uusip.png)

## Tietojen pysyväistallennus
Pakkauksen storage luokat <strong>HandleUsers</strong> ja <strong>HandleContacs</strong> vastaavat tietokannan tietojen käsittelystä. <strong>HandelUsers</strong>-luokka tallentaa käyttäjiä tietokantaan ja tarkastaa käyttäjien salasanojen oikeellisuuden. <strong>HandleContacts</strong>-luokan vastuulla on yhteystietojen tallentamineen tietokantaan, niiden poistaminen ja palauttaminen käyttöliittymälle tulostettavaksi.

Pakkauksessa database sijaitseva <strong>HandleDatabase</strong>-luokka tarjoaa tallennuslogiikasta vastaaville luokille tietokantayhteyden SQLite-tietokantaan. Pakettissa reader sijaitseva moduulissa luetaan CSV-tiedostosta tarvittavat tietokantataulut, ja luokka <strong>HandleDabase</strong> huolehtii taulujen lisäämisestä tietokantaan. Tiedosto [.env](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/.env) määrittelee tietokanta- ja csv-tiedostojen nimet. 

## Päätoiminallisuudet
Tässsä osiossa selitettynä ja sekvenssikaavioina kuvattuna ohjelman päätoiminnallisuudet.

### Kirjautuminen
Ohjelman käynnistyessä käyttäjä kohtaa ensiksi kirjautumisikkunan. Tässä ikkunassa sijaitseviin kenttiin käyttäjä syöttää käyttäjätunnuksen ja salasanan. Nämä tiedot menevät eteenpäin luokan <strong>HandleUser</strong> tarkastettavaksi, ja jos nämä tiedot ovat validit, niin kyseisen käyttäjän id-numero haetaan tietokannasta ja asetetaan <strong>HandleSession</strong>-luokan metodin add_session avulla istunnon arvoksi. Kun salasana on validoitu, niin käyttäjälle aukeaa ikkuna, jossa ilmenee ohjelman toiminallisuus.
![kirjautuminen](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kirjautuminen.png)

### Uusi käyttäjä
Jos käyttäjällä ei ole ennestään käyttäjätunnusta ja salasanaa, niin se luodaan erillisessä omassa ikkunassaa syöttämällä haluttu tunnus ja salasana kenttiin. Luokka <strong>HandleUser</strong> asettaa nämä tiedot tietokantaan metodinsa insert_usert avulla, ja palauttaa lopuksi kontrollin käyttöliittymälle.<br>
![uusi](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/uusi_kayttaja.png)

### Lisää kontakti
Ensiksi luokan <strong>HandleSession</strong> metodin avulla get_session haetaan kirjautuneena olevan käyttäjän id-numero. Luokan <strong>HandleContacts</strong> metodin insert_contact avulla syötetään tietoja tietokantaan, ja tämä tämä id-numero annetaan syötteen mukana, jotta kontakti voidaan yksilöidä kirjautuneeseen käyttäjään.
![lisaa](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/lisaa_yhteystieto.png)

### Kontaktit
Tässä sekvenssikaaviossa on kaksi toimintoa: kirjautuneena olevan käyttäjän kontaktien hakeminen ja niiden poistaminen. Käyttäjälle haetaan luokan <strong>HandleSession</strong> metodin get_session avulla id-numero, ja tämä id-numero syötetään luokan <strong>HandleContact</strong> metodille get_contacts, joka palauttaa yhteystiedot näytettäväksi käyttäjälle. Metodi get_contacts palauttaa myös piilotetuna yhteystiedon id-numeron, joka avulla voidaan luokan <strong>HandeContacts<strong> metodia käyttämällä poistaa kyseinen yhteystieto tietokannasta nappia painamalla.
![kontaktit](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kontaktit.png)
