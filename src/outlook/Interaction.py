import random
import time
import os
from datetime import datetime

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from dotenv import load_dotenv

from .Utilities import print_info, \
    print_success, \
    print_error, \
    get_name, \
    get_lines


# load_dotenv()
class VotesGenerator:
    def __init__(self):
        self.driver = ""
        self.receiver_name = ""
        self.email = ""
        self.password = ""
        self.i = 0
        self.emails = ""

    def get_driver(self):
        print_info("getting the driver")
        # chrome_options.add_extension(path_to_extension)
        # self.driver = uc.Chrome()
        self.driver = webdriver.Firefox()
        return

    def go_to_signup(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        ".Button-sc-1dqy6lx-0.jjtmnk.sibxBMlr_oxWTfBrEz2G",
                    )
                )
            )
        finally:
            go_signup = self.driver.find_elements(
                By.CSS_SELECTOR, ".Button-sc-1dqy6lx-0.jjtmnk.sibxBMlr_oxWTfBrEz2G"
            )
            if len(go_signup) != 0:
                go_signup[0].click()

        return

    def remove_descrections(self):
        policy_close_button = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon",
        )
        if len(policy_close_button) != 0:
            policy_close_button[0].click()
            print("NOTE: REMOVED POLICY")

        try:
            cookies_button = self.driver.find_element(
                By.ID, "onetrust-accept-btn-handler"
            )
        except:
            print("NOTE: No cookies there")
        else:
            cookies_button.click()
            print("REMOVE COOKIES")

        return

    def fill_name(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="forminator-field-text-1"]',
                    )
                )
            )
        except Exception as e:
            print_error(e)
        else:
            name_field = self.driver.find_element(
                By.XPATH,'//*[@id="forminator-field-text-1"]'
            )
            self.receiver_name = get_name()
            name_field.clear()
            name_field.send_keys(self.receiver_name)
            print_success("field name is done")
        return

    def proxy(self, nexte = False):
        with open("./proxies", 'r') as F:
            proxies = F.readlines()
        return proxies[random.randint(0,len(proxies)-1)]
    def email_field(self, email=""):
        # user, _ = os.getenv("USER").split("@")
        # self.email = user + "+" + generate_random_string().lower() + "@gmail.com"
        # if not nexte:
        #     self.emails = get_lines("../data/emails")
        # self.email = next(self.emails, None)
        # print(self.email)
        self.email = email
        print(self.email)
        print("waiting for the email field")
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH, '//*[@id="root"]/section/section/div/div/div/div[2]/form/div[1]/div/div/span/span/input',
                    )
                )
            )
        except Exception as e:
            print_error(e)
        else:
            email_input = self.driver.find_element(By.XPATH, '//*[@id="root"]/section/section/div/div/div/div[2]/form/div[1]/div/div/span/span/input')
            email_input.clear()
            email_input.send_keys(self.email)
            print_success("email field done")
        return

    def password_field(self, password = ""):
        self.password = password
        print("Password:",self.password)
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="root"]/section/section/div/div/div/div[2]/form/div[2]/div/div/span/span/input',
                    )
                )
            )
        except Exception as e:
            print_error(e)
        else:
            email_input = self.driver.find_element(By.XPATH,
                                                   '//*[@id="root"]/section/section/div/div/div/div[2]/form/div[2]/div/div/span/span/input')
            email_input.clear()
            email_input.send_keys(self.password)
            print_success("password field done")
        return


    def wait_recptcha_to_be_solved_2(self):
        try:
            iframe = WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')
                )
            )
        except:
            print("ERROR: WE CANNOT SWITCH TO RECAPTCHA IFRAME")
        else:
            print("NOTE: PRESENCE OF RECAPTCHA")
            self.driver.switch_to.frame(iframe)
            print(f"WAITING FOR RECAPTCHA TO BE SOLVED...")
            try:
                WebDriverWait(self.driver, 55).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="recaptcha-anchor"][contains(@aria-checked, "true")]')
                    )
                )
            except Exception as err:
                print(err)
            else:
                print("NOTE: RECAPTCHA HAS BEEN SOLVED")
                self.driver.switch_to.default_content()
                self.remove_destraction()
                return True

    def wait_recptcha_to_be_solved(self):
        try:
            iframe = WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')
                )
            )
        except:
            print("ERROR: WE CANNOT SWITCH TO RECAPTCHA IFRAME")
        else:
            print("NOTE: PRESENCE OF RECAPTCHA")
            self.driver.switch_to.frame(iframe)
            print(f"WAITING FOR RECAPTCHA TO BE SOLVED...")
            for i in range(100):
                try:
                    recaptcha = self.driver.find_elements(By.CSS_SELECTOR, '#recaptcha-anchor[aria-checked="true"]')
                except:
                    print(f"WARNING: WAITING FOR RECAPTCHA TO BE SOLVED {100 - i}...")
                    time.sleep(5)
                else:
                    if len(recaptcha) != 0:
                        print("NOTE: RECAPTCHA HAS BEEN SOLVED")
                        self.driver.switch_to.default_content()
                        return True
                    else:
                        print(f"WARNING: WAITING FOR RECAPTCHA TO BE SOLVED {100 - i}...")
                        time.sleep(5)
            # self.driver.save_screenshot("screenshot.png")
            self.driver.switch_to.default_content()
            return False

    def submit_form(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="root"]/section/section/div/div/div/div[2]/form/button',
                    )
                )
            )
        except Exception as e:
            print_error(e)
        else:
            button = self.driver.find_element(By.XPATH,'//*[@id="root"]/section/section/div/div/div/div[2]/form/button')
            button.click()
            print_success("Button Clicked")
        return

    def close_tab(self):
        self.driver.quit()

    def main(self, driver = "", email="", password=""):
        try:
            if driver == "":
                self.get_driver()
            else:
                self.driver = driver
            self.driver.get("https://accounts.mathpix.com/signup")
            self.email_field(email=email)
            self.password_field(password=password)
            self.wait_recptcha_to_be_solved()
            self.submit_form()
            time.sleep(2)
            print("Find the verification link...")
            self.driver.get("https://outlook.live.com/mail/0/")
            try:
                WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH, '//*[@title="support@mathpix.com"]',
                        )
                    )
                )
            except Exception as e:
                print(e)
                print("we did not find a verif email")
            else:
                email_label = self.driver.find_element(By.XPATH, '//*[@title="support@mathpix.com"]')
                email_label.click()
                print("Email Clicked")
                time.sleep(3)
                try:
                    WebDriverWait(self.driver, 100).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH, '//*[@id="UniqueMessageBody"]/div/div/div/p[2]/a',
                            )
                        )
                    )
                except Exception as e:
                    print(e)
                    print("this error")
                else:
                    element = self.driver.find_element(By.XPATH,'//*[@id="UniqueMessageBody"]/div/div/div/p[2]/a')
                    href_value = element.get_attribute("href")
                    print(href_value)
                    self.driver.get(href_value)
                    print("saving account: " + str(email) + ":" + str(password))
                    with open("account.txt", 'a') as f:
                        f.write(str(email) + ":" + str(password) + ":" + str(datetime.now().strftime("%d-%m-%Y")))
                        f.write("\n")
                    print("account saved")
                    print("We have clicked on verification link")
                    time.sleep(3)
                    exit()

        except Exception as e:
            print(e)
            self.main()
        else:
            return



    # end of class

if __name__ == "__main__":
    current_date = datetime.now().strftime("%d-%m-%Y")
    print(current_date)
