__author__ = 'Cameron'
import re
import unicodedata
import requests

def remove_links(str):
    """
    Removes all [] from any string passed in
    :param str:
    :return: cleaned string
    """
    stripped_str = re.sub("\[.*\]","", str)
    str_list = filter(None, stripped_str.split(" "))
    built_string = " ".join(str_list)
    return built_string

def replace_non_break_space(str):
    """
    Removes the dumb &nlbd non break space
    :param str: str to work on
    :return: cleaned string
    """
    non_break_space = u'\xa0'
    str = str.replace(non_break_space, " ")
    return str

def new_line_to_whitespace(str):
    """
    Gets rid of all new lines and changes to whitespace, front end will handle the newlines
    :param str:
    :return:
    """
    str = str.replace("\n", " ")
    return str

def remove_unicode(str):
    """
    Removes all special unicode characters and changes to ascii
    :param str:
    :return: ascii style string
    """
    return unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')

def clean_string(str):
    """
    cleans all strings passed in
    :param str:
    :return:
    """
    if not isinstance(str, basestring):
        str = remove_unicode(str)
    str = replace_non_break_space(str)
    str = new_line_to_whitespace(str)
    str = remove_links(str)
    return str

def get_html_from_url(url):
    """
    Gets the html from a given webpage
    :param url: Url to retrieve html
    :return: all html
    """
    request = requests.get(url)
    data = request.text
    return data