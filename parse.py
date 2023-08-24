import bs4

with open('sample.html','r') as f:
    soup = bs4.BeautifulSoup(f,'html.parser')
    
em_tags = soup.find_all("em")

for em in em_tags:
    text = em.text.strip()
    if len(text)>1 and text[1]=="/":
        print(text)