from bs4 import BeautifulSoup
import requests

def hackathon_():
    website = 'devfolio'
    url = f"https://{website}.co/hackathons"
    html = requests.get(url).text
    
    soup = BeautifulSoup(html, 'html.parser')

    hackathons = soup.find_all('div', class_='sc-fmGnzW iXcaew CompactHackathonCard__StyledCard-sc-9ff45231-0 fudhHJ')
    hackathon_data = []
    for hackathon in hackathons:
        heading = hackathon.find('h3', class_='sc-hZgfyJ oSdsf')
        theme = hackathon.find('p', class_='sc-hZgfyJ hZQPen')
        theme_result = hackathon.find('div', class_='sc-hZgfyJ hZQPen')

        heading = heading.text if heading else ""
        theme = theme.text if theme else ""
        theme_result = theme_result.text if theme_result else ""

        

        hackathon_data.append({
            'heading': heading,
            'theme': theme,
            'theme_result': theme_result,
        })
    
    
    return hackathon_data





































