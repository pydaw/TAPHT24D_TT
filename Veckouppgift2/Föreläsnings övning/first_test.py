import re
from playwright.sync_api import Page, expect

def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()
    
    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()
