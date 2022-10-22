from time import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://web.whatsapp.com/')
time.sleep(20)

def bot():
    try:
        bolinha = driver.find_element_by_class_name('l7jjieqr il1gyv3w ei5e7seu h0viaqh7 tpmajp1w k07a8sro riy2oczp dsh4tgtl hnx8ox4h gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt')
        bolinha = driver.find_elements_by_class_name('l7jjieqr il1gyv3w ei5e7seu h0viaqh7 tpmajp1w k07a8sro riy2oczp dsh4tgtl hnx8ox4h gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt')
        clicaBolinhas = bolinha[-1]
        runBolinha = webdriver.common.action_chains.ActionChains(driver)
        runBolinha.move_to_element_with_offset(clicaBolinhas,0,-20)
        runBolinha.click()
        runBolinha.perform()
        runBolinha.click()
        runBolinha.perform()
        

    except:
        print('Buscando novas mensagens')
        time.sleep(2)
while True:
    bot()
