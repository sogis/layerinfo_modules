# Heatdrill

Liefert für die geklickte Koordinate Grundlageinformationen bezüglich der Bewilligung von Erdwäremsonden-Bohrungen. Die Informationen sind ausschliesslich für die Fachanwender im AfU verständlich (Sind nicht allgemeinverständlich Aufbereitet).

Nutzt für die Abfrage den Heatdrill-Service (repo heatdrill), und adaptiert dessen Antwort für die Anzeige im Web GIS Client.

## Betriebsdokumentation

* Umgebungsvariable
* Abhängigkeiten auf Bibliotheken
* Packetierung
* Fehlerausgabe
* ...

## Entwicklungsdokumentation

Zur (Weiter-)Entwicklung muss lokal die bezüglich der Versionen passende Python-Umgebung erstellt werden. Mittels dem Skript pyruntime/setup.sh wird:
* Die Python V 3.6.x runtime unter pyruntime/venv36 erstellt
* Die notwendigen Bibliotheken in venv36 hinein installiert

Mittels gradle wrapper werden:
* Mock-Datenbank und Mock-Heatdrill-Service gestartet: **startEnvironment**   
Nach dem Start muss http://localhost:8080/service?x=2600000&y=1250000 eine korrekte Antwort erzeugen.
* Tests ausgeführt: **test**
* Das python package nach erfolgreichen UnitTests unter /dist als zip erstellt. Die Versionierung erfolgt über das Datum im Dateinamen des zip. **packageDistribution**

Details siehe in Datei build.gradle. 

### UnitTest Output
Nicht von der Ausgabe der UnitTests verwirren lassen. Die Tests decken auch die korrekte Behandlung von Timeouts, falscher URL, ... ab. Entsprechende Meldungen dazu werden beim Ausführen der Tests ausgegeben - Die Tests sind aber erfolgreich, solange der Returnvalue "0" ist. Gradle meldet dann **BUILD SUCCESFUL** . 


