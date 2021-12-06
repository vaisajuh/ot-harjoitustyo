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
### Kirjautuminen
![kirjautuminen](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kirjautuminen.png)
### Uusi käyttäjä
![uusi](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/uusi_kayttaja.png)
### Lisää kontakti
![lisaa](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/lisaa_yhteystieto.png)
### Kontaktit
![kontaktit](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kontaktit.png)
