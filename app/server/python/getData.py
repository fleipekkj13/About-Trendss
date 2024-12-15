import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from dotenv import load_dotenv
import os
import json
load_dotenv()

TWITTER_TREDS_URL = os.getenv('URL_TWITTER_TREDS')
SLEEP_SCROLL_TIME = .5
SLEEP_LOAD_TIME = 5

class GetData:
    def __init__(self):
        self.data: dict = {}
        self._setupBrowser()
        JSON_DATA = self.get_twitter_data()
        print(json.dumps(JSON_DATA))


    def _setupBrowser(self):
        FIREFOX_PROFILE_URL = os.getenv('FIREFOX_PROFILE_PATH')
        GECKODRIVER_PATH = os.getenv('GECKODRIVER_PATH')

        self.options = Options()
        self.options.add_argument('-profile')
        self.options.add_argument(FIREFOX_PROFILE_URL)
        self.service = Service(GECKODRIVER_PATH)
        self.driver = Firefox(service=self.service, options=self.options)

    
    def _scroll_window(self, x:int ,y: int, twice: bool):
        self.driver.execute_script(f'window.scroll({x}, {y})')
        sleep(SLEEP_SCROLL_TIME)
        if twice:
            self.driver.execute_script('window.scroll(0,0)')

    

    def _getTreds(self) -> list:
        TREDS_XPATH = os.getenv('GET_TREDS_XPATH')
        return self.driver.find_elements(By.XPATH, TREDS_XPATH)
    

    def get_twitter_data(self):
        self.driver.get(TWITTER_TREDS_URL) #Entra no Twitter na aba treds
        sleep(SLEEP_LOAD_TIME)
        self._scroll_window(0,10000, True)
        TREDS = self._getTreds() #Coleta todas as treds

        index = 0
        for tred in TREDS:
            self.data[index] = [] #Start the DICT
            
            split_tred = tred.text.split('\n')
            
            self.data[index].append(f'Position: {split_tred[0]}')
            self.data[index].append(f'Title: {split_tred[3]}')
            self.data[index].append(f'Total Posts: {split_tred[-1]}')

            index += 1
        
        self.driver.quit()

        return self.data

d = GetData()