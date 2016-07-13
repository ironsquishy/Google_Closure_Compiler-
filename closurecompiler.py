#!/usr/bin/env python

#Google Closure Compile interface and compile from URL.

import httplib, urllib, sys


def main(optimize, urlArg, fileNameArg):

    params = urllib.urlencode([
    ('code_url', urlArg),
    ('compilation_level', optimize),
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
    if len(sys.argv) > 2:
        if sys.argv[1] == '-w':
            optimize = 'WHITESPACE_ONLY'
        elif sys.argv[1] == '-a':
            optimize = 'ADVANCED_OPTIMIZATIONS'
        elif sys.argv[1] == '-s':
            optimize = 'SIMPLE_OPTIMIZATIONS'
        else:
            optimize = 'SIMPLE_OPTIMIZATIONS'
        urlArg = sys.argv[2];
        fileName = sys.argv[3];
        main(optimize, urlArg, fileName)
    else:
       optimize = 'SIMPLE_OPTIMIZATIONS'
       urlArg = sys.argv[1]
       fileName = sys.argv[2]
       main(optimize, urlArg, fileName)
