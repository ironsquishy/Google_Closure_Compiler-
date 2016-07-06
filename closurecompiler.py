#!/usr/bin/env python

#Google Closure Compile interface and compile from URL.

import httplib, urllib, sys


def main(urlArg, fileNameArg):

    params = urllib.urlencode([
    ('code_url', urlArg),
    ('compilation_level', 'WHITESPACE_ONLY'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code')
    ])

    headers = {"Content-type": "application/x-www-form-urlencoded"}

    conn = httplib.HTTPConnection('closure-compiler.appspot.com')
    conn.request('POST', '/compile', params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    with open(fileNameArg, 'w') as fileOuput:
        fileOuput.write(data)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
