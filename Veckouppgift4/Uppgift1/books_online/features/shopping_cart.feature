Feature: Varor i varukorgen
    Som en kund vill jag kunna lägga varor i en varukorg och se produkt pris, antal samt total kostnad.

    Scenario Outline: Användaren lägger böcker i varukorgen
        Given användaren befinner på sidan med böcker
        When när användaren trycker på knappen "lägg i varukorg" för bok "<book>" med priset "<price>"
        Then skall varukorgen innehålla böckerna "<books>" och ange antal "<number_of_books>" samt aktuellt pris "<total_price>" 

        Examples:
            | book  | price | books             | number_of_books | total_price | 
            | bok1  | 100   | bok1              | 1               | 100         |
            | bok2  | 200   | bok1, bok2        | 2               | 300         |
            | bok3  | 300   | bok1, bok2, bok3  | 3               | 600         |
    

    Scenario Outline: Användaren tar bort böcker från varukorg
        Given användaren befinner sig på varukorgsidan
        And varukorgen innehåller "<books>"
        When användaren trycker på papperskorgen för "<book>"
        Then boken skall tas bort från varukorgen och visa pris "<total_price>" samt antal "<number_of_books>"

        Examples:
            | books             | book    | prices   | number_of_books | total_price | 
            | bok1              | bok1    | 100      | 0               | 0           |
            | bok1, bok2        | bok1    | 200      | 1               | 200         |
            | bok1, bok2, bok3  | bok2    | 100, 300 | 2               | 400         |


    Scenario: Användaren lägger till 2 likadana böcker i varukorgen
        Given användaren befinner på sidan med böcker
        When när användaren trycker på knappen "lägg i varukorg" för boken "Ubuntu som Server" 2 gånger
        Then antalet av boken "Ubuntu som Server" skall vara 2 i varukorgen
    

    Scenario Outline: Användaren tömmer varukorgen
        Given användaren befinner sig på varukorgsidan
        And varukorgen innehåller "<books>"
        When användaren trycker på "töm varukorg"
        Then varukorgen skall vara tom och summan skall vara noll

        Examples:
            | books            |
            | bok1, bok2, bok3 |
      