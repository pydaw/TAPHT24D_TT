
# Veckouppgift 7 - CI/CD

1. Beskriv ett CI/CD-flöde för ett tänkt projekt (till exempel en Flask-app eller webbtjänst).  
	a. Vad händer när utvecklaren pushar kod?
	- När utvecklaren pushar sin kod till Git så är det meningen att en pipeline startas. Ofta finns denna pipeline i Git verktyget som man använder Ex i GitHub så heter denna GitHub actions. Men går även att ha externa verktyg för detta exempelvis Jenkins.
	- När Pipelinen startas så körs olika automatiserade tester samt byggprocesser.
	
	b. Vilka tester ska köras?
	- Vilka tester som skall köras beror till stor del av vad som är viktigast för att applikationen skall fungera tillförlitligt.
	- Smoke tester körs först för att snabbt kunna se om något har gått sönder och att applikationen kan startas upp och köras. Att detta körs först är för att utvecklaren skall få en snabb feedback att det inte hänt något kritiskt med applikationen.
	- Enhetstester -  minsta byggstenarna och funktioner i applikationen
	- Linter tester - kontrollera att kodbasen följer den beslutade syntaxen
	- Integrationstes - det är bra att testa mot delar i koden som skall prata externt med api eller andra kritiska funktioner.
	- Prel E2E tester -  beror på applikationen vad som skall testas här men men kan vara bra att se att det gå att stega runt som en användare och använda de grundläggande funktionerna i applikaktionen.

	c. När och hur byggs applikationen?
	- Beror på applikation om det till exempel kompilerad kod kan man behöva bygga innan innan smoketesterna eller integrationstesterna. Är det en webtjänst skriven i Python kan man bygga det sista man gör efter att man kört alla tester.
	- Python webbexemplet kan det röra sig om att lägga koden i en container.
	  
	d. Rita flödet som en enkel bild eller lista.

    ``` mermaid
        flowchart TD
        A[CI/CD] --> B(Steg1: Utvecklare pushar koden till Git) --> C(Steg2: Pipeline triggas) --> D(Steg3: Smoketester) --> E(Steg4: Linting) --> F(Steg5: Enhetstester) --> G(Steg6: Integrationstester) --> H(Steg7: E2E tester) --> I(Steg8: Bygger applikationen Ex skapar en container) --> J(Prel. Steg9: Deployment i stagingmiljö - om manuell granskning krävs) --> K(Prel. Steg10: Manuell granskning) --> L(Steg11: Deployment i produktionsmiljö) --> A
    ```


	e. Vad skulle kunna gå fel i flödet?
	- Tester kan fallera
	- Externa 3:e parttjänster kan vara nere (Ex api'er som testas under integrationstesterna)
	- Syntax kan vara felskriven och stoppas av linting test
	- Bygget kan det vara paket som ej finns längre

	f. Vilka tester är viktigast i just ditt flöde?
	- Smoketesterna - eftersom där visas det om applikationens kritiska funktioner fungerar, samt blir ett snabbt test.
	  
	g. Hur kan testning förbättra kvaliteten?  
	- Man gör i ofta inte lika stora releaser utan mindre releaser som sker oftare. Detta göra att man litar mer att den lilla förändringen inte kommer att påverka så mycket på koden.
	- Testningen kommer också ge snabb feedback till utvecklaren i ett tidigare skede, vilket gör att resultatet i slutet av processen håller högre kvalité.

2. Hur tror du att automatiserad testning påverkar en utvecklares vardag?  
	Förhoppningsvis så kommer den påverka det till det positivare om testerna gör att utvecklaren kan hitta fel i koden fortare. Detta gör att man kan lita på koden och man får bättre kvalité på produkten.
	
	Om testerna däremot är instabila kan detta göra att man inte litar på testerna eller sin kod man skrivit. Risken är då att processen och releaserna blir tröga, och kvalitén blir inte lika bra..

3. Vad är en fördel och en nackdel med att ha testning inbyggd i CI/CD-flödet?  
	 **Fördelar**
	 - Fel kan upptäckas i ett tidigare stadie
	 - Agilt arbetssätt med fortare releaser i mindre steg
	 - Högre kvalité på koden

	**Nackdelar**
	- Om man har mycket tester, samt att testerna tar lång tid att köra. Kan feedbacken ta väldigt lång tid att få.
	- Kan ta mycket tid att underhålla testerna om kodbasen växer. Men är i de flesta fall värt detta pga kvalitetshöjning.
	

5. Om du skulle införa CI/CD i ett skarpt projekt – vad skulle du börja med?  
	- Skulle se om verktyget som jag använder till Git har inbyggd funktion för detta, samt tittat på om man kommer hela vägen med detta verktyget. Ex om man vill lägga till framtida E2E-tester är det möjligt.
	- Även tänka att man börjar smått och inför pipelinen steg för steg.
	- Börja med enkla enhetstester
	- Lägg till deployment steget. Kan vara bra att börja med att sätta manuellt granska innan släpp eftersom man inte har så många tester i början.
	- Fyll på med mer anvancerade tester så som Ex. integrationstester och E2E.
	- När man väl har ett antal tester på plats, fundera på vilka av dessa är de viktigaste och snabbaste som gör att man kan se om applikationen fungerar. Ange dessa som smoketester.
	- När man börjar att lita på att testerna kommer testa igenom koden på ett önskad nivå kan man börja se om an kan ändra deployment till produktion istället för staging.

6. Hur skiljer sig GitHub Actions från andra CI/CD-verktyg du hört om eller testat?  
   (denna gör du bara om du har erfarenhet från andra CI/CD-verktyg).
	   - På mitt jobb använder vi bitbucket pipeline. Ser väldigt lika ut. Men är säkert många detaljer som inte fungerar lika.
