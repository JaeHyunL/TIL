import bs4
import re
import requests


def xpath_soup(element: bs4.element.NavigableString) -> str:
    """ bs4 엘리먼트 -> Xpath String

    bs4로 크롤링한 데이터를
    front에서 액션 이벤트를 통한 이동을 하기 위해 데이터를 xpath로 변환

    Args:
        element (_type_): _description_

    Returns:
        _type_: _description_
    """

    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
        )
        child = parent
    components.reverse()

    return '/%s' % '/'.join(components)


def custom_crawler(uri: str = "http://localhost:3084/manual/1", 
                   text: str = "", indexPage: int = 1):

    target_text = ''
    try:
        target_text = requests.get(uri).text
    except ConnectionError as ce:
        print('http connection error: %s' % ce)

        return False

    target_tag_list = []
    regex_text = re.compile(text)
    soup = bs4.BeautifulSoup(target_text, "lxml")
    target_tag = soup.find_all(string=regex_text)

    for target in target_tag:
        target_tag_list.append(xpath_soup(target))

    return target_tag_list
