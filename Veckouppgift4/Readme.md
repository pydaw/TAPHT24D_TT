# Veckouppgift 4
Kursdeltagare: Daniel Wärnelöv

## Hur löstes uppgiften
Uppgiften löstes genom att titta på filmen som spelades under lektionen och härma den koden som skrevs.
Har även tittat på exempel på nätet (på behave dokumentationen, youtube, och diverse bloggar).

Stegen som togs för att lösa uppgiften var:
- Steg1: Skapade python env med `python -m venv .venv`, körde sedan acitvate för att aktivera miljön 
- Steg2: Installerade "behave" med `pip install behave`
- Steg3: Skapade gherkin fil-strukturen enligt föreläsningsanteckningarna.
  daniel@5CD1460TCQ:/mnt/c/Users/dawa01/Documents/Python Scripts/nbi/TAPHT24D_TT/Veckouppgift4$ tree
	.
	├── Readme.md
	└── Uppgift1
	    └── books_online
	        └── features
	            ├── shopping_cart.feature
	            └── steps
	                └── shopping_cart.steps.py

- Steg4: Skapade Featuren med filen `shopping_cart`.feature. Samt skrev scenarier på följande krav:
	- Användaren kan lägga böcker i en varukorg
	- Användaren kan ta bort böcker från varukorgen
	- Varukorgen visar alltid aktuell summa och antal böcker
	- Om användaren försöker lägga en bok som redan finns i varukorgen ska antalet av just den boken öka istället för att Skapa en ny rad
	- Det skall gå att tömma varukorgen helt
- Steg5: Skapade filen `shopping_cart.steps.py` för att programmera stegen i python och bahave.
- Steg6: Körde behave engång utan att skriva någon kod, behave kommer då att skriva ut exempel på alla stegen i python. Vilket gör att man kan ta och kopiera detta och använda för att börja implementationen.
- Steg7: Började med de stegen som inte var i "Outline" format vilket gjorde det lättare att förstå hur behave fungerade. 
	 - Detta gjordes med att tagga det scenariet som man höll på med med taggen `@wip`. 
	 - För att köra scenariet användes kommandot `behave -t wip` (fungerade inte att köra med @-tecknet i powershell)
 - Steg8: Efter att implementerat grund funktionerna för testet så implementerades Outline scenariona.
 
## Reflektioner (Vad som var lätt och svårt)
Det är lätt att se på när man ser på en film hur man gör men att göra det själv är svårare.
Man börjar att fundera på definitioner på Given, When, Then och vad koden skall placeras.

Konceptet "context" är också svårt att ta in vad är fördelen att använda metoden till om man inte behöver den i vissa lägen.

En svårighet som jag också funderade på är att det är lätt att förstöra testet genom att man ändrar en felstavning i gherkin och detta gör då att tillhörande steg inte blir utfört.

Använde mig av python log funktion för att veta vad som gick fel i testet. Tyckte inte behave skrev ut så mycket i terminalen så var en del gånger svårt att att felsöka.

## Kod
[Gherkin - shopping_cart.featue](./Uppgift1/books_online/features/shopping_cart.feature)  
[Behave steps - shopping_cart.steps.py](./Uppgift1/books_online/features/steps/shopping_cart.steps.py)

## Test resultat
```shell
(.venv) PS C:\Users\dawa01\Documents\Python Scripts\nbi\TAPHT24D_TT\Veckouppgift4\Uppgift1\books_online> behave
Feature: Varor i varukorgen # features/shopping_cart.feature:1
  Som en kund vill jag kunna lägga varor i en varukorg och se produkt pris, antal samt total kostnad.
  Scenario Outline: Användaren lägger böcker i varukorgen -- @1.1                               # features/shopping_cart.feature:11
    Given användaren befinner på sidan med böcker                                               # features/steps/shopping_cart.steps.py:69
    When när användaren trycker på knappen "lägg i varukorg" för bok "bok1" med priset "100"    # features/steps/shopping_cart.steps.py:74
    Then skall varukorgen innehålla böckerna "bok1" och ange antal "1" samt aktuellt pris "100" # features/steps/shopping_cart.steps.py:81

  Scenario Outline: Användaren lägger böcker i varukorgen -- @1.2                                     # features/shopping_cart.feature:12
    Given användaren befinner på sidan med böcker                                                     # features/steps/shopping_cart.steps.py:69
    When när användaren trycker på knappen "lägg i varukorg" för bok "bok2" med priset "200"          # features/steps/shopping_cart.steps.py:74
    Then skall varukorgen innehålla böckerna "bok1, bok2" och ange antal "2" samt aktuellt pris "300" # features/steps/shopping_cart.steps.py:81

  Scenario Outline: Användaren lägger böcker i varukorgen -- @1.3                                           # features/shopping_cart.feature:13
    Given användaren befinner på sidan med böcker                                                           # features/steps/shopping_cart.steps.py:69
    When när användaren trycker på knappen "lägg i varukorg" för bok "bok3" med priset "300"                # features/steps/shopping_cart.steps.py:74
    Then skall varukorgen innehålla böckerna "bok1, bok2, bok3" och ange antal "3" samt aktuellt pris "600" # features/steps/shopping_cart.steps.py:81

  Scenario Outline: Användaren tar bort böcker från varukorg -- @1.1           # features/shopping_cart.feature:24
    Given användaren befinner sig på varukorgsidan                             # features/steps/shopping_cart.steps.py:88
    And varukorgen innehåller "bok1"                                           # features/steps/shopping_cart.steps.py:93
    When användaren trycker på papperskorgen för "bok1"                        # features/steps/shopping_cart.steps.py:106
    Then boken skall tas bort från varukorgen och visa pris "0" samt antal "0" # features/steps/shopping_cart.steps.py:111

  Scenario Outline: Användaren tar bort böcker från varukorg -- @1.2             # features/shopping_cart.feature:25
    Given användaren befinner sig på varukorgsidan                               # features/steps/shopping_cart.steps.py:88
    And varukorgen innehåller "bok1, bok2"                                       # features/steps/shopping_cart.steps.py:93
    When användaren trycker på papperskorgen för "bok1"                          # features/steps/shopping_cart.steps.py:106
    Then boken skall tas bort från varukorgen och visa pris "200" samt antal "1" # features/steps/shopping_cart.steps.py:111

  Scenario Outline: Användaren tar bort böcker från varukorg -- @1.3             # features/shopping_cart.feature:26
    Given användaren befinner sig på varukorgsidan                               # features/steps/shopping_cart.steps.py:88
    And varukorgen innehåller "bok1, bok2, bok3"                                 # features/steps/shopping_cart.steps.py:93
    When användaren trycker på papperskorgen för "bok2"                          # features/steps/shopping_cart.steps.py:106
    Then boken skall tas bort från varukorgen och visa pris "400" samt antal "2" # features/steps/shopping_cart.steps.py:111

  Scenario: Användaren lägger till 2 likadana böcker i varukorgen                                   # features/shopping_cart.feature:29
    Given användaren befinner på sidan med böcker                                                   # features/steps/shopping_cart.steps.py:69
    When när användaren trycker på knappen "lägg i varukorg" för boken "Ubuntu som Server" 2 gånger # features/steps/shopping_cart.steps.py:117
    Then antalet av boken "Ubuntu som Server" skall vara 2 i varukorgen                             # features/steps/shopping_cart.steps.py:132

  Scenario Outline: Användaren tömmer varukorgen -- @1.1      # features/shopping_cart.feature:43
    Given användaren befinner sig på varukorgsidan            # features/steps/shopping_cart.steps.py:88
    And varukorgen innehåller "bok1, bok2, bok3"              # features/steps/shopping_cart.steps.py:93
    When användaren trycker på "töm varukorg"                 # features/steps/shopping_cart.steps.py:136
    Then varukorgen skall vara tom och summan skall vara noll # features/steps/shopping_cart.steps.py:141

1 feature passed, 0 failed, 0 skipped
8 scenarios passed, 0 failed, 0 skipped
28 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.008s
```