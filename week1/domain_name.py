from urllib import parse


def domain_name(url):
    res = parse.urlparse(url)
    if res.netloc:
        res = res.netloc.split(".")
    else:
        res = res.path.split(".")
    return res[0] if res[0] != "www" else res[1]


# A different variant not using urlparse
def my_domain_name(url):
    levels = url.split("/")
    for lvl in levels:
        if lvl and lvl not in ("http:", "https:"):
            levels = lvl.split(".")
            break
    return levels[0] if levels[0] != "www" else levels[1]


if __name__ == "__main__":
    names = (
        "http://github.com/carbonfive/raygun",
        "http://www.zombie-bites.com",
        "https://www.cnet.com",
        "http://google.co.jp",
        "www.xakep.ru",
        "youtube.com",
        "gov.ru.co.uk",
        "abracadabra",
        "http://"
        )
    for n in names:
        print(n, "=>", domain_name(n))
    print("empty: ", domain_name(""))

    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
