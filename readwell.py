"""
Functions to interact with the Goodreads API
"""

import configparser
from rauth.service import OAuth1Service, OAuth1Session
from bs4 import BeautifulSoup

def get_access_configs():
    """
    Looks for access.ini and reads developer key and secret
    from it if found.
    access.ini is expected to be in the following format:

    [GOODREADS_ACCESS]
    KEY = 4S0V6DwoWe76q9FAVwtr
    SECRET = eGefOGrVzaAnR2k6yspersPXXYdOaFj6hOEXzia1
    """

    parser = configparser.ConfigParser()
    parse_result = parser.read('access.ini')
    if not parse_result:
        return(None)

    # else
    return((parser['GOODREADS_ACCESS']['KEY'], parser['GOODREADS_ACCESS']['SECRET']))

def get_token_configs():
    """
    Looks for tokens.ini and reads saved session token and session token secret
    from it if found.
    tokens.ini is expected to be in the following format:

    [GOODREADS_TOKENS]
    TOKEN = k7xiGLmu5RpNVMWgQKpL
    TOKEN_SECRET = l4DCZh6dXKwAixD3PDVOkqKVMsTM3daIMGlXq76u
    """

    parser = configparser.ConfigParser()
    parse_result = parser.read('tokens.ini')

    if not parse_result:
        return(None)

    return(parser['GOODREADS_TOKENS']['TOKEN'], parser['GOODREADS_TOKENS']['TOKEN_SECRET'])

def get_session():
    """
    Creates a session using the developer key and secret,
    and session token and token secret.
    """

    key, secret = get_access_configs()
    if not key:
        raise Exception('No access.ini file found with KEY and SECRET information to authenticate.')

    token, token_secret = get_token_configs()
    if not token:
        # todo: implement authentication logic
        raise NotImplementedError

    new_session = OAuth1Session(key, secret, token, token_secret)
    return(new_session)

def get_user_id(sess):
    """
    Given a session, will return the authenticated user's ID.
    """
    if not isinstance(sess, OAuth1Session):
        raise TypeError('Was not passed a proper OAuth1Session')

    response = sess.get('https://www.goodreads.com/api/auth_user')
    response.raise_for_status()
    response_soup = BeautifulSoup(response.content, 'lxml')
    user_id = response_soup.user['id']
    return(user_id)
