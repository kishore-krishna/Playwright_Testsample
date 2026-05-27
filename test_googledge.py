def test_google_title(page):
    # 1. Navigate to Google
    page.goto("https://www.google.com")
    
    # 2. Verify the page title is exactly "Google"
    # Playwright's built-in assertion automatically handles waits
    assert page.title() == "Google"