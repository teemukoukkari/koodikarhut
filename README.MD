# Taistelurobotin ohjelma

## Yleisrakenne

Yleinen kansiosta löytyy ohjelma jonka saa helposti toimimaan myös muiden roboteilla. 

Vanha kansiosta löytyy alkuperäinen koodi, jota voi käyttää jos muokattu ei lähde toimimaan. Joukkuekohtaiset jutut, esimerkiksi kuvat poistin koodista, muuten samanlainen.

Pistän koodin, jota käytämme omalla robotilla koodikarhut kansioon. Se voi olla hankalampi käyttää muille, sillä siellä on meidän robotille suunniteltuja ominaisuuksia. Pistän kuitenkin julkiseksi, saa hyödyntää ja käyttää, mutta en dokumentoi tänne. Toistaiseksi siellä ei ole mitään erilaista.

Käynnistettävät ohjelmat ovat alaosa.py ja ylaosa.py

Jos Bluetooth ei toimi käynnistyksen jälkeen ("Not Available"), uudelleenkäynnistys auttaa.

## Moottorien portit

Kaikkien moottorien pitää olla kytkettyinä, muuten ohjelma ei käynnisty. Alaosaa ohjataan kuten alkuperäisessäkin koodissa. Vain portit ovat vaihtuneet. Yläosan moottorien ohjaukset lukee alempana, ne ovat muuttuneet. Ohjausta on moottorien jännitteiden kirjoituksen osalta optimoitu, joka parantaa viivettä.

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

Olen kommentoinnut koodin suhteellisen hyvin englanniksi, joten muokkaaminen on suhteellisen helppoa jos osaa.

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
Jos tulee ongelmia tai kysyttävää ohejelmasta votite laittaa sähköpostia osoitteeseen teemu.koukkari@gmail.com
