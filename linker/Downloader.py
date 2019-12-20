from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, sys
from selenium.webdriver import ActionChains


# Catalog URL dictionary
catalog_url_dic = {
    "catalog_url_benz_1": "____",
    "catalog_url_bmw_2": "____",
    "catalog_url_audi_3": "____",
    "catalog_url_volkswagen_4": "____",
    "catalog_url_mini_5": "____",
    "catalog_url_volvo_6": "____",
    "catalog_url_jaguar_7": "____",
    "catalog_url_landrover_8": "____",
    "catalog_url_porsche_9": "____",
    "catalog_url_ferrari_10": "____",
    "catalog_url_lambo_11": "____",
    "catalog_url_maserati_12": "____",
    "catalog_url_peugeot_13": "____",
    "catalog_url_citroen_14": "____",
    "catalog_url_ds_15": "____",
    "catalog_url_smart_16": "____",
    "catalog_url_bentley_17": "____",
    "catalog_url_rollsroyce_18": "____",
    "catalog_url_toyota_19": "____",
    "catalog_url_lexus_20": "____",
    "catalog_url_nissan_21": "____",
    "catalog_url_infinity_22": "____",
    "catalog_url_lincoln_23": "____",
    "catalog_url_honda_24": "____",
    "catalog_url_jeep_25": "____",
    "catalog_url_ford_26": "____",
    "catalog_url_cadillac_27": "____",
}

# Required PATHs
catalog_url = 'https://www.mercedes-benz.co.kr/passengercars/mercedes-benz-cars/catalog/disclaimer-pricelist.module.html'
compressor_url = 'https://www.ilovepdf.com/compress_pdf'
pdf2img_url = 'https://www.ilovepdf.com/pdf_to_jpg'
chromedriver_dir = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
downloadFile_dir = r"C:\Users\ADMIN\Desktop\Catalog_noye\Resources\downloads"

# Open up a Chrome browser and navigate to web page(PDF viewer disabled)
chromeOptions = Options()
prefs = {"plugins.always_open_pdf_externally": True,
         "download.default_directory": downloadFile_dir,
         "download.prompt_for_download": False,
         "download.directory_upgrade": True,
         'profile.default_content_setting_values': {'cookies': 2, 'images': 2,}
                                                    # 'javascript': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                    # 'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                                    # 'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                    # 'media_stream_mic': 2, 'media_stream_camera': 2,
                                                    # 'protocol_handlers': 2,
                                                    # 'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                    # 'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                    # 'metro_switch_to_desktop': 2,
                                                    # 'protected_media_identifier': 2, 'app_banner': 2,
                                                    # 'site_engagement': 2,
                                                    # 'durable_storage': 2}
         }

chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver_dir, options=chromeOptions)
driver.get(pdf2img_url)


# Extract the catalog by X_PATH & Download
catalogs = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div[3]/input').send_keys(r'C:\Users\ADMIN\Desktop\Sanjaa\카탈로그\21.Nissan\Catalogs_compressed\370Z-catalog-201901.pdf')
catalogs = driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
catalogs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/a"))).click()




