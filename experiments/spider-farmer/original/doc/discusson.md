@[REDACTED:maintainer-handle:SF-IMPL-1]
Description
[REDACTED:maintainer-handle:SF-IMPL-1]
opened on Mar 3
lets use this for discussions

Activity
[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-1]
on Mar 3
Author
I also started decompiling and found a rsa key+cert, based on the name i guess its used for mqtt.

Also i already sent my updated CB controller back to amazon :) but i still have msg dumps and can always order another one.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 3
Schau dir die files an. Ich habe einmal die Android app angefangen zu decompeliren und die software von den led lampen kontoller der oben auf den lampen sitz.

Das sie haben in der APP zwei zertifikatsdatein die sie nutzen um die verbindung zum cloud service abzusichern. und einemal ein hardcode zertifikat für eine TLS verbindung von den gräten untereinander

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 3
Ich habe auch ein teil der lampen software schon wieder hergestellt das liegt aber nicht bei das ist ein Ghidra projekt.
Ob jetzt das Hardcodierte certifikat auch für die verschlüßellung von den über bluetooth gesendeten JSON strings verwendet wird weiß ich noch nicht

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 3
Mein ziel ist das selbe wie deins ich möchte das man alle Produkte von SF mit Home Assistenten nutzen kann am besten ohne ihren eigenen Kontroller eben direkt.

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-1]
on Mar 3
Author
Ok,

Doofe an der app, ist flutter, da gibts blutter, kann aber zummindest bei mir mit der 32bit arm nix anfangen.

Interessant ist, dass Du die firmware dumps hast, ggf. schau ich mal, ob da was auf meinen esp32-s2, läuft. Ist einfacher als die echte hw zu flashen.

Werde auch etwas rumprobieren. Die echte hw ist aktuell in verwendung und wird von kumpel genutzt. Habe nur die esphome componente gebaut, dass man das schön in home assistant sieht. Werde denke ich mal auch die schreib funktionen einbauen.

Aktuell wird halt die power leiste und lampe verwendet.

Mein ziel ist das selbe wie deins ich möchte das man alle Produkte von SF mit Home Assistenten nutzen kann am besten ohne ihren eigenen Kontroller eben direkt.

ah du meinst, über das rj12 interface?

Ich habe an sich nix gegen den CB oder powerstrip controller, aber das der das WLAN PW über BLE an die welt schickt ist nicht so super :)

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 3
ah du meinst, über das rj12 interface?

nee ich habe lampen mit

Image
Schaue dir dazu die an: https://github.com/[REDACTED:maintainer-handle:SF-IMPL-2]/ReverseEngineeringSpiderFarmer/blob/master/SpiderFarmer_SE1500_Hardware.md

die verfügen über BLE & WLAN davon ist auch der Firmware dump habe leider keinen SF-GGS-CB

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-1]
on Mar 3
Author
Ah, ja die lampe ist hier auch im einsatz, aber wird in dem fall über rj12 und über SF-GGS-AC5 gesteuert, deswegen habe ich keinen direkten support für die lampe in die esphome componente eingebaut, aber da die 1.5 fw verwendet wird, sollte ich einfach direkten support einbauen können.

Ich nehme an, 1.7 ist dann verschlüsselt?

Ggf. ist es einfacher die fw zu analysieren statt die app.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 3
Also die Lampen kann man über Bluetooth oder Wlan steuern.

Mit der Version 1.7 haben sie die Bluetooth Kommunikation verschlüsselt.

Jetzt bin ich in der APP und Firmware auf der suche wie sie das machen.
Mich interessiert auch der Verbindung Prozess
Und was nach China gesendet wird
[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 3
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 3
Ich glaube die Lampe bietet einen MQTT Server an über den sie sich steuern lässt. Ich versuche derzeit einen Wlan-AP zu simulieren um den Datenverkehr switchen Lampe und App im Wlan unverschlüsselt Mitzuschneiden.

Damit ich sehen was sie hin und her sendet was auf Bluetooth läuft habe ich schon gut raus sie dazu in die Excel datein

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented on Mar 9
[REDACTED:maintainer-handle:SF-IMPL-1]
on Mar 9
Author
hab etwas mit ghidra und der firmware rumgespielt, finde aber leider bis auf wo die json gebaut werden nicht viel bezüglich der verschlüsselung/obfuscation.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 10
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 10
Ich suche derzeit nach den 3 Standard Möglichkeiten die der ESP32 mitbringt für Bluetooth LE mit SMP. In Ghidra

Mein verdacht ist auch das sie eventuell - die uid nutzen als Password. Für die Standard Methode der Verschlüsselung mit Passwort.
Weil eigentlich im Speicher NVS des EPS32 der key der Ausgehandelt Verbindung stehen müsste dies tut er aber nicht
ich habe einen Firmware dump ausgelesen nach Bounding. Das einzige was im NVS gespeichert ist und nicht Standard ist.

benutzeremail
und
uid

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 10
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 10
In der Firmware ist ja fast alles aus den Espressiff Standart Componenten von der ESP-IDF 5.3.2

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 11
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 11
Image
Ist das nun die Default Funktion oder ist sie von MZ modifiziert so nennt sich der Entwickler der Android APP

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 15
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 15
Ich bin jetzt einen schritt weiter gekommen ich werde die weiteren functionen wieder herstellen. siehe in dem ghidra file zum import.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented on Mar 21
[REDACTED:maintainer-handle:SF-IMPL-2]
on Mar 21
https://gitlab.informatik.uni-bremen.de/fbrning/esp-idf/-/blob/bd8b81ee8d6cae0c5b0ccd3c6a7aefc5e091e428/components/mbedtls/port/aes/dma/esp_aes.c#L695

AES128
CBC 16
KEY BkJu61kLt3afuogT

47 remaining items
[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
3 days ago
Author
Ja ist selbe für encrypted:

Decoded: MSG: 0002 ID: 4255 TOTAL: 608 OFF: 0 SIZE: 400 CRC: 19015 vs 19015
Decoded: MSG: 0002 ID: 4255 TOTAL: 608 OFF: 400 SIZE: 208 CRC: 49210 vs 49210

CRC ist auch über header + daten

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
3 days ago
Author
Hm, wie genau bist du an den IV gekommen?

Habe leider keine lampe zum gegentesten die ich flashen kann, aber mein powerstrip 10 scheint einen anderen IV zu haben. kommt auf jedenfall nur schmarrn raus.

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
3 days ago
Author
Hab da was nettes online gefunden zum testen:

https://emn178.github.io/online-tools/aes/decrypt/?input=5ba9330ef5e7cb8c477097de6f737fcb308bf7e10eddaa90e1d17106be2c6ee845419370b016adda873ef03e75526d78faf285cc29046a76e17938b14bc6c7859b819d48ff015aa15f6706c67af0b729b32d7f78edd68c051dc49079747c3e38d51fcb471bdf531b970a378fd626cd28e92159e4ff71e415e45a5c87a26ce8e858eb5f5dc17b1a34b1e8a0f4019ec26e55f286f6e41d181f33f9da0b5552c37087c567ccb194dda9b49bfc1269296cc1bec70c26e4f26dbb1e64d399f536f269e9e148185497b842163061681a313170d7cd7295c7b08331a8af64d0cfd9ec176c92d0a9231c8ba893b749b2590e3ac7b4995f7c0729317f6bd22f372036c8b17d798fd8bb86d7a2f2cecc008ff2e605689a4ecf00d0015955b335b6a9f83b9e3346f1e08754672295b9cc3c74279bb0d3a5f68a87d0b74d0c435b6324f6078327c0e35d8995ccf2145cfb09493b2cce5535bc0299c35d289fe1c24afacb3a02e6d47de46c4d48977856646790da112ba95450cef9cad2617a5590af8255b960&source=text&input_type=hex&output_type=hex&key_size=128&mode=CBC&padding=NoPadding&key_type=custom&hash=SHA256&custom_iteration_enabled=0&iteration=1&key_input_type=utf-8&key=&iv_input_type=utf-8&iv=

Wenn man die Keys eingibt, liefert der die selbern werte die ich bekomme aber die daten sind nur kauderwelsch.

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
3 days ago
Author
Image
[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
3 days ago
Author
Fucking hell:

List of potential key/iv values:

BkJu61kLt3afuogT
2AKVNUbU4mvU3Elt
h411AfTnVVusvsjE
2pci13UbdjPR1ble
75YdgtITdMfiyS5x
84Rf7SUkinfvxNlc
FIUz0N1xrmaaso61
J4G0M9dX1f1v3fXr
RnWokNEvKW6LcWJg
br3MSw3YDM0gRdEP
iVi6D24KxbrvXUuO
lVIlATSlxaS1btfd
mKli62mtym9j6Odi
v04Y436txRWeHd6w
At least for my PS10 it seems to be:

lVIlATSlxaS1btfd and 84Rf7SUkinfvxNlc

Need to see how the mapping works and also if i made a typo, since i actually extracted them semi manually via ghidra and a wildcard search of the android app.

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
3 days ago
Author
Yay, works, getting all values as before. with version 3.14 on the SF-GGS-PS10.

Now code cleanup and adding config option to set key and iv.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-2]
3 days ago
Hm, wie genau bist du an den IV gekommen?

Habe leider keine lampe zum gegentesten die ich flashen kann, aber mein powerstrip 10 scheint einen anderen IV zu haben. kommt auf jedenfall nur schmarrn raus.

Ich habe den FLash ausgelesen und in diesem dump dort die ram offsets die in der software verwendet wurden.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented 3 days ago
[REDACTED:maintainer-handle:SF-IMPL-2]
3 days ago
android app.

Der erste verbindungs aufbau findet ja wohl immer über bluetooth stat. Ich denke mal das sie über den bluetooth adversting device name und den magic header erkennen welches Produkt es ist und dadurch dann den iv einstellen.

Ich habe noch mehre lampen aus den ich den dump lesen könnte um zu prüfen ob es der selbe iv ist. diese prüfung wird ja eh auf mich zu kommen aber grade schreibe ich hier dran

Ich werde ja testen ob das geht:
https://github.com/[REDACTED:maintainer-handle:SF-IMPL-2]/SpiderBEL_ESPtoMQTT/

Image
[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented 2 days ago
[REDACTED:maintainer-handle:SF-IMPL-1]
2 days ago
Author
Ich denke mal das sie über den bluetooth adversting device name und den magic header erkennen welches Produkt es ist und dadurch dann den iv einstellen.

Denke ich auch, wobei der KEY und IV anders ist.

Ich habe noch mehre lampen aus den ich den dump lesen könnte um zu prüfen ob es der selbe iv ist. diese prüfung wird ja eh auf mich zu kommen aber grade schreibe ich hier dran

glaube nicht das dies nötig ist. die von Dir gefunden KEY und IV kombo sind in der firmware drinnen. die anderen KEYs und IVs die ich gestern Nacht extrahiert habe nicht. Also gehe ich davon aus, dass alle lampen, die mit der FW 1.7 laufen, diese nutzen.

Ich bin mit meiner ESP Home Componente nun soweit, dass wenn ich "meine" keys im code hardcode, das entschlüsseln wunderbar klappt.

Werde jetzt daran arbeiten, dass diese via config einstellbar sind, somit könntest Du ggf. damit auch testen. Werde aber noch an vollem Lampen support arbeiten müssen, aktuell nur controller support. CB, PS10 und PS5, was das Auslesen der Daten geht.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented 2 days ago
[REDACTED:maintainer-handle:SF-IMPL-2]
2 days ago
Werde jetzt daran arbeiten, dass diese via config einstellbar sind,

Als tip nutze einfach mal google ki zum code schreiben nimmt mir nee menge Arbeit ab: einfach den ganzen code aus deiner main.cpp einfügen und dann formulieren was du noch willst. ist nicht immer perfekt und Fehler frei aber extrem hilfreich.

[REDACTED:maintainer-handle:SF-IMPL-2]
[REDACTED:maintainer-handle:SF-IMPL-2] commented 2 days ago
[REDACTED:maintainer-handle:SF-IMPL-2]
2 days ago
glaube nicht das dies nötig ist. die von Dir gefunden KEY und IV kombo sind in der firmware drinnen. die anderen KEYs und IVs die ich gestern Nacht extrahiert habe nicht. Also gehe ich davon aus, dass alle lampen, die mit der FW 1.7 laufen, diese nutzen.

Ja macht ja auch sinn wenn sie für jede art von gerät einen andren IV haben dann kann man ja so schon den daten import von einem
falschen gerät verhindern. Ich meine aus Sicht von dem Spider Farmer Controller.

Leider brauche ich die anderen Sachen von Spider nicht nur die Lampen würde sonnst gern mal von allen dumps ziehen um zu verstehen wie es läuft.. Aber ich denke aus Sicht der einzelnen Bauteile, Lüfter, Pumpen, Lampen
werden sie es so machen das sie die model.txt nutzen die in der Firmware ist um das verhalten der Software etwas zu
verändern je nach gerät.

noheton
noheton commented 2 days ago
noheton
2 days ago · edited by noheton
Bin leider gerade etwas busy aber muss mal am Wochenende sehen, ob ich meinen Controller (ohne Steckdosen) eingebunden bekomme.

Die mqtt Sache läuft - aber dann ist erst mal nix mit app. Wäre zu verschmerzen, aber steuern muss ich noch implementieren.

Zum Thema KI coding - mach da gerade viele Erfahrungen... So wirklich hab ich da noch keine best practice. Aber ist schon richtig, dass das manchmal gut helfen kann.

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented yesterday
[REDACTED:maintainer-handle:SF-IMPL-1]
yesterday
Author
@noheton

kann gerne meinen branch von meiner esphome componente pushen, hier kannst du dann testen welcher key für den reinen controller passt. Traue mich mein PS5 nicht zu flashen, da in verwendung aber mit meiner amazon "leihgabe" PS10 gehts gut.

Werde hiermit auch schauen dass ich die dosen als switch implementiere und die ein oder andere sache auch schreibend.

[REDACTED:maintainer-handle:SF-IMPL-1]
[REDACTED:maintainer-handle:SF-IMPL-1] commented yesterday
[REDACTED:maintainer-handle:SF-IMPL-1]
yesterday
Author
OK, hier mein PR/Branch: [REDACTED:repo-path:SF-IMPL-1]#6

noheton
noheton commented yesterday
noheton
yesterday
@[REDACTED:maintainer-handle:SF-IMPL-1] ich guck's mir an und geb dir Rückmeldung.
Nur noch morgen dann ist endlich Wochenende...
