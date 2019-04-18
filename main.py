from logger import Logger
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

logger = Logger("Simple-Endpointer-Server", 'simple-endpoint-server.log')


def printinfo(value: str):
    logger.debug(value)


def printfail(value: str, error):
    logger.fail(value, error)


def printsuccess(value: str):
    logger.success(value)


def read_urls(strfilename: str):
    urls = []
    f = None
    try:
        printinfo('Reading file' + strfilename)
        f = open(strfilename, "r")
        for line in f:
            urls.append(line)
    except FileNotFoundError as error:
        printfail(' => Arquivo não encontrado', error)
    finally:
        if f:
            f.close()

    return urls


def test_urls(urls):
    for url in urls:
        req = Request(url)
        try:
            printinfo('Checking url {}'.format(url).rstrip("\n\r"))
            urlopen(req).read()
            printsuccess(' => OK')
        except (HTTPError, URLError) as error:
            printfail(' => NOK', error)


filename = input("Informe o arquivo com os endereços: ")
test_urls(read_urls(filename))
