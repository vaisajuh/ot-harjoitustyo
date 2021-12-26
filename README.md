# ContactsApp
Tämän sovelluksen tarkoituksena on tarjota mahdollisuus tallentaa yhteystietoja tietokantaan. Jokaisella kirjautuneella käyttäjällä on oma henkilökohtainen lista yhteystiedoista.

## Huomio python-versiosta
Sovellus on testattu python-versiolla <code>3.8</code> ja sovelluksen toimintaa vanhemmilla versioilla ei voida taata. 

## Dokumentaatio
- [Käyttöohje](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)<br>
- [Vaatimusmäärittely](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) <br>
- [Tuntikirjanpito](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md) <br>
- [Arkkitehtuurikuvaus](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Releaset
- [Viikko5](https://github.com/vaisajuh/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko6](https://github.com/vaisajuh/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus](https://github.com/vaisajuh/ot-harjoitustyo/releases/tag/loppupalatus)

## Sovelluksen asennus
- Riippuvuudet asennetaan komennolla: <h3><pre>poetry install</pre></h3>

## Komentorivitoiminnot
- Ohjelma käynnistyy komennolla: <h3><pre>poetry run invoke start</pre></h3>
- Testit voi jaa komennolla: <h3><pre>poetry run invoke test</pre></h3>
- Testikattavuusraportin saa komennolla: <h3><pre>poetry run invoke coverage-report</pre></h3>
- Tiedoston [.pylintrc](https://github.com/vaisajuh/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla: <h3><pre>poetry run invoke lint</pre></h3>
