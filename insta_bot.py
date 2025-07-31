from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from brain import ask_brain



# Login and open DMs
def login_to_instagram(username, password):
    try:
         # Setup Chrome options first
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless=new")  # Enable new headless mode
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Start browser while searching
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        # Navigate to Instagram
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        # Login
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        return driver
    except Exception as e:
        print(f"⚠️ Error during login: {e}")
        try:
            driver.quit()
        except:
            pass
        return None


def check_and_reply(driver):
    try:
        driver.get("https://www.instagram.com/direct/inbox/")
        time.sleep(2)

        messages = driver.find_elements(By.XPATH, "//span[contains(text(), 'Q:')]")
        if not messages:
            print("No new messages starting with 'Q:' found.")
            time.sleep(1)
            return

        for msg in messages:
            try:
                question = msg.text.replace("Q:", "").strip()
                # Check for specific questions and provide predefined answers
                if question.lower() == "who are you":
                    answer = "I'm Igris develop by Ayush rana taking info from chatgpt database"
                else:
                    # If not a specific question, ask the brain
                    answer = ask_brain(question)
               
                msg.click()
                time.sleep(2)

                # Wait for the message input field to be clickable
                wait = WebDriverWait(driver, 10)
                # Locate the message input field using role='textbox'
                message_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox' and @aria-label='Message']")))
                # Send the answer using send_keys
                message_input.send_keys(answer)
                # Press Enter to send the message
                message_input.send_keys(Keys.RETURN)
                
                time.sleep(2)
                # After sending the message, navigate back to the inbox list
                driver.get("https://www.instagram.com/direct/inbox/")
                time.sleep(1)

            except Exception as e:
                print(f"⚠️ Error processing message: {e}")
                # If there's an error with a specific message, log it and continue to the next message
                # Also navigate back to the inbox list in case of error
                try:
                    driver.get("https://www.instagram.com/direct/inbox/")
                    time.sleep(2)
                except:
                    pass
                continue # Continue to the next message in the loop

    except Exception as e:
        print(f"⚠️ Error in check_and_reply: {e}")
        # If a general error occurs while checking inbox, the outer loop will handle retries
        # No need to return False here, as the outer loop doesn't depend on it for re-login
    

# Example use
if __name__ == "__main__":
    # Attempt to log in once at the beginning
    print("Attempting to log in...")
    driver = login_to_instagram("username", "password")

    # Check if login was successful
    if driver is None:
        print("Failed to log in. Exiting program.")
        exit() # Exit if login fails

    print("Login successful. Starting continuous message check.")

    # Continuous loop to check for messages
    while True:
        print("Checking for new messages...")
        # Call check_and_reply. Errors during message processing are handled inside the function.
        check_and_reply(driver)

        # Wait before the next check cycle
        print("Check cycle complete. Waiting 30 seconds before next check.")
        time.sleep(10)

