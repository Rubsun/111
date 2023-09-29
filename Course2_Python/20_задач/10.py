def search_email(email: str) -> bool:
    HOSTS = ['yandex.ru', 'mail.ru']
    return ' ' not in email and any([email.endswith('@'+host) for host in HOSTS])