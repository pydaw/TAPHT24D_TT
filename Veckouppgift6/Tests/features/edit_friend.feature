# US1.1 - Som en användare vill jag kunna ändra uppgifterna för en vän, så att jag kan hålla listan uppdaterad.
# US1.1.1 - Som en användare vill jag få ett meddelande om jag inte fyllt i båda fälten i formuläret, så att jag inte glömmer att fylla i all data för kontakten.

Feature: Ändra en väns uppgifter
    
    Scenario: Ändra en väns namn
        Given användaren befinner sig på vyn för att ändra en vän
        When spara namnet "batman"
        Then kontrollera att ändrad kontaktuppgift finns i listan
   
    Scenario: Ändra en väns epost
        Given användaren befinner sig på vyn för att ändra en vän
        When spara epost "batman@cave.nu"
        Then kontrollera att ändrad kontaktuppgift finns i listan
   
    Scenario: Fyller inte i namnet fältet på formuläret
        Given användaren befinner sig på vyn för att ändra en vän
        When spara namnet ""
        Then kontrollera att felmeddelande fås
   
    Scenario: Fyller inte i epost fältet på formuläret
        Given användaren befinner sig på vyn för att ändra en vän
        When spara epost ""
        Then kontrollera att felmeddelande fås
