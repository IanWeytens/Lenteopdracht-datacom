# Lenteopdracht-datacom

## 1) Joystick en ADC MCP3008
In jullie kit is er een joystick aanwezig. De joystick is niet meer of minder dan 2 trimmers en 1
drukknop. De 2 signalen van de trimmer VRX en VRY kunnen we aansluiten op de MCP3008. De SW
is de aansluiting van de drukknop, die kan je via een weerstand van 470Ω rechtstreeks verbinden
met de pi. Op het printje mag je op de GND en de +5V pin de spanning van 3V3 aansluiten. Sluit dus
zeker GEEN 5V aan op de joystick module.
Maak gebruik van jullie klasse MCP3008 en lees continue (while True met kleine delay) de waarden
in van de beide kanalen.
Behandel een druk op de joystick als een gewone drukknop. Maak gebruik van een callback
methode. Print telkens de volgende tekst af : “Er is {aantal} keer op de joystick gedrukt!”.

## 2) LCD display
Wat komt er op het LCD display?
Het display zal 3 statussen kennen. Met een druk op de joystick knop zullen we de status van het
display wijzigen. Status 1 => status 2 => status 3 => status 1 => ….
Die status hou je best bij in een globale variabele.
### Status 1
Op status 1 zullen we de Ip adressen van de pi weergeven.
Via de command console kunnen we de Ip-adressen op de volgende manier opvragen : via de
instructie “hostname –all-ip-addresses” kunnen we de ipadressen van de pi bekomen. We krijgen
het wlan0 inet en inet6 adres terug en het eth0.
LENTE VAKANTIE OPDRACHT
NEW MEDIA AND COMMUNICATION TECHNOLOGY
3
In Python kunnen we via de subprocess module connecteren via verschillende in-en output pipes.
https://docs.python.org/3.5/library/subprocess.html?highlight=check_output#subprocess.check_ou
tput
Met de check_output methode kunnen we linux commands uitvoeren en krijgen we de output als
returnwaarde.
In de returnwaarde ips vind je de ip-adressen terug. Haal die eruit en geef ze weer op het scherm.
### Status 2
In de tweede status geven we de VRX waarde van de joystick terug. We krijgen hier een waarde van
0 t.e.m. 1023 terug. Op de eerste lijn geven we dit visueel weer met een aantal blokjes. Een lijn
bestaat uit 16 karakters of 16 blokjes. Verdeel de ingelezen waarde over deze blokjes. Op de
tweede lijn plaats je de tekst. VRX => waarde. Je krijgt dan b.v. het volgende resultaat.
### Status 3
In de derde status geven we de VRYwaarde van de joystick terug. We krijgen hier een waarde van 0
t.e.m. 1023 terug.
LENTE VAKANTIE OPDRACHT
NEW MEDIA AND COMMUNICATION TECHNOLOGY
4

## 3) Arduino en 4*7 segment display
Dit display bestaat uit 4 aparte 7-segment displays, waarvan de anodes voor de segmenten met
elkaar zijn doorverbonden. De kathodes worden per cijfer apart naar buiten gebracht. Door de
combinatie van anode en kathode kunnen we dus nog steeds elk segment apart aansturen. De pins
zijn in dezelfde volgorde genummerd als bij de enkele versie (onder links -> rechts, dan boven rechts
-> links), maar je kan ook je multimeter gebruiken om uit te vlooien welke pin wat is.
Normaal heeft iedereen een display met gemeenschappelijke kathode, namelijk de 3461AS.
Door één van de vier kathodes naar een lang spanningsniveau te trekken bepaal je naar welke digit
je stuurt. We kunnen dus telkens maar naar 1 van de 4 digits aansturen. Vermits de digits geen
geheugen hebben, het zijn ordinaire led, gaan we dus continu onze cijfers één voor één opnieuw
moeten sturen. De digits zullen dus maar ¼ van de tijd oplichten. Als je dit snel genoeg doet is het
voor het menselijk oog niet meer waar te nemen en lijkt het alsof de cijfers gewoon continu
branden. Men noemt dit ook multiplexing. Zo’n multiplexing taak is belastend voor de processor van
de pi, dit is echter een ideale taak om te laten uitvoeren door onze Arduino.
De Arduino heeft 14 digitale pinnen waarvan we er 2 zullen nodig hebben voor de seriële
communicatie tussen de Pi en de Arduino. Voor het 4 maal 7-segment display hebben we 8+4
pinnen nodig. 8 keer de kathode en 4 keer de anode. We hebben dus net voldoende pinnen.
De 8 anodes verbinden we via een weerstand van 1KΩ met de digitale pinnen van de Arduino. De 4
kathodes verbinden we deze keer niet met de massa maar met 4 digitale pinnen op de Arduino.
LENTE VAKANTIE OPDRACHT
NEW MEDIA AND COMMUNICATION TECHNOLOGY
5
Standaard brengen we die pinnen hoog, in dat geval is er geen spanningsverschil en vloeit er geen
stroom. Vervolgens kunnen we een cijfer klaarzetten op de 8 anode pinnen en de overeenkomstige
kathode laag trekken om het op één van de 4 posities te tonen. Daarna brengen we de kathode
weer hoog, zetten het volgende cijfer klaar en brengen de overeenkomstige kathode laag. Zo
itereer je continu over de 4 cijfers, na het 4de cijfer begin je opnieuw van voor af aan.
Schrijf een sketch op de Arduino, die 4 cijfers van de pi ontvangt. Die 4 cijfers toon je op het display
tot dat er nieuwe data van de pi binnenkomt. Ter bevestiging van de ontvangen data, stuurt de
arduino de 4 cijfers aangevuld met “ok” terug naar de pi.
De pinlayout van het display kan je hier terugvinden :
https://nl.aliexpress.com/item/0-36inch-4digits-red-7-segment-led-display/32584341214.html

## 4) Tijd inlezen op de pi
Vraag de huidige tijd op de met de Raspberry pi. Verbind de pi met de Arduino, vergeet de
levelshifter niet!
Stuur de huidige tijd door naar de Arduino. Lees de bevestiging binnen die je terugkrijgt van de
Arduino. (enkel uur en minuten doorsturen = 4 cijfers)
Sluit nog een knop aan op de pi. Als er op deze knop gedrukt wordt, laat je gedurende 5 seconden,
de seconden afspelen op het 4*7 segment display.

## 5) RGB led
Sluit een RGB led aan (incl…) . Maak voor elke kleur een instantie aan van de klasse PWM_led. Laad
de X-as van de joystick overeenkomen met één kleur, de Y-as met een tweede kleur. Het derde kleur
is het gemiddelde van de eerste twee kleuren. Reken de schaal van de joystick om naar een
percentage.

## 6) LCD display met shiftregister of PCF8574
Het LCD display is in 8 bits modus een ware GPIO pinnen vreter. Daarom zullen we de 8 databus
lijnen van het LCD display aansluiten op de 8 uitgangen van de PCF8574 of het shiftregister. Aan
jullie de keuze. Je kan ze natuurlijk ook allebei uitproberen. 😊 De RS en de E pinnen kan je
rechtstreeks aansluiten op de Pi.
