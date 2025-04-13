# Veckouppgift 6
Skall göra tester med behave och playwright på sidan: https://forverkliga.se/JavaScript/my-contacts/#/

Följer flödet:
``` mermaid
flowchart TD
    A[Requirement] --> B(User Storys) --> C(Features) --> D(Scenarios) --> E(Steps) --> A
```


## Userstories

| Krav/Nuvarande funktion                                               | User Story                                                                                                                                                                                                           |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 Visa lista med alla vänner                                          | US1 - Som en användare vill jag kunna se en lista med alla vänner, så att jag har alla kontaktuppgifter samlade.                                                                                                     |
| 1.1 Ändra uppgifter för en vän                                        | US1.1 - Som en användare vill jag kunna ändra uppgifterna för en vän, så att jag kan hålla listan uppdaterad.                                                                                                        |
| 1.1.1 Formuläret visar ett felmeddelande om båda fälten är ifyllda    | US1.1.1 - Som en användare vill jag få ett meddelande om jag inte fyllt i båda fälten i formuläret, så att jag inte glömmer att fylla i all data för kontakten.                                                      |
| 1.2 Ta bort en vän                                                    | US1.2 - Som en användare vill jag kunna radera en vän från listan, så att man kan hålla listan med vänner uppdaterad med de närvarande vännerna.                                                                     |
| 1.3 Söka baserat på namn, oberoende av stora eller små bokstäver      | US1.3 - Som en användare vill jag kunna söka efter en vän och kunna hitta vännen oberoende om jag använder stora eller små bokstäver, så att jag vet att jag inte missar min vän i sökningen.                        |
| 1.4 Söka baserat på e-post, oberoende av stora eller små bokstäver    | US1.4 - Som en användare vill jag kunna söka efter en vän genom en e-post adress och kunna hitta vännen oberoende om jag använder stora eller små bokstäver, så att jag vet att jag inte missar min vän i sökningen. |
| 2 Lägga till ny vän                                                   | US2 - Som en användare vill jag kunna lägga till nya vänner, så att jag kan spara nya kontakter.                                                                                                                     |
| 2.1 Formuläret visar ett felmeddelande om inte båda fälten är ifyllda | US2.1- Som en användare vill jag få ett meddelande om jag inte fyllt i båda fälten i formuläret, så att jag inte glömmer att fylla i all data för kontakten.                                                         |


## Tester
[Visa lista med vänner](tests/features/view_friends.feature)  
[Söka efter vänner](tests/features/search_friends.feature)  
[Ändra uppgifter på vän](tests/features/edit_friend.feature)  
[Ta bort vän](tests/features/delete_friend.feature)  
[Lägga till vän](tests/features/add_friend.feature)  

## Test resultat
``` log
(.venv) PS C:\Users\<user>\Documents\Python Scripts\nbi\TAPHT24D_TT\Veckouppgift6\tests> behave                              
Feature: Lägg till vän i listan # features/add_friend.feature:5

  Scenario: Lägga till en vän med både namn och e-post             # features/add_friend.feature:7
    Given användaren befinner sig på vyn för att lägga till en vän # steps/add_friend.py:6
    When sparar vän "My Friend" med epost "my@friend.se"           # steps/add_friend.py:12
    Then kontrollera att ny kontaktuppgift finns i listan          # steps/add_friend.py:22

  Scenario: Visa felmeddelande om namn saknas                         # features/add_friend.feature:13
    Given användaren befinner sig på vyn för att lägga till en vän    # steps/add_friend.py:6
    When sparar vän "" med epost "my@friend.se"                       # steps/add_friend.py:32
    Then användaren får ett meddelande att alla fälte inte är ifyllda # steps/add_friend.py:50

  Scenario: Visa felmeddelande om e-post saknas                       # features/add_friend.feature:19
    Given användaren befinner sig på vyn för att lägga till en vän    # steps/add_friend.py:6
    When sparar vän "My Friend" med epost ""                          # steps/add_friend.py:41
    Then användaren får ett meddelande att alla fälte inte är ifyllda # steps/add_friend.py:50

Feature: Ta bort vän # features/delete_friend.feature:3

  Scenario: Ta bort en vän och kontrollera att den inte finns i listan  # features/delete_friend.feature:5
    Given användaren befinner sig på sidan med vänlistan                # steps/view_friends.py:5
    And namn "Spock" är med i listan                                    # steps/delete_friends.py:5
    When trycker på på "Ta bort" för namn                               # steps/delete_friends.py:12
    Then ska inte namnet finnas kvar i listan                           # steps/delete_friends.py:17

Feature: Ändra en väns uppgifter # features/edit_friend.feature:4

  Scenario: Ändra en väns namn                                # features/edit_friend.feature:6
    Given användaren befinner sig på vyn för att ändra en vän # steps/edit_friend.py:6
    When spara namnet "batman"                                # steps/edit_friend.py:13
    Then kontrollera att ändrad kontaktuppgift finns i listan # steps/edit_friend.py:31

  Scenario: Ändra en väns epost                               # features/edit_friend.feature:11
    Given användaren befinner sig på vyn för att ändra en vän # steps/edit_friend.py:6
    When spara epost "batman@cave.nu"                         # steps/edit_friend.py:22
    Then kontrollera att ändrad kontaktuppgift finns i listan # steps/edit_friend.py:31

  Scenario: Fyller inte i namnet fältet på formuläret         # features/edit_friend.feature:16
    Given användaren befinner sig på vyn för att ändra en vän # steps/edit_friend.py:6
    When spara namnet ""                                      # steps/edit_friend.py:44
    Then kontrollera att felmeddelande fås                    # steps/edit_friend.py:58

  Scenario: Fyller inte i epost fältet på formuläret          # features/edit_friend.feature:21
    Given användaren befinner sig på vyn för att ändra en vän # steps/edit_friend.py:6
    When spara epost ""                                       # steps/edit_friend.py:51
    Then kontrollera att felmeddelande fås                    # steps/edit_friend.py:58

Feature: Söka efter vänner # features/search_friends.feature:4
  Söka efter vänner (både namn och e-post)
  Scenario Outline: Söka efter en vän med -- @1.1        # features/search_friends.feature:14
    Given användaren befinner sig på sidan med vänlistan # steps/view_friends.py:5
    When skriver in "Jean-Luc" i sökfältet               # steps/search_friends.py:20
    Then skall listan visa "1" matchningar               # steps/search_friends.py:41

  Scenario Outline: Söka efter en vän med -- @1.2               # features/search_friends.feature:15
    Given användaren befinner sig på sidan med vänlistan        # steps/view_friends.py:5
    When skriver in "commander.riker@starfleet.com" i sökfältet # steps/search_friends.py:20
    Then skall listan visa "1" matchningar                      # steps/search_friends.py:41

  Scenario Outline: Söka efter en vän med -- @1.1        # features/search_friends.feature:25
    Given användaren befinner sig på sidan med vänlistan # steps/view_friends.py:5
    When skriver in "jean-luc" med gemener i sökfältet   # steps/search_friends.py:27
    Then skall listan visa "1" matchningar               # steps/search_friends.py:41

  Scenario Outline: Söka efter en vän med -- @1.2                           # features/search_friends.feature:26
    Given användaren befinner sig på sidan med vänlistan                    # steps/view_friends.py:5
    When skriver in "commander.riker@starfleet.com" med gemener i sökfältet # steps/search_friends.py:27
    Then skall listan visa "1" matchningar                                  # steps/search_friends.py:41

  Scenario Outline: Söka efter en vän med -- @1.1        # features/search_friends.feature:36
    Given användaren befinner sig på sidan med vänlistan # steps/view_friends.py:5
    When skriver in "JEAN-LUC" med versaler i sökfältet  # steps/search_friends.py:34
    Then skall listan visa "1" matchningar               # steps/search_friends.py:41

  Scenario Outline: Söka efter en vän med -- @1.2                            # features/search_friends.feature:37
    Given användaren befinner sig på sidan med vänlistan                     # steps/view_friends.py:5
    When skriver in "COMMANDER.RIKER@STARFLEET.COM" med versaler i sökfältet # steps/search_friends.py:34
    Then skall listan visa "1" matchningar                                   # steps/search_friends.py:41

Feature: Visa alla vänner # features/view_friends.feature:3
  För att kunna se vilka vänner jag har
  Scenario: Användaren ser listan med alla vänner        # features/view_friends.feature:6
    Given användaren befinner sig på sidan med vänlistan # steps/view_friends.py:5
    When användaren tittar på listan                     # steps/view_friends.py:10
    Then användaren ser en lista med 5 vänner            # steps/view_friends.py:15

5 features passed, 0 failed, 0 skipped
15 scenarios passed, 0 failed, 0 skipped
46 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m8.196s
```