import re


def domain_name(url):
    domain = re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
    return domain


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


