from functions import *
import pytest
import pytest_check as check
import time
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
ADMIN_USER = os.getenv('ADMIN_USER')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

web_url = r"https://alpha.app.behold.ai"
# web_url = r"https://app.behold.ai"
web_url_login = fr'{web_url}/auth/signin'

def test1():
    try:
        test1 = Start_Web()
        driver = test1.start_chrome(url=web_url_login)
        login(driver=driver, user=ADMIN_USER, p_word=ADMIN_PASSWORD)
        sl_edit = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.sl_edit_btn)))
        assert sl_edit is not None
        log.info(f'Edit button exists')
        sl_edit.click()
    except:
        log.info(r"didn't find the edit button")
        driver.quit()
    time.sleep(10)
    driver.quit()


def test_login():
    # cmd = '"C:\\Users\\KevinHarris\\source\\repos\\docstowav\\ffmpeg.exe" -y -f dshow -i video="screen-capture-recorder" -r 10 -t 30 "C:\\Users\\KevinHarris\\source\\repos\\docstowav\\screen-capture.mp4"'
    # proc = subprocess.Popen(cmd)
    test_login = Start_Web()
    driver = test_login.start_chrome(url=web_url_login)
    actual = login(driver=driver, user=ADMIN_USER, p_word=ADMIN_PASSWORD)

    expectedUrl = fr"{web_url}/home"
    log.info(rf"{expectedUrl} and {actual}")
    driver.quit()
    if check.equal(actual, expectedUrl, log.info(fr"checking The expected:{expectedUrl} == actual:{actual}")):
        log.info("they matched")
    else:
        log.info("they don't match")
    # proc.wait(10)


def test_Invalid_login():
    test_Invalid_login = Start_Web()
    driver = test_Invalid_login.start_chrome(url=web_url_login)
    user = "kevinh@behold.ai1"
    p_word = ADMIN_PASSWORD
    '''Login as user'''
    username = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.username_xpath)))
    username.send_keys(user)
    log.info(f"username used: \"{user}\"")
    password = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.password_xpath)))
    password.send_keys(p_word)
    log.info(f"password used: ***")
    submit = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.login_submit_xpath)))
    submit.click()
    log.info(f"submit clicked")
    failedLogin = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.login_error)))

    '''give me all the attributes'''
    # log.info(failedLogin.get_property('attributes'))
    # log.info(failedLogin.get_attribute('role'))

    # todo could be made more robust!
    if check.equal(failedLogin.get_attribute('role'), "alert", log.info(fr"checking the invalid user is not logged in")):
        log.info("failed to login")
    else:
        log.info("something went wrong")
    driver.quit()


def test_layout_switch():
    try:
        test_layout_switch = Start_Web()
        driver = test_layout_switch.start_chrome(url=web_url_login)
        login(driver=driver, user=ADMIN_USER, p_word=ADMIN_PASSWORD)

        '''filter a specified worklist to view'''
        load_worklist(driver=driver, worklist="KH 12-07-22 CXR")
        load_by_accession(driver=driver, accession="4105003980362")

        change_layout(driver=driver, layout=NM.layout_2x1)
    except:
        log.info(r"didn't find the something button")
        driver.quit()
    time.sleep(5)
    driver.quit()


def test_sl_table():
    test_sl_table = Start_Web()
    driver = test_sl_table.start_chrome(url=web_url_login)
    actual = login(driver=driver, user=ADMIN_USER, p_word=ADMIN_PASSWORD)

    # filter a specified worklist to view
    load_worklist(driver=driver, worklist="KH 12-07-22 CXR")
    cols, rows = get_table_cols_rows(driver=driver)
    log.info(f"columns: {cols}, Rows: {rows}")
    clear_accession(driver=driver)
    cols, rows = get_table_cols_rows(driver=driver)
    log.info(f"{cols}, {rows}")


def test_set_normal():
    try:
        test_set_normal = Start_Web()
        driver = test_set_normal.start_chrome(url=web_url_login)
        login(driver=driver, user=ADMIN_USER, p_word=ADMIN_PASSWORD)

        '''filter a specified worklist to view'''
        load_worklist(driver=driver, worklist="KH 12-07-22 CXR")

        clear_accession(driver=driver)
        # get_table_content(driver=driver)
        # cols, rows = get_table_cols_rows(driver=driver)
        # log.info(f"columns: {cols}, Rows: {rows}")
        load_by_accession(driver=driver, accession="4105003980362")

        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.normalSelector)))
        invert_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, NM.invert_button_id)))
        time.sleep(2)
        invert_button.click()
        time.sleep(2)
        invert_button.click()
        time.sleep(2)

        wwwc_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, NM.wwwc_button_id)))
        wwwc_enabled = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, NM.wwwc_button_enabled)))
        log.info(f'Window Level Center button is selected: {wwwc_enabled.is_displayed()}')


        check_tooltip(driver=driver, element=NM.reset_button_id, expected_tt="Reset Image")
        check_tooltip(driver=driver, element=NM.wwwc_button_id, expected_tt="Window Level Tool")
        check_tooltip(driver=driver, element=NM.invert_button_id, expected_tt="Invert")
        check_tooltip(driver=driver, element=NM.pan_button_id, expected_tt="Pan")
        check_tooltip(driver=driver, element=NM.zoom_button_id, expected_tt="Zoom")

        pan(driver=driver, move_x="100", move_y="-100")

        subOptimalSelector = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, NM.subOptimalSelector)))
        subOptimalSelector.click()
        time.sleep(1)
        draw_rectangle(driver=driver, start_x="-500", start_y="200", end_x="100", end_y="100")
        draw_rectangle(driver=driver, start_x="-300", start_y="-400", end_x="100", end_y="100")
        draw_ellipse(driver=driver, start_x="100", start_y="-500", end_x="100", end_y="100")
        draw_ellipse(driver=driver, start_x="300", start_y="000", end_x="50", end_y="50")
        draw_ruler(driver=driver, start_x="150", start_y="150", end_x="100", end_y="100")
        draw_ruler(driver=driver, start_x="300", start_y="-200", end_x="100", end_y="100")
        draw_point_probe(driver=driver, start_x="300", start_y="300")
        draw_point_probe(driver=driver, start_x="350", start_y="350")
        draw_angle(driver=driver, start_x="0", start_y="0", end_x1="100", end_y1="100", end_x2="-100", end_y2="0")

        screengrab_image(driver=driver, imageview="#selectedstudy > div > div.Pane.vertical.Pane1",
                         imagename='file1.png')

        '''get tooltip'''
        tt = info_tooltips(driver=driver, element=NM.info_1)
        expected = "Normal frontal image performed in inspiration shows a well-penetrated radiograph. " \
                   "Vertebrae are visible behind the heart. " \
                   "Left hemidiaphragm is visible to the edge of the spine. " \
                   "The lungs are appropriately visualized and the vascular markings are not prominent. " \
                   "An abnormality is any finding that is not within normal limits on the image including areas outside the chest."
        check.equal(tt, expected, log.info(f"Assert that the tooltip text is as expected"))

        tt = info_tooltips(driver=driver, element=NM.info_2)
        expected = "A film that does not fulfill the definition of an optimal quality image.\n\n" \
                   "The definition of an optimal quality image is an image that has all the following:\n" \
                   "* The entire chest including lung apices and the costophrenic angles is included in the Field of view.\n" \
                   "* No patient rotation.\n" \
                   "* Adequate depth of inspiration.\n" \
                   "* Adequate degree of photon penetration."
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_3)
        expected = "Reduced volume is seen, accompanied by increased opacity in the affected part of the lung. " \
                   "Atelectasis is often associated with abnormal displacement of fissures, bronchi, vessels, " \
                   "diaphragm, heart, or mediastinum. The distribution can be lobar, segmental, or subsegmental. " \
                   "Atelectasis is often qualified by descriptors such as linear, discoid, or platelike."
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_4)
        expected = "Collapse refers to collapse of a lobe of the lung. Collapse is also used to describe sever " \
                   "atelectasis or atelectasis associated with opacity. Bowing or displacement of a fissure occurs " \
                   "towards the collapsing lobe a significant amount of volume loss that causes opacity.\n\n" \
                   "Direct signs:\n" \
                   "* displacement of fissures\n" \
                   "* crowding of pulmonary vessels\n\n" \
                   "Indirect signs:\n" \
                   "* elevation of the ipsilateral hemidiaphragm\n" \
                   "* crowding of the ipsilateral ribs\n" \
                   "* shift of the mediastinum towards the side of atelectasis\n" \
                   "* compensatory hyperinflation of normal lobes\n" \
                   "* hilar displacement towards the collapse"
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_5)
        expected = "Pathologic process that fills the alveoli with fluid, pus, blood, cells or other substances " \
                   "resulting in lobar, diffuse or multifocal ill-defined opacities. There is no volume loss and " \
                   "unlike a mass, the findings are usually not well-defined."
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_6)
        expected = '“Covid-like” features on chest radiographs: Multiple bilateral patchy or diffuse asymmetric airspace opacities (or ground glass opacities)'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_7)
        expected = '1. increase in density and/or size of the hilar\n' \
                   '2. irregular appearance of the hilar\n' \
                   '3. Suspicion of hilar mass\n' \
                   '4. This is a highly subjective class, only tag when confident'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_8)
        expected = 'Any pulmonary, pleural, or mediastinal lesion seen on chest radiographs as an opacity greater ' \
                   'than 3 cm in diameter (without regard to contour, border, or density characteristics). ' \
                   'Mass usually implies a solid or partly solid opacity.'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_9)
        expected = 'Highly subjective category -please only tag if confident about diagnosis'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_10)
        expected = 'Presence of medical devise on the CXR such as sternotomy wires, pacemaker,' \
                   ' central line and drainage tube.'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_11)
        expected = 'A rounded opacity, well or poorly defined, measuring up to 3 cm in diameter.'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_12)
        expected = 'Highly subjective category -please only tag if confident about diagnosis'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_13)
        expected = '* Pneumothorax is gas/air without lung markings or gas/air in the pleural cavity\n' \
                   '* Air is peripheral to the white line of the pleura\n' \
                   '* In upright film the pneumothorax is usually in the apices\n' \
                   '* In supine film the costophrenic angle is abnormally deepened when the pleural air collects ' \
                   'laterally, producing the deep sulcus sign\n' \
                   '* In Hydropneumothorax there is air-fluid level on an upright film'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_14)
        expected = 'Abnormal accumulation of fluid in the extravascular compartments of the lung. Feature on the CXR include:\n' \
                   '* Central pulmonary venous congestions\n' \
                   '* Upper lobe pulmonary venous diversion\n' \
                   '* Peribronchial cuffing and perfihilar haze\n' \
                   '* Septal line/Kerley lines\n' \
                   ' * thickening of interlobar fissures\n' \
                   ' * Air space opacification classically in a batwing distribution'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

        tt = info_tooltips(driver=driver, element=NM.info_15)
        expected = 'Highly subjective category -please only tag if confident about diagnosis'
        check.equal(tt, expected, log.info(f'Assert that the tooltip text is as expected'))

    except:
        log.info(r"didn't like your test")
        driver.quit()
    time.sleep(3)
    driver.quit()


def test_back_to_sl():
    try:
        test_back_to_sl = Start_Web()
        driver = test_back_to_sl.start_chrome(url=web_url_login)
        login(driver=driver, user=ADMIN_USER, p_word=ADMIN_PASSWORD)

        '''filter a specified worklist to view'''
        load_worklist(driver=driver, worklist="KH 12-07-22 CXR")

        clear_accession(driver=driver)
        load_by_accession(driver=driver, accession="4105003980362")
        time.sleep(3)
        submit_report = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, NM.back_to_sl)))
        submit_report.click()
    except:
        log.info(r"didn't like your test")
        driver.quit()
    time.sleep(3)
    driver.quit()
