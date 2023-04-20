def parse_ukd_data():
    import requests
    from bs4 import BeautifulSoup as bs

    data = requests.get(url='https://ukd.edu.ua')

    soup = bs(data.content, 'html.parser')
    divs = soup.div
    block = divs.find(class_='col-lg-9 col-md-12')
    ulki = block.ul
    ashki = ulki.find_all('a')
    for spec in ashki:
        if spec.text == 'Спеціальності':
            continue
        print(spec.text)


if __name__ == '__main__':
    parse_ukd_data()
