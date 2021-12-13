# Arkkitehtuurikuvaus
## Käyttöliittymä
Käyttöliittymällä on neljä näkymää:
- Kirjautuminen
- Ohjelman toiminallisuus
- Yhteystietojen lisääminen
- Yhteystietojen näyttäminen

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

Pakkauksessa database sijaitseva <strong>HandleDatabase</strong>-luokka tarjoaa tallennuslogiikasta vastaaville luokille tietokantayhteyden SQLite-tietokantaan. Pakettissa reader sijaitseva moduulissa luetaan CSV-tiedostosta tarvittavat tietokantataulut, ja luokka <strong>HandleDabase</strong> huolehtii taulujen lisäämisestä tietokantaan.

## Päätoiminallisuudet
Tässsä osiossa selitettynä ja sekvenssikaavioina kuvattuna ohjelman päätoiminnallisuudet.

### Kirjautuminen
Ohjelman käynnistyessä käyttäjä kohtaa ensiksi kirjautumisikkunan. Tässä ikkunassa sijaitseviin kenttiin käyttäjä syöttää käyttäjätunnuksen ja salasanan. Nämä tiedot menevät eteenpäin luokan HandeluUser tarkastettavaksi, ja jos nämä tiedot ovat validit, niin kyseisen käyttäjän id-numero haetaan tietokannasta ja asetetaan HandleSession-luokan metodin add_session avulla istunnon arvoksi. Kun salasana on validoitu, niin käyttäjälle aukeaa ikkuna, jossa ilmenee ohjelman toiminallisuus.
![kirjautuminen](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kirjautuminen.png)

### Uusi käyttäjä
Jos käyttäjällä ei ole ennestään käyttäjätunnusta ja salasanaa, niin se luodaan syöttämällä haluttu käyttäjätunnus ja salasana kirjautumisikkunassa sijaitseviin kenttiin. Tämä prosessi menee saman tarkastuksen läpi kuin olemassaolevan käyttäjän tapauksessa, mutta koska käyttäjää ei löydy tietokannasta, niin se luodaan ja loppu etenee saman kaavan mukaan.
![uusi](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/uusi_kayttaja.png)

### Lisää kontakti
Käyttäjän lisätessä kontakteja haetaan ensiksi luokan HandleSession metodin avulla get_session kirjautuneena olevan käyttäjän id-numero. Kun käyttäjä syöttää luokan HandleContacts metodin insert_contact avulla tietoja tietokantaan, niin tämä tämä id-numero annetaan syötteen mukana, jotta kontakti voidaan yksilöidä kirjautuneeseen käyttäjään. 
![lisaa](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/lisaa_yhteystieto.png)

### Kontaktit
Tässä sekvenssikaaviossa on kaksi toimintoa: kirjautuneena olevan käyttäjän kontaktien hakeminen ja niiden poistaminen. Käyttäjälle haetaan luokan HandleSession metodin get_session avulla id-numero, ja tämä id-numero syötetään luokan HandleContact metodille get_contacts, joka palauttaa yhteystiedot näytettäväksi käyttäjälle. Metodi get_contacts palauttaa myös piilotetuna yhteystiedon id-numeron, joka avulla voidaan luokan HandeContacts metodia käyttämällä poistaa kyseinen yhteystieto tietokannasta nappia painamalla. 
![kontaktit](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kontaktit.png)
