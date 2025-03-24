# 1 Gruppövning
  
Gör gärna uppgifterna i grupp. Särskilt när man tar fram user stories, acceptanskriterier och testscenarier  finns det ett värde i att diskutera med minst en till.  
  
  
  
1 Betrakta [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/)   
Skriv user stories som beskriver vad användaren ska kunna göra:  
- skapa och ta bort widgets - timer och anteckning
- byta plats på två widgets
- ändra tidsinställning på timer
- starta, pausa, återställ
- ändra texten för anteckning
- ändra temafärg
(Det finns säkert fler saker man kan testa, men ovanstående är de viktigaste.)  
  
Svar:  
`Syntax:  Som en [roll], vill jag [vad], [så att…]`
  
OBS! Widget = Timer eller anteckning  
- US1: Som en användare, vill jag skapa en timer, så att man kan visa tiden hur lång en rast är.
- US2: Som en användare, vill jag skapa en anteckning, så jag kan lämna ett meddelande till mötesdeltagarna.
- US3: Som en användare, vill jag kunna radera vald widget så att jag bara ser de widgets som jag är intresserad av.
- US4: Som en användare, vill jag kunna ändra plats på widget, så att jag exempelvis kan sortera widgets som är prioriterade överst.
- US5: Som en användare, vill jag kunna ändra tiden på timern, så att man kan justera en felaktig tid.
- US6: Som en användare, vill jag kunna starta timer, så att timern börjar räkna ner.
- US7: Som en användare, vill jag pausa timern, så att jag slipper att återställa timer om man råkat starta.
- US8: Som en användare, vill jag återställa timern, så att jag snabbt kan göra mig redo för nästa rast.
- US9: Som en användare, vill jag kunna ändra anteckning, så att jag kan ändra eventuella felaktigheter i texten.
- US10: Som en användare, vill jag kunna kunna ändra temafärg, så att den passar både i ljusa och mörka miljöer.
  
2 Formulera acceptanskriterier för alla user stories.  
  
Svar:  
- [x] AK1.1: Ny timer skall skapas när man trycker på knappen "Add timer"
- [x] AK1.2: Den nya timern skall visa den inställda default tiden

- [x] AK2.1: Ny anteckning skall skapas när man trycker på "Add note"
- [x] AK2.2: Anteckningen skall ha default texten "Click to change text"

- [x] AK3.1: Timers skall raderas med raderas med radera-knappen
- [x] AK3.2: Anteckningen skall raderas med radera-knappen

- [x] AK4.1: Timerns position skall hoppa ett steg upp om man trycker på knappen med en uppil
- [x] AK4.2: Anteckningen position skall hoppa ett steg upp om man trycker på knappen med en uppil

- [x] AK5.1: Timerns minuttid skall kunna ändras genom att man klickar på kugghjulet

- [x] AK6.1: Timern skall börja att räkna ner när man trycker på start knappen

- [x] AK7.1: Timerns skall sluta att räkna ner och behålla tiden som den står på när man trycker på knappen "Paus".
- [x] AK7.2: Knappen "Paus" skall visas när man startat en timer.

- [x] AK8.1: Timerns tid skall ställas till default tiden om man trycker på knappen reset

- [x] AK9.1: Anteckningen text skall kunna ändras om man klickar på texten

- [x] AK10.1: Tema färgerna på elementen på sidan Light (Vit/Blå), Dark (Svart/Grå), Forest (Skogsgrön/Ljusgrön), Orange skall kunna väljas med knapparna "Light", "Dark", "Forest" och "Orange".  
  
  
3 Skriv ner testscenarier för varje acceptanskriterium. (Ett scenario kan täcka in flera acceptanskriterier.)  
  
Svar:  
- [x] TS1: Add timer
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add Timer" (AK1.1)
	- Kontrollera att timer visas med default tiden "15:00" (AK1.1, AK1.2)
- [x] TS2: Start timer
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add timer"
	- Klicka på knappen "Start" (AK6.1)
	-  Vänta 1s
	- Kontrollera att timern räknar ner (AK6.1)
- [x] TS3: Pause timer
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add timer"
	- Klicka på knappen "Start"
	- Klicka på knappen "Pause" (AK7.2)
	- Vänta 1s
	- Kontrollera att tiden är samma (AK7.1)
- [x] TS4: Reset timer
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add timer"
	- Klicka på knappen "Start" (AK6.1)
	- Vänta 1s
	- Klicka på knappen "Reset" (AK8.1)
	- Kontrollera att default tiden är satt (AK8.1)
- [x] TS5: Remove timer
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add Timer"
	- Räkna antalet widgets
	- Klicka på knappen som ser ut som papperskorg med klassen "icon close" (AK3.1)
	- Kontrollera att antalet widgets är en mindre än innan (AK3.1)
- [x] TS6: Adjust time
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add Timer"
	- Klicka kugghjulet (AK5.1)
	- Ändra antal min 11 min i settings menyn (AK5.1)
- [x] TS7: Add note
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add note" (AK2.1)
	- Kontrollera att timer visas med default tiden "Click to change text" (AK2.1, AK2.2)
- [x] TS8: Remove note
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add note"
	- Klicka på knappen som ser ut som papperskorg med klassen "icon close" (AK3.2)
	- Kontrollera att anteckningen inte syns längre (AK3.2)
- [x] TS9: Change note
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add note"
	- Klicka på texten "Click to change text" (AK9.1)
	- Ändra antecknings texten till "Test change note text" (AK9.1)
	- Kontrollera att texten har ändrats (AK9.1)
- [x] TS10: Adjust position
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Klicka på knappen "Add timer"
	- Klicka på knappen "Add note"
	- Kontrollera att note elementet ligger sist
	- Tryck på knappen med en pil upp (klassen "icon up") på note elementet (AK4.2)
	- Kontrollera att timer elementet ligger sist
	-  Tryck på knappen med en pil upp (klassen "icon up") på timer elementet (AK4.1)
	- Kontrollera att note elementet ligger sist
- [x] TS11: Change theme
	- Gå in på på sidan: [https://lejonmanen.github.io/timer-vue/](https://lejonmanen.github.io/timer-vue/) 
	- Kontrollera att titeln på sidan är: "Timer app"
	- Kontrollera att default tema är "Light" (data-theme = "null")
	- Klicka på knappen "Dark" (AK10.1)
	- Kontrollera att tema är "Dark" (data-theme = "dark") (AK10.1)
	- Klicka på knappen "Forest" (AK10.1)
	- Kontrollera att tema är "Forest" (data-theme = "forest") (AK10.1)
	- Klicka på knappen "Orange" (AK10.1)
	- Kontrollera att tema är "Orange" (data-theme = "orange") (AK10.1)
	- Klicka på knappen "Light" (AK10.1)
	- Kontrollera att tema är "Light" (data-theme = "") (AK10.1)
  
4 Implementera E2E-tester i Playwright för utvalda scenarier. Gör så många ni hinner med.  
Code review! Om ni delar upp arbetet: se till att återsamlas och visa upp den koden ni har skrivit.  
  
Svar:  
[Uppgift 1.4](./Uppgift1_4/test_timer_app.py)
  
Resultat:  
```
============================= test session starts =============================
platform win32 -- Python 3.13.2, pytest-8.3.5, pluggy-1.5.0
rootdir: c:\Users\dawa01\Documents\Python Scripts\nbi\TAPHT24D_TT
configfile: pytest.ini
plugins: base-url-2.1.0, playwright-0.7.0
collected 11 items

Veckouppgift3/Uppgift1_4/test_timer_app.py::TestTimer::test_add_timer[chromium] PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestTimer::test_start_timer[chromium] 
-------------------------------- live log call --------------------------------
2025-03-24 21:40:19 [    INFO] test_timer_app :32       Start time: 15:00
2025-03-24 21:40:20 [    INFO] test_timer_app :39       Present time: 14:59
PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestTimer::test_pause_timer[chromium] 
-------------------------------- live log call --------------------------------
2025-03-24 21:40:21 [    INFO] test_timer_app :60       Pause time: 14:59
2025-03-24 21:40:22 [    INFO] test_timer_app :65       Present time: 14:59
PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestTimer::test_reset_timer[chromium] 
-------------------------------- live log call --------------------------------
2025-03-24 21:40:24 [    INFO] test_timer_app :84       Time: 14:59
2025-03-24 21:40:24 [    INFO] test_timer_app :91       Reset time: 15:00
PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestTimer::test_remove_timer[chromium] 
-------------------------------- live log call --------------------------------
2025-03-24 21:40:24 [    INFO] test_timer_app :109      Number of widget when timer is added: 2
2025-03-24 21:40:24 [    INFO] test_timer_app :116      Number of widget when timer is removed: 1
PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestTimer::test_adjust_time[chromium] PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestNote::test_add_note[chromium] PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestNote::test_remove_note[chromium] 
-------------------------------- live log call --------------------------------
2025-03-24 21:40:25 [    INFO] test_timer_app :151      Number of widget when note is added: 2
2025-03-24 21:40:25 [    INFO] test_timer_app :157      Number of widget when note is removed: 1
PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestNote::test_change_note[chromium] PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestOther::test_adjust_positon_of_widget[chromium] PASSED
Veckouppgift3/Uppgift1_4/test_timer_app.py::TestOther::test_change_theme[chromium] 
-------------------------------- live log call --------------------------------
2025-03-24 21:40:26 [    INFO] test_timer_app :200      Theme: null
2025-03-24 21:40:26 [    INFO] test_timer_app :206      Theme: dark
2025-03-24 21:40:26 [    INFO] test_timer_app :211      Theme: forest
2025-03-24 21:40:26 [    INFO] test_timer_app :216      Theme: orange
2025-03-24 21:40:26 [    INFO] test_timer_app :221      Theme: 
PASSED

============================= 11 passed in 19.54s =============================
Finished running tests!
```
  
# 2 Öva mera  
Testa på samma sätt exemplet från genomgången:  
[https://tap-ht24-testverktyg.github.io/form-demo/](https://tap-ht24-testverktyg.github.io/form-demo/)  
  
Svar:  
Ej gjord