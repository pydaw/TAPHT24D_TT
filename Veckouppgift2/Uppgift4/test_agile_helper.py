import pytest
import re
from playwright.sync_api import Page, expect

import time



def test_US1_first_open_sprint_planning(page: Page):
    """
    Story: Som en användare, vill jag se mötet "sprint planning" som 
    utspelar sig första dagen på en sprint, så att jag vet vad j
    ag ska göra på mötet.
    """

    # Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Sätter default timeout
    page.set_default_timeout(timeout=3000)

    # Klicka på knappen som innehåller texten "first"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click()

    # Klicka på knappen vars text innehåller "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()
    sp_button.click()

    # Kontrollera att ett `<dialog>` element visas på sidan, 
    # som innehåller en rubrik med texten "Sprint planning"
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

    # Klicka på knappen vars text innehåller "Ok we're done"
    done_button = page.get_by_role("button").get_by_text(re.compile("done"))
    expect(done_button).to_be_visible()
    done_button.click()


@pytest.mark.parametrize("button_text", ["first","middle","last"])
def test_US2_open_daily_standup(page: Page, button_text):
    """
    Som en användare, vill jag se mötet "daily stand up" som utspelar sig 
    varje dag under sprintens gång, så att jag vet vad jag ska göra på mötet.
    """

    # Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Sätter default timeout
    page.set_default_timeout(timeout=3000)

    # Klicka på knappen som innehåller texten i parameter button_text
    locator = page.get_by_role("button")
    parmeter_button = locator.get_by_text(re.compile(button_text, re.IGNORECASE))
    parmeter_button.click()

    # Klicka på knappen vars text innehåller "Daily standup"
    ds_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(ds_button).to_be_visible()
    ds_button.click()

    # Kontrollera att ett `<dialog>` element visas på sidan, 
    # som innehåller en rubrik med texten "Daily standup"
    ds_heading = page.get_by_role("heading").get_by_text("Daily standup")
    expect(ds_heading).to_be_visible()

    # Klicka på knappen vars text innehåller "Ok we're done"
    done_button = page.get_by_role("button").get_by_text(re.compile("done"))
    expect(done_button).to_be_visible()
    done_button.click()


@pytest.mark.parametrize("button_text", ["first","middle","last"])
def test_US3_start_daily_standup(page: Page, button_text):
    """
    Som en användare, vill jag under "daily stand up" kunna starta en timer, 
    så att jag vet att mötet kommer hållas kort.
    """

    # Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Sätter default timeout
    page.set_default_timeout(timeout=3000)

    # Klicka på knappen som innehåller texten i parameter button_text
    locator = page.get_by_role("button")
    parameter_button = locator.get_by_text(re.compile(button_text, re.IGNORECASE))
    parameter_button.click()

    # Klicka på knappen vars text innehåller "Daily standup"
    ds_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(ds_button).to_be_visible()
    ds_button.click()

    # Kontrollera att det finns ett `<span>` element med texten `--:--`
    ds_timer = page.get_by_text(re.compile("--:--"))
    expect(ds_timer).to_be_visible()

    # Spara parent av timer elementet
    ds_parent = ds_timer.locator('..')

    # Klicka på knappen vars text innehåller "Start the standup: 10minutes"
    start_button = page.get_by_role("button").get_by_text(re.compile("start the standup",re.IGNORECASE))
    expect(start_button).to_be_visible()
    start_button.click()

    # Vänta 0,1s
    time.sleep(0.1)

    # Kontrollera att `<span>` element innehåller texten `9:`
    ds_timer = page.get_by_text(re.compile(r"\d+:\d+"))
    expect(ds_timer).to_contain_text(re.compile("9:", re.IGNORECASE))


def test_US4_last_open_sprint_review(page: Page):
    """
    Som en användare, vill jag se vilket arbete som skall presenteras för 
    produkt ägaren under en "Sprint review" som utspelar sig sist under sprinten, 
    så att jag vet vad som skall presenteras.
    """

    # Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Sätter default timeout
    page.set_default_timeout(timeout=3000)

    # Klicka på knappen innehåller texten "Last"
    locator = page.get_by_role("button")
    last_button = locator.get_by_text("Last")
    last_button.click()

    # Klicka på knappen vars text innehåller "Sprint review"
    sr_button = page.get_by_role("button").get_by_text(re.compile("Sprint review"))
    expect(sr_button).to_be_visible()
    sr_button.click()

    # Kontrollera att ett `<dialog>` element visas på sidan, 
    # som innehåller en rubrik med texten "Sprint review"
    sr_heading = page.get_by_role("heading").get_by_text("Sprint review")
    expect(sr_heading).to_be_visible()

    # Klicka på knappen vars text innehåller "Ok we're done"
    done_button = page.get_by_role("button").get_by_text(re.compile("done"))
    expect(done_button).to_be_visible()
    done_button.click()


def test_US5_last_open_sprint_retrospective(page: Page):
    """
    Som en användare, vill jag se vad som skall göras under "Sprint retrospective" 
    som utspelar sig efter sprinten, så att jag vet vilka frågor som skall besvaras 
    samt se hur sprinten har gått och bli bättre till nästa sprint.
    """

    # Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Sätter default timeout
    page.set_default_timeout(timeout=3000)

    # Klicka på knappen innehåller texten "Last"
    locator = page.get_by_role("button")
    last_button = locator.get_by_text("Last")
    last_button.click()

    # Klicka på knappen vars text innehåller "Sprint retrospective"
    sr_button = page.get_by_role("button").get_by_text(re.compile("Sprint retrospective"))
    expect(sr_button).to_be_visible()
    sr_button.click()

    # Kontrollera att ett `<dialog>` element visas på sidan, 
    # som innehåller en rubrik med texten "Sprint retrospective"
    sr_heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(sr_heading).to_be_visible()

    # Klicka på knappen vars text innehåller "complete"
    complete_button = page.get_by_role("button").get_by_text(re.compile("complete"))
    expect(complete_button).to_be_visible()
    complete_button.click()

@pytest.mark.parametrize("button_text", ["first","middle","last"])
def test_US6_navigate_back_to_main_page(page: Page, button_text):
    """
    Som en användare, vill jag kunna komma kunna navigera tillbaka i menyerna, 
    så att jag vet att jag kan välja rätt meny om jag tycker fel.
    """

    # Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Sätter default timeout
    page.set_default_timeout(timeout=3000)

    # Klicka på knappen som innehåller texten i parameter button_text
    locator = page.get_by_role("button")
    parmeter_button = locator.get_by_text(re.compile(button_text, re.IGNORECASE))
    parmeter_button.click()

    # Klicka på knappen vars text innehåller "Start over"
    done_button = page.get_by_role("button").get_by_text(re.compile("start over", re.IGNORECASE))
    expect(done_button).to_be_visible()
    done_button.click()
