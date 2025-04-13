# US1 - Som en användare vill jag kunna se en lista med alla vänner, så att jag har alla kontaktuppgifter samlade.

Feature: Visa alla vänner
  För att kunna se vilka vänner jag har

  Scenario: Användaren ser listan med alla vänner
    Given användaren befinner sig på sidan med vänlistan
    When användaren tittar på listan
    Then användaren ser en lista med 5 vänner
