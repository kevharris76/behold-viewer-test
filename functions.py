from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import namemap as NM
import pytest
import pytest_check as check

import time
import os
# from dotenv import load_dotenv, find_dotenv
import logging

# load_dotenv(find_dotenv())
# ADMIN_USER = os.getenv('ADMIN_USER')
# ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

log = logging.getLogger()

# web_url = r"https://alpha.app.behold.ai"
# # web_url = r"https://app.behold.ai"
# web_url_login = fr'{web_url}/auth/signin'


class Start_Web():
    def __init__(self):
        pass

    def start_chrome(self, url=None):
        # set incognito params
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--window-position=0,-1000")
        options.add_argument("--start-maximized")
        executable_path = ChromeService(r"C:\auto\tools\web_drivers\chromedriver.exe")


        '''use latest driver downloaded'''
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        '''use driver in specified location'''
        driver = webdriver.Chrome(service=executable_path, options=options)

        driver.get(url)
        driver.maximize_window()
        return driver


'''study list metadata'''
def login(driver=None, user=None, p_word=None):
    '''Login as user'''
    username = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.username_xpath)))
                #driver.find_element(by=By.CSS_SELECTOR, value=NM.username_xpath)
    username.send_keys(user)
    log.info(f"username used: \"{user}\"")
    password = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.password_xpath)))
    password.send_keys(p_word)
    log.info(f"password used: ***")
    submit = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.login_submit_xpath)))
    submit.click()
    log.info(f"submit clicked")
    sl_textbox = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.sl_filter_textbox)))

    if sl_textbox:
        log.info(f"Logged in as \"{user}\"")
    else:
        log.info(f"Failed to Login as \"{user}\"")
    actualUrl = driver.current_url
    return actualUrl


def load_worklist(driver=None, worklist=None):
    sl_filter_tb = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.sl_filter_textbox)))
    sl_filter_tb.send_keys(worklist)

    pending_list = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.active span span')))
    # log.info(pending_list.get_property("innerHTML"))
    pending_list.click()

    actual = str(pending_list.get_property("innerHTML")).upper().strip()
    log.info(f'The actual worklist: \"{actual}\"')
    log.info(f'The expected worklist: \"{worklist}\"')
    if check.equal(worklist, actual, f'does \"{worklist}\" match \"{actual}\"'):
        log.info(f"worklist loaded: \"{worklist}\"")


def load_by_accession(driver=None, accession=None):
    accession_number = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, NM.wl_accession_tb)))
    clear_accession(driver=driver)
    accession_number.send_keys(accession)
    time.sleep(2)
    accession_number.send_keys(Keys.ENTER)
    time.sleep(2)
    accession_number.send_keys(Keys.ENTER)
    time.sleep(5)

    load_image = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(7)')))
    actual = load_image.get_attribute("innerHTML")

    check.equal(accession, actual, log.info(f"checking that accession searched is filtered on \"{accession}\" == \"{actual}\""))
    load_image.click()
    # time.sleep(5)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.normalSelector)))


def get_image_text(driver=None, classname=None):
    details = driver.find_element(By.CLASS_NAME, classname)
    # log.info(f"{details}")

    title, value = details.find_elements(By.CSS_SELECTOR, "h5"), details.find_elements(By.CSS_SELECTOR, "p")
    keys, values = [], []
    for i in range(len(title)):
        keys.append(title[i].get_attribute("innerHTML"))
        values.append(value[i].get_attribute("innerHTML"))

    patient_details = zip(keys, values)
    patient_details = dict(patient_details)
    return patient_details

def get_table_cols_rows(driver=None):
    table_header_xpath = '//*[@id="application"]/div/div[2]/div/div/div/div[1]/div/div[2]/div[1]/table/thead/tr/th'
    col = driver.find_elements(By.XPATH, table_header_xpath)
    time.sleep(3)
    table = '//*[@id="application"]/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr'
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, table)))
    rows = driver.find_elements(By.XPATH, table)
    return len(col), len(rows)

def get_table_content(driver=None):
    # get study list table header and table contents
    time.sleep(2)
    sl_table_header = driver.find_element(By.CSS_SELECTOR, NM.sl_table_header)
    table_cols = sl_table_header.find_elements(By.CSS_SELECTOR, "th")
    log.info(len(table_cols))
    for i in range(len(table_cols)):
        log.info(f'{table_cols[i].text}')

    sl_table_content = driver.find_element(By.CSS_SELECTOR, NM.sl_table_content)
    key = sl_table_content.find_elements(By.CSS_SELECTOR, "td")
    log.info(len(key))
    for i in range(len(key)):
        log.info(f'{key[i].text}')

def clear_accession(driver=None):
    accession_number = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, NM.wl_accession_tb)))
    i=1
    while i < 30:
        accession_number.send_keys(Keys.BACKSPACE)
        i += 1
    accession_number.send_keys(Keys.ENTER)
    time.sleep(4)

def screengrab_image(driver=None,imageview=None, imagename=None):
    location = driver.find_element(By.CSS_SELECTOR, imageview)
    location.screenshot(imagename)

def draw_rectangle(driver=None, start_x=None, start_y=None, end_x=None, end_y=None):
    try:
        enabled = driver.find_element(By.XPATH, NM.rectangle_roi_enabled).is_displayed()
        log.info(f'rectangle button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x, end_y).release()
        action.perform()
        time.sleep(2)
    except:
        rectangle_roi = driver.find_element(By.ID, NM.rectangle_roi_id)
        rectangle_roi.click()
        enabled = driver.find_element(By.XPATH, NM.rectangle_roi_enabled).is_displayed()
        log.info(f'rectangle button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x, end_y).release()
        action.perform()
        time.sleep(2)

def draw_ellipse(driver=None, start_x=None, start_y=None, end_x=None, end_y=None):
    try:
        enabled = driver.find_element(By.XPATH, NM.ellipse_roi_enabled).is_displayed()
        log.info(f'ellipse button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x, end_y).release()
        action.perform()
        time.sleep(2)
    except:
        ellipse_roi = driver.find_element(By.ID, NM.ellipse_roi_id)
        ellipse_roi.click()
        enabled = driver.find_element(By.XPATH, NM.ellipse_roi_enabled).is_displayed()
        log.info(f'ellipse button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x, end_y).release()
        action.perform()
        time.sleep(2)

def draw_ruler(driver=None, start_x=None, start_y=None, end_x=None, end_y=None):
    try:
        enabled = driver.find_element(By.XPATH, NM.ruler_enabled).is_displayed()
        log.info(f'ruler button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x, end_y).release()
        action.perform()
        time.sleep(2)
    except:
        ruler_roi = driver.find_element(By.ID, NM.ruler_id)
        ruler_roi.click()
        enabled = driver.find_element(By.XPATH, NM.ruler_enabled).is_displayed()
        log.info(f'ruler button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x, end_y).release()
        action.perform()
        time.sleep(2)

def draw_point_probe(driver=None, start_x=None, start_y=None):
    try:
        enabled = driver.find_element(By.XPATH, NM.point_enabled).is_displayed()
        log.info(f'Point probe button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click()
        action.perform()
        time.sleep(2)
    except:
        point_probe = driver.find_element(By.ID, NM.point_id)
        point_probe.click()
        enabled = driver.find_element(By.XPATH, NM.point_enabled).is_displayed()
        log.info(f'Point probe button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click()
        action.perform()
        time.sleep(2)

def draw_angle(driver=None, start_x=None, start_y=None, end_x1=None, end_y1=None, end_x2=None, end_y2=None):
    try:
        enabled = driver.find_element(By.XPATH, NM.angle_enabled).is_displayed()
        log.info(f'ellipse button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click().move_by_offset(end_x1, end_y1).click()\
            .click().move_by_offset(end_x2, end_y2).click()
        action.perform()
        time.sleep(2)
    except:
        ellipse_roi = driver.find_element(By.ID, NM.angle_id)
        ellipse_roi.click()
        enabled = driver.find_element(By.XPATH, NM.angle_enabled).is_displayed()
        log.info(f'ellipse button is selected: {enabled}')
        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        # log.info(location.rect)
        action = ActionChains(driver)
        action.move_to_element(location).move_by_offset(start_x, start_y).click().move_by_offset(end_x1, end_y1).click()\
            .click().move_by_offset(end_x2, end_y2).click()
        action.perform()
        time.sleep(2)

def info_tooltips(driver=None, element=None):
    info_tooltip = driver.find_element(By.CSS_SELECTOR, element)
    action = ActionChains(driver)
    action.move_to_element(info_tooltip).perform()
    time.sleep(1)
    tt = driver.find_element(By.ID, "tooltip-direction-bottom").text
    # log.info(tt.text)
    time.sleep(1)
    return tt

def pan(driver=None, move_x=None, move_y=None):
    try:
        pan_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, NM.pan_button_id)))
        disabled = driver.find_element(By.XPATH, NM.pan_button_disabled).is_displayed()
        check.is_true(disabled, log.info(f'pan_button is not selected: {disabled}'))

        time.sleep(2)
        pan_button.click()
        time.sleep(2)
        enabled = driver.find_element(By.XPATH, NM.pan_button_enabled).is_displayed()
        check.is_true(enabled, log.info(f'pan_button is selected: {enabled}'))

        location = driver.find_element(By.CSS_SELECTOR, NM.image_view)
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(location, move_x, move_y).perform()
        time.sleep(2)
        pan_button.click()
        time.sleep(2)
        disabled = driver.find_element(By.XPATH, NM.pan_button_disabled).is_displayed()
        check.is_true(disabled, log.info(f'pan_button is not selected: {disabled}'))
    except:
        log.info(f'Something has gone wrong with pan image')

def check_tooltip(driver=None, element=None, expected_tt=None):
    try:
        tooltip = driver.find_element(By.ID, element)
        action = ActionChains(driver)
        action.move_to_element(tooltip).perform()
        time.sleep(1)
        tt = driver.find_element(By.ID, "tooltip-direction-bottom").text
        check.equal(tt, expected_tt, log.info(f"check the tooltip matches: \"{tt}\" == \"{expected_tt}\""))
        time.sleep(1)
    except:
        log.error(f"something went wrong checking for {element} tooltip")

def change_layout(driver=None, layout=None):
    layout_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, layout))) #driver.find_element(By.XPATH, layout)
    layout_button.click()
    time.sleep(2) # TODO - this is a dumb click want to get buttons detected to check enabled disabled before and after click()
    # try:
    #     enabled = driver.find_element(By.XPATH, NM.layout_2x1_enabled).is_displayed()
    #     log.info(f'layout is already selected: {enabled}')
    # except:
    #     disabled = driver.find_element(By.XPATH, NM.layout_2x1_disabled).is_displayed()
    #     check.is_true(disabled, log.info(f'pan_button is selected: {disabled}'))
    #     layout_button = driver.find_element(By.XPATH, layout)
    #     layout_button.click()
    #     enabled = driver.find_element(By.XPATH, NM.layout_2x1_enabled).is_displayed()
    #     check.is_true(enabled, log.info(f'pan_button is selected: {disabled}'))
    #     time.sleep(2)