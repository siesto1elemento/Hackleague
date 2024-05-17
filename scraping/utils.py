from bs4 import BeautifulSoup
import requests

def hackathon_():
    website = 'devfolio'
    url = f"https://{website}.co/hackathons"
    html = requests.get(url).text
    
    soup = BeautifulSoup(html, 'lxml')

    hackathons = soup.find_all('div', class_='sc-dwVMhp fdwmgb CompactHackathonCard__StyledCard-sc-4a10fa2a-0 ihpCnk')
    hackathon_data = []
    for hackathon in hackathons:
        heading = hackathon.find('h3', class_='sc-cHPgQl guEEhq').text
        theme = hackathon.find('p', class_='sc-cHPgQl kCrHaC').text
        theme_result = hackathon.find('div', class_='sc-tQuYZ hdPpzk').text
        link = hackathon.find('a', class_='Link__LinkBase-sc-af40de1d-0 lkflLS').get('href')
        

        hackathon_data.append({
            'heading': heading,
            'theme': theme,
            'theme_result': theme_result,
            'link':link,
        })
    
    
    return hackathon_data





































