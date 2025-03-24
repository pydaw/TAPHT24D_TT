import re
import pytest
import logging
from playwright.sync_api import Page, expect

import time

url = "https://lejonmanen.github.io/timer-vue/"


@pytest.fixture(scope="function",autouse=True)
def goto_url(page:Page):
    page.goto(url)
    page.set_default_timeout(timeout=3000)
    expect(page).to_have_title("Timer app")
    
class TestTimer:
    def test_add_timer(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        timer = page.locator(".widget").last
        timer_time = timer.locator(".row.time").get_by_text(re.compile("15:00"))
        expect(timer_time).to_be_visible()


    def test_start_timer(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        timer = page.locator(".widget").last
        start_button = timer.get_by_role("button").get_by_text("Start")
        
        # Save start time
        timer_start_time = timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}")).text_content()
        logging.info(f"Start time: {timer_start_time}")
        
        start_button.click()
        time.sleep(1)
        
        # Save time after wait
        timer_present_time= timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}")).text_content()
        logging.info(f"Present time: {timer_present_time}")
        

        # Check that timer is counting down
        start_time_minutes, start_time_seconds = timer_start_time.split(":")
        present_time_minutes, present_time_seconds = timer_present_time.split(":")
        assert(int(start_time_minutes) > int(present_time_minutes))
        assert(int(start_time_seconds) < int(present_time_seconds))
        

    def test_pause_timer(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        timer = page.locator(".widget").last
        timer.get_by_role("button").get_by_text("Start").click()
        time.sleep(1)
        
        # Pause
        timer.get_by_role("button").get_by_text("Pause").click()
        
        # Save pause time
        timer_pause_time = timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}")).text_content()
        logging.info(f"Pause time: {timer_pause_time}")
        time.sleep(1)

        # Save time after wait
        timer_present_time = timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}")).text_content()
        logging.info(f"Present time: {timer_present_time}")

        # Check that timer is not counting down
        pause_time_minutes, pause_time_seconds = timer_pause_time.split(":")
        present_time_minutes, present_time_seconds = timer_present_time.split(":")
        assert(int(pause_time_minutes) == int(present_time_minutes))
        assert(int(pause_time_seconds) == int(present_time_seconds))


    def test_reset_timer(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        timer = page.locator(".widget").last
        
        # Save start time
        timer.get_by_role("button").get_by_text("Start").click()
        time.sleep(1)
        
        # Save time
        timer_time = timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}")).text_content()
        logging.info(f"Time: {timer_time}")
        
        # Reset
        timer.get_by_role("button").get_by_text("Reset").click()
        
        # Save reset time
        timer_reset_time = timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}")).text_content()
        logging.info(f"Reset time: {timer_reset_time}")

        # Check that timer is not counting down
        time_minutes, time_seconds = timer_time.split(":")
        reset_time_minutes, reset_time_seconds = timer_reset_time.split(":")
        assert(int(time_minutes) < int(reset_time_minutes))
        assert(int(time_seconds) > int(reset_time_seconds))
        assert(timer_reset_time == "15:00")
    

    def test_remove_timer(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        timer = page.locator(".widget").last
        timer_time = timer.locator(".row.time").get_by_text(re.compile("15:00"))
        expect(timer_time).to_be_visible()

        widgets = page.locator(".widget")
        number_of_widgets = widgets.count()
        logging.info(f"Number of widget when timer is added: {number_of_widgets}")

        timer.locator(".icon.close").click()
        timer_time = timer.locator(".row.time").get_by_text(re.compile("15:00"))
        
        widgets = page.locator(".widget")
        number_of_widgets_after_timer_delete = widgets.count()
        logging.info(f"Number of widget when timer is removed: {number_of_widgets_after_timer_delete}")

        assert(number_of_widgets_after_timer_delete == number_of_widgets - 1)


    def test_adjust_time(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        timer = page.locator(".widget").last
        timer_time = timer.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}"))
        expect(timer_time).to_contain_text(re.compile("15:00"))

        timer.locator(".icon.settings").click()
        timer.locator(".settings-menu").locator("input").fill("11")
        timer.locator(".icon.settings").click()
        
        timer.get_by_role("button").get_by_text("Reset").click()
        expect(timer_time).to_contain_text(re.compile("11:00"))


class TestNote:
    def test_add_note(self, page:Page):
        page.get_by_role("button").get_by_text("Add note").click()
        note = page.locator(".widget").last
        note_textbox = note.locator(".note").get_by_text(re.compile("change text"))
        expect(note_textbox).to_contain_text("Click to change text")

    
    def test_remove_note(self, page:Page):
        page.get_by_role("button").get_by_text("Add note").click()
        note = page.locator(".widget").last
        note_textbox = note.locator(".note").get_by_text(re.compile("change text"))
        expect(note_textbox).to_be_visible()

        widgets = page.locator(".widget")
        number_of_widgets = widgets.count()
        logging.info(f"Number of widget when note is added: {number_of_widgets}")

        note.locator(".icon.close").click()
        
        widgets = page.locator(".widget")
        number_of_widgets_after_note_delete = widgets.count()
        logging.info(f"Number of widget when note is removed: {number_of_widgets_after_note_delete}")

        assert(number_of_widgets_after_note_delete < number_of_widgets)


    def test_change_note(self, page:Page):
        page.get_by_role("button").get_by_text("Add note").click()
        note = page.locator(".widget").last
        note_text = note.locator("h3")
        expect(note_text).to_contain_text("change text")
        
        note_text.click()
        
        note_input = note.get_by_placeholder("Description")
        test_text = "Test change note text"
        note_input.fill(test_text)
        note_text.press("Enter")
        expect(note_text).to_have_text(test_text)


class TestOther:
    def test_adjust_positon_of_widget(self, page:Page):
        page.get_by_role("button").get_by_text("Add timer").click()
        page.get_by_role("button").get_by_text("Add note").click()
        
        last_item = page.locator(".widget").last
        
        note_textbox = last_item.locator(".note").get_by_text(re.compile("change text"))
        expect(note_textbox).to_be_visible()
        
        last_item.locator(".icon.up").click()
        
        timer_time = last_item.locator(".row.time").get_by_text(re.compile(r"\d{2}:\d{2}"))
        expect(timer_time).to_be_visible()
        
        last_item.locator(".icon.up").click()
        
        note_textbox = last_item.locator(".note").get_by_text(re.compile("change text"))
        expect(note_textbox).to_be_visible()
    

    def test_change_theme(self, page:Page):
        theme = page.locator("xpath=/html").get_attribute("data-theme")
        logging.info(f"Theme: {theme}")
        assert theme == "null"

        page.get_by_role("button").get_by_text("Dark").click()
        theme = page.locator("xpath=/html").get_attribute("data-theme")
        assert theme == "dark"
        logging.info(f"Theme: {theme}")
        
        page.get_by_role("button").get_by_text("Forest").click()
        theme = page.locator("xpath=/html").get_attribute("data-theme")
        assert theme == "forest"
        logging.info(f"Theme: {theme}")
        
        page.get_by_role("button").get_by_text("Orange").click()
        theme = page.locator("xpath=/html").get_attribute("data-theme")
        assert theme == "orange"
        logging.info(f"Theme: {theme}")
        
        page.get_by_role("button").get_by_text("Light").click()
        theme = page.locator("xpath=/html").get_attribute("data-theme")
        assert theme == ""
        logging.info(f"Theme: {theme}")


