import pytest
import os
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context(request):
    # Start Playwright and launch Chrome with video recording enabled
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)  # Use 'chrome' instead of Chromium
        video_dir = Path("../reports")
        video_dir.mkdir(parents=True, exist_ok=True)  # Ensure the video directory exists

        context = browser.new_context(
            record_video_dir=str(video_dir),
            record_video_size={"width": 1280, "height": 720}  # Optional: specify video size
        )
        
        page = context.new_page()  # Open a page to ensure the context.pages is not empty
        yield page  # Yield the page to the test instead of context

        # Close the page (video recording will stop automatically)

        # Get the video path and rename it after test execution
        if page.video:
            video_path = page.video.path()  # Get the video path from the page, not context
            timestamp = datetime.now().strftime("%m%d_%H%M")  # Generate timestamp (e.g., 20240907_151230)
            new_video_name = f"{timestamp}.webm"  # Name based on test function name + timestamp
            new_video_path = video_dir / new_video_name
            os.rename(video_path, new_video_path)

        page.close()
        context.close()
        browser.close()

def test_google_title(browser_context):
    page = browser_context

    # Go to Google
    page.goto("https://www.google.com")

    # Assert that the title is correct
    assert page.title() == "Google", f"Expected title to be 'Google', but got {page.title()}"

    # Page is closed after the test in the fixture


def test_google_title1(browser_context):
    page = browser_context

    # Go to Google
    page.goto("https://www.google.com")

    # Assert that the title is correct
    assert page.title() == "Goole", f"Expected title to be 'Google', but got {page.title()}"

    # Page is closed after the test in the fixture
