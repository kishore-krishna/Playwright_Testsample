from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1. Launch Microsoft Edge (channel="msedge" forces it to use Edge)
    # headless=False means you will physically see the browser window open
    browser = p.chromium.launch(channel="msedge", headless=False)
    
    # 2. Open a new browser tab
    page = browser.new_page()
    
    # 3. Go to Google
    page.goto("https://www.google.com")
    
    # 4. Fetch the page title
    edge_title = page.title()
    
    # 5. Print it to the console
    print("\n" + "="*30)
    print(f"Edge Page Title: {edge_title}")
    print("="*30 + "\n")
    
    # 6. Clean up and close the browser
    browser.close()