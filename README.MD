# Taistelurobotin ohjelma

## Yleisrakenne

Yleinen kansiosta löytyy ohjelma jonka saa helposti toimimaan myös muiden roboteilla. Päivittäessä teen sinne aina uuden kansion (esim. yleinen2), joten vanha ohjelma säilyy myös päivittäessä.

Vanha kansiosta löytyy alkuperäinen koodi, jota voi käyttää jos muokattu ei lähde toimimaan. Joukkuekohtaiset jutut, esimerkiksi kuvat poistin koodista, muuten samanlainen.

Laitan keskeneräisen koodin, jota testaan koodikarhut kansioon. Se voi olla hankalampi käyttää muille, sillä siellä on meidän robotin pohjalta tehtyjä ominaisuuksia. Pistän kuitenkin tänne, saa hyödyntää ja käyttää. Päivitän sitä mukaa yleiseen ja dokumentoin kun otamme itse koodin käytöön.

Käynnistettävät ohjelmat ovat alaosa.py ja ylaosa.py

Jos Bluetooth ei toimi käynnistyksen jälkeen ("Not Available"), uudelleenkäynnistys auttaa.

## Moottorien portit

Kaikkien moottorien pitää olla kytkettyinä, muuten ohjelma ei käynnisty. Alaosaa ohjataan kuten alkuperäisessäkin koodissa, vain portit ovat vaihtuneet. Yläosan moottorien ohjaukset lukee alempana, ne ovat muuttuneet. Ohjausta on moottorien jännitteiden kirjoituksen osalta optimoitu, joka parantaa viivettä.

Alaosan moottorien portit:  
A: etuvasen  
B: etuoikea  
C: takavasen  
D: takeoikea  

Yläosan moottorien portit:  
A: Vasen tikku vasemmalle/oikealle  
B: L1 ja R1 napit, ohjaimen takana ylhäällä  
C: Oikea tikku ylös/alas  
D: Ei ohjausta, ei tarvitse kytkeä  

Muut napit:  
Share: yhteyden testaus, piippaus  
Options: Ohjelman pysäyttäminen oikein  

## Koodin rakenne tarkemmin

Olen kommentoinnut koodin suhteellisen hyvin englanniksi, joten muokkaaminen on melko helppoa jos osaa.

Gamepad.py:  
-Täällä on määritelty ohjaimen eventtien tyypit, koodit sekä arvot  
-Lisäksi on eventtejen lukemiseen liittyvät määritykset  
-GamepadEvent luokassa on koko tapahtuma joka tulee ohjaimelta  
-Gamepad luokassa on tapahtumien vastaanottamiseen liittyvää koodia  

Common.py:  
-Täällä on koodia, jota käytetään sekä ala- että yläosassa  
-Scale funktio muuttaa ohjaimen arvon moottorin tehoksi  
-Funktio piippausäänelle  
-Main loop, joka ottaa sisään ohjelmakohtaiset funktiot sekä kutsuu niitä tarvittaessa  
-Loopissa on lisäksi yhteyden testauksen ja ohjelman pysäytyksen koodit  

Alaosa.py:  
-Alaosan moottorien alustus  
-Funktio moottorien pysäyttämiseen  
-Moottorien ohjaus  
-Kutsutaan common.py:n koodia  

Ylaosa.py:  
-Yläosan moottorien alustus  
-Moottorien ohjaus  
-Kutsutaan common.py:n koodia  

## Yhteystiedot
Jos tulee ongelmia tai kysyttävää ohjelmasta voitte laittaa sähköpostia osoitteeseen teemu.koukkari@gmail.com
