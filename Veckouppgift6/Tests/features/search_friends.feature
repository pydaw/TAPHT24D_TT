# US1.2 - Som en användare vill jag kunna radera en vän från listan, så att man kan hålla listan med vänner uppdaterad med de närvarande vännerna.
# US1.3 - Som en användare vill jag kunna söka efter en vän och kunna hitta vännen oberoende om jag använder stora eller små bokstäver, så att jag vet att jag inte missar min vän i sökningen.

Feature: Söka efter vänner
    Söka efter vänner (både namn och e-post)

    Scenario Outline: Söka efter en vän med
        Given användaren befinner sig på sidan med vänlistan
        When skriver in <search> i sökfältet
        Then skall listan visa <antal> matchningar

    Examples:
        | sökning                       | antal |
        | Jean-Luc                      | 1     |
        | commander.riker@starfleet.com | 1     |


    Scenario Outline: Söka efter en vän med
        Given användaren befinner sig på sidan med vänlistan
        When skriver in <search> med gemener i sökfältet
        Then skall listan visa <antal> matchningar

    Examples:
        | sökning                       | antal |
        | jean-luc                      | 1     |
        | commander.riker@starfleet.com | 1     |


    Scenario Outline: Söka efter en vän med
        Given användaren befinner sig på sidan med vänlistan
        When skriver in <search> med versaler i sökfältet
        Then skall listan visa <antal> matchningar

    Examples:
        | sökning                       | antal |
        | JEAN-LUC                      | 1     |
        | COMMANDER.RIKER@STARFLEET.COM | 1     |

    