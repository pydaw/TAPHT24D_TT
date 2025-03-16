
# 1 Diskutera i grupp
Denna gången är det en fördel att diskutera de flesta uppgifterna.  
Planera din tid, så att du hinner arbeta med alla övningarna.  
Du ska alltså inte göra "färdigt" alla tidigare övningar innan du går vidare på nästa.  
  
1a  
Vilka strängar matchas av det reguljära uttrycket: "ab" ? Testa era svar på https://regex101.com/  
a. "a b"  
b. "aBBa"  
c. "sabotör"  
  
Svar:  
c - måste matcha med samma case som strängen man jämför med.  
  

1b  
Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?  
  
Svar:  
Genom använda ignore case flaggan.  
(?i)nisse  
  
1c  
Vilka strängar matchas av "a\*n" ?  
a. "an"  
b. "amerikan"  
c. "naturlig"  
d ."annandag"  
  
Svar:
Matchar alla efter som * = 0 eller fler tecken
  
  
1d  
Vilka strängar matchas av "[ae]n" ?  
a. "naiv"  
b. "inconsequential"  
c. "bae"  
  
Svar:  
Matchar "an" eller "en"  
dvs. b  
  

1e  
Vilka strängar matchas av "je.+e"?  
a. "je"  
b. "jee"  
c. "jeppe"  
d. "je je"  
  
Svar:  
. Matchar vilken single character som (även "white charaters" så som mellanslag) och + är ett eller flera tecken.  
dvs c och d  
  

1f   
Vilka strängar matchas av "\san?\s"  
a. "sansad"  
b. " annan "  
c. "    an   na   an   "  
d. "be a darling"  
  
Svar:  
Strängen skall ha en "white space" char innan och efter strängen samt skall börja med an  
men kan sluta på vilken annan character som även ingen. dvs " an " eller " a "  
c och d  
  
  
1e  
Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"  
a. "lines?"  
b. "^a*ö$"  
c. "[aeiouyåäö]+"  
d. "[123456789]\d*"  
e. "\d{4}-\d{2}-\d{2}"  
  
Svar:  
a. line eller lines  
b. strängen måste börja med a och sluta med ö  
c. strängen måste innehålla vokaler men kan vara ett eller flera tecken.  
d. förstod inte riktigt vad man skulle åstadkomma med denna. Strängen matchar med 1-9 och även vilken siffra som. Så antar att man ute efter siffror.  
e. datum.... 2025-03-02  
  
  
2a   
Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".
  
Svar:  
"Som en användare vill kunna läsa hur man gör en sprint retrospective så användaren vet hur man kan avsluta en sprinten."  
  

2b Skriv ner ett testscenario för user storyn. Använd en punktlista. Fundera särskilt på vad som ska testas implicit och explicit.  
Implicit = underförstått, testas indirekt  
Explicit = uttryckligen, testas direkt  
  
Svar:  
Scenario:  
1. Öppna webbläsaren och gå till sidan https://lejonmanen.github.io/agile-helper/  
2. Tryckt på knappen "Last"  
3. Tryck sedan på knappen "... Sprint retrospective"  
4. Kontrollera en del av text som sällan ändras  
5. Tryck på knappen "The sprint is complete"  
  
  
3  Titta på kodexemplet från lektionen. Skriv upp allt du är osäker på och diskutera i grupp eller fråga om på nästa lektion.  
  
```python
def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()
    
    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()
```
  
Svar:  
Vad händer om man har flera element som liknar varandra men sedan anropar ex click().  
Ex istället för "Sprint planning" anropar man "Start" då man letar efter knappen.  
  

# 2 Öva på regex  
1a Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:  
"Fiskarna som jag fångade var 55 cm långa."  
  
Svar:
Längden på antalet siffror kan variera där av "\d*\d"  
Sedan kanske man inte har mellanslag mellan cm och värdet där av "?" efter mellanslaget.  
"\d*\d ?cm"  
  

1b Denna gången vill vi veta om det finns två längder.  
  
Svar:  
`(\d*\d\s?cm).+?(\d*\d\s?cm)`  


1c Längderna ska vara samma enhet.  
"Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."  
  
Svar:  
`(\d*\d\s?cm).*?(\d*\d\s?cm)|(\d.*\d\s?m).*?(\d.*\d\s?m)`  
  
2 Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"  
Om du vill övertänka fördjupa dig mera: https://sv.wikipedia.org/wiki/Postnummer_i_Sverige   
  
Svar:  
`\d{3}\s\d{2}`  
  

3 Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.  
  
Svar:  
`\d{4}-\d{2}-\d{2}`  
  

4 Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas:  
200 kr  
12,50 kr  
0,35 kr  
  
Svar:  
`\d.*\skr`  
  

5a Skriv ett regex som matchar en e-postadress (`användarnamn@server.domän`) enligt följande icke kompletta regler.  
användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck  
server kan innehålla samma sorts tecken  
domän kan innehålla bokstäver och siffror  
  
Svar:  
`([a-zA-Z0-9.\-]*)@([a-zA-z0-9.\-]*).([a-zA-Z0-9]*)`  
  

5b Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln här:  
What is a valid email address format  
  
Svar:  
Tyckte inte jag fick till någon bra lösning.  
  
  
# 3 Öva på user stories  
Skapa user stories som beskriver funktionaliteten i https://lejonmanen.github.io/agile-helper/   
För varje user story ska du skriva ett scenario. Målet är att all befintlig funktionalitet ska täckas in av en user story - alla knappar ska bli klickade minst en gång.  
Gör gärna den här uppgiften tillsammans med klasskamrater, så ni kan diskutera era scenarion, skillnader och likheter.  
  
Exempel:  
[User story 1]  
Story: Som en användare, vill jag se mötet "sprint planning" som utspelar sig första dagen på en sprint, så att jag vet vad jag ska göra på mötet.  
  
Scenario:  
Navigera till webbsidan https://lejonmanen.github.io/agile-helper/   
Klicka på knappen med texten "First"  
Klicka på knappen vars text innehåller "Sprint planning"  
Kontrollera att ett `<dialog>` element visas på sidan, som innehåller en rubrik med texten "Sprint planning"  
  
Svar:  
[User story 1]  
Story:  
Som en användare, vill jag se mötet "sprint planning" som utspelar sig första dagen på en sprint, så att jag vet vad jag ska göra på mötet.  
  
Scenario:  
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen som innehåller texten "first"
- Klicka på knappen vars text innehåller "Sprint planning"
- Kontrollera att ett `<dialog>` element visas på sidan, som innehåller en rubrik med texten "Sprint planning"
- Klicka på knappen vars text innehåller "Ok we're done"
  
  
[User story 2]  
Story:  
Som en användare, vill jag se mötet "daily stand up" som utspelar sig varje dag under sprintens gång, så att jag vet vad jag ska göra på mötet.  
  
Scenario:  
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen innehåller texten "first", "middle" eller "last"
- Klicka på knappen vars text innehåller "Daily standup"
- Kontrollera att ett `<dialog>` element visas på sidan, som innehåller en rubrik med texten "Daily standup"
- Klicka på knappen vars text innehåller "Ok we're done"
  
  
[User story 3]  
Story:  
Som en användare, vill jag under "daily stand up" kunna starta en timer, så att jag vet att mötet kommer hållas kort.  
  
Scenario:  
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen innehåller texten "first", "middle" eller "last"
- Klicka på knappen vars text innehåller "Daily standup"
- Kontrollera att det finns ett `<span>` element med texten `--:--`
- Klicka på knappen vars text innehåller "Start the standup: 10minutes"
- Kontrollera att `<span>` element av klassen "`framed `"   innehåller texten `9:`
  
  
[User story 4]  
Story:  
Som en användare, vill jag se vilket arbete som skall presenteras för produkt ägaren under en "Sprint review" som utspelar sig sist under sprinten, så att jag vet vad som skall presenteras.  
  
Scenario:  
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen innehåller texten "last"
- Klicka på knappen vars text innehåller "Sprint review"
- Kontrollera att ett `<dialog>` element visas på sidan, som innehåller en rubrik med texten "Sprint review"
- Klicka på knappen vars text innehåller "Ok we're done!"
  
  
[User story 5]  
Story:  
Som en användare, vill jag se vad som skall göras under "Sprint retrospective" som utspelar sig efter sprinten, så att jag vet vilka frågor som skall besvaras samt se hur sprinten har gått och bli bättre till nästa sprint.  
  
Scenario:  
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen innehåller texten "last"
- Klicka på knappen vars text innehåller "Sprint retrospective"
- Kontrollera att ett `<dialog>` element visas på sidan, som innehåller en rubrik med texten "Sprint retrospective"
- Klicka på knappen vars text innehåller "complete"
  
  
[User story 6]  
Story:  
Som en användare, vill jag kunna komma kunna navigera tillbaka i menyerna, så att jag vet att jag kan välja rätt meny om jag tycker fel.  
  
Scenario:  
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen med texten "First", "Somewhere in the middle" eller "Last"
- Kontrollera att knappen med texten "Start over" finns
- Klicka på knappen med texten "Start over"
  
  
# 4 Öva på E2E test
Utgå från dina user stories och scenarion i föregående uppgift. Skriv kod med Playwright som testar dem. Ta hjälp av kodexemplet i presentationen.  
  
Svar:  
[Uppgift 4 - E2E test](./Veckouppgift2/Uppgift4/test_agile_helper.py)  
  
```bash
============================= test session starts =============================
platform win32 -- Python 3.13.2, pytest-8.3.5, pluggy-1.5.0
rootdir: c:\Users\dawa01\Documents\Python Scripts\nbi\TAPHT24D_TT
configfile: pytest.ini
plugins: base-url-2.1.0, playwright-0.7.0
collected 12 items

Veckouppgift2\Uppgift4\test_agile_helper.py ............                 [100%]

============================= 12 passed in 14.93s =============================
Finished running tests!
```

