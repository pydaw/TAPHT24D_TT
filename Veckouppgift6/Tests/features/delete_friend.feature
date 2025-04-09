# US1.2 - Som en användare vill jag kunna radera en vän från listan, så att man kan hålla listan med vänner uppdaterad med de närvarande vännerna.

Feature: Ta bort vän
    
    Scenario: Ta bort en vän och kontrollera att den inte finns i listan
        Given användaren befinner sig på sidan med vänlistan
        And namn "Spock" är med i listan
        When trycker på på "Ta bort" för namn
        Then ska inte namnet finnas kvar i listan
