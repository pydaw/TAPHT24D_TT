# US2 - Som en användare vill jag kunna lägga till nya vänner, så att jag kan spara nya kontakter.
# US2.1 - Som en användare vill jag få ett meddelande om jag inte fyllt i båda fälten i formuläret, så att jag inte glömmer att fylla i all data för kontakten.


Feature: Lägg till vän i listan
    
    Scenario: Lägga till en vän med både namn och e-post
        Given användaren befinner sig på vyn för att lägga till en vän
        When sparar vän "My Friend" med epost "my@friend.se"
        Then kontrollera att ny kontaktuppgift finns i listan


    Scenario: Visa felmeddelande om namn saknas
        Given användaren befinner sig på vyn för att lägga till en vän
        When sparar vän "" med epost "my@friend.se"
        Then användaren får ett meddelande att alla fälte inte är ifyllda


    Scenario: Visa felmeddelande om e-post saknas
        Given användaren befinner sig på vyn för att lägga till en vän
        When sparar vän "My Friend" med epost ""
        Then användaren får ett meddelande att alla fälte inte är ifyllda
