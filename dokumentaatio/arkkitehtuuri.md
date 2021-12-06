# Arkkitehtuurikuvaus
## Sovelluslogiikka
### Luokkavaavio
![luokat](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokat1.png)
### Luokka- ja pakkauskaaviot
Ensiksi pakkauksen <strong>store</strong> luokat injektoidaan luokkaan <strong>handledatabase,</strong> ja nämä injektoidaan luokkaan <strong>main.</strong> Luokkaan <strong>Main</strong> injektoidaan vielä pakkauksen <strong>session</strong> luokka <strong>handle_session,</strong>
 ja lopuksi tämä kokonaisuus siirretään käyttöliittymästä vastaavalle luokalle <strong>ui.</strong> Punainen viiva pakkausten <strong>session</strong>
 ja <strong>store</strong> välillä on piirretty kuvaamaan niiden sisältämien luokkien välistä epäsuoraa yhteyttä.<br>
![pakkaus](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkaus.png)
## Päätoiminallisuudet
Tässsä osiossa selitettynä ja sekvenssikaavioina kuvattuna ohjelman päätoinallisuudet.
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
