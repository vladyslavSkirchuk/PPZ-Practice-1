from requests import RequestException


def get_text_info(filepath: str) -> None:
    from pprint import pprint

    with open(filepath) as f:
        data = f.read().lower()

    list_of_data = data.split(' ')
    list_of_words = list(word for word in list_of_data if word.isalpha())
    unique_words = set(list_of_words)

    counts = dict()
    for word in unique_words:
        counts.update({word: list_of_words.count(word)})

    pprint(counts)


def download_csv(urlpath: str) -> None:
    import requests
    import csv
    save_as = 'source_data/file.csv'

    try:
        data = requests.get(url=urlpath)
    except RequestException as exc:
        print(f'Error: {str(exc)}')
    else:
        rowed_data = [row.split(';') for row in data.content.decode().strip().split('\n')][:-1]

        with open(save_as, 'w') as download:
            writer = csv.writer(download)
            writer.writerows(rowed_data)


if __name__ == '__main__':
    get_text_info(input('Enter .txt filepath: '))
    download_csv(input('Enter .csv urlpath: '))
