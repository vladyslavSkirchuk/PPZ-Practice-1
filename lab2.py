from typing import List


def palindrome(text: str) -> List[str]:
    palindromes = list()
    text = text.lower()
    list_of_words = text.split(' ')

    for word in list_of_words:
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes


def validate_ip(ip: str) -> str:
    import ipaddress

    try:
        ip_obj = ipaddress.ip_address(ip)
        print(f'This ip is valid: {ip_obj}')
    except ValueError:
        print(f'This ip is not valid: {ip}')


def get_os():
    import platform

    system = platform.system()

    match system:
        case 'Linux':
            print('Linux')
        case 'Darwin':
            print('Mac')
        case 'Windows':
            print('Windows')
        case _:
            print('Unregistered OS')


if __name__ == '__main__':
    print(palindrome(input('Enter your text for search palindromes: ')))
    validate_ip(input('Enter ip address: '))
    get_os()
