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
        link = hackathon.find('a', class_='Link__LinkBase-sc-e5d23d99-0 bnxtME')
        link = link.get("href")
        if len(hackathon.find_all('p',class_='sc-hZgfyJ ifkmYk')) > 2:
            mode = hackathon.find_all('p', class_='sc-hZgfyJ ifkmYk')[0]
            date = hackathon.find_all('p',class_='sc-hZgfyJ ifkmYk')[2]
        else:
            mode = None
            date = None
        heading = heading.text if heading else ""
        theme = theme.text if theme else ""
        theme_result = theme_result.text if theme_result else ""
        mode = mode.text if mode else ""
        date = date.text if date else ""


        

        hackathon_data.append({
            'heading': heading,
            'theme': theme,
            'theme_result': theme_result,
            'link':link,
            'mode':mode,
            'date':date
        })
    
    
    return hackathon_data





































