# readwell

***This project is on hold as it seems like the Goodreads API is in a bad state with no hope of improvement. As far as I can tell, the API calls consistently return erroneous data - for example, the number of shelves doesn't match my number of shelves, and the number of books in each shelf is way off.***

`readwell` is a lightweight Python script with functions to interact with the [Goodreads][] [API][].

[Goodreads]: https://www.goodreads.com/ "Goodreads"
[API]: https://www.goodreads.com/api/index "Goodreads API documentation"

This project is not affiliated in any way with Goodreads. It is not an official client, and could stop working at any time. Really, I just created this for myself.

## Philosophy

The project's philosophy is simple: why go to the site to do the thing when I can do it from the comfort of my own command line? The project's less simplistic philosophy is that I wanted an excuse to write some Python that made API calls, and Goodreads was a great candidate because I can see myself wanting to automate interactions with my reading data soon.

## Usage

This is starting out as a simple module/script with functions to import and use. The script creates an OAuth session and uses it to query the API.

The current implementation is rudimentary but growing. Right now, the functions expect a developer key, secret, a session token, and a session token secret. This is expected to be in already saved `ini` files (see below), but the script will grow to enable the user to generate and save the session tokens. The user will have to get their own developer key and secret, which is [easy to do][getapiaccess].

[getapiaccess]: https://www.goodreads.com/api/keys "Register for Goodreads API"

Example of current usage is:

```python
from readwell import *
sess = get_session()
user_id = get_user_id(sess)
```

For `get_session()` to work, the script expects to find two files, `access.ini` and `tokens.ini`.

`access.ini` should contain the developer's key and secret, in the following format:

```text
[GOODREADS_ACCESS]
KEY = 4S0V6DwoWe76q9FAVwtr
SECRET = eGefOGrVzaAnR2k6yspersPXXYdOaFj6hOEXzia1
```

Those are of course random strings and it would be amazing if they actually worked.

`tokens.ini` stores session token and token secret.

```text
[GOODREADS_TOKENS]
TOKEN = k7xiGLmu5RpNVMWgQKpL
TOKEN_SECRET = l4DCZh6dXKwAixD3PDVOkqKVMsTM3daIMGlXq76u
```

## See also

- [`sefakilic/goodreads`][sefakilic_goodreads]: A wrapper that is likely fuller than whatever `readwell` is going to be, but the project's README indicates it is no longer maintained. I haven't tried using it and haven't looked at the code, but am mentioning it here in the spirit of [See Also][seealso].

[sefakilic_goodreads]: https://github.com/sefakilic/goodreads "A Python wrapper for Goodreads API - no longer maintained"
[seealso]: https://macwright.org/2015/01/12/see-also.html "macwright.org - See Also"
