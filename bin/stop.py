#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import Popen

from redis import Redis

from lookyloo.default import get_homedir, get_socket_path


def main():
    get_homedir()
    p = Popen(['shutdown'])
    p.wait()
    r = Redis(unix_socket_path=get_socket_path('cache'), db=1)
    r.delete('shutdown')
    r = Redis(unix_socket_path=get_socket_path('cache'))
    r.delete('tree_cache')
    Popen(['run_backend', '--stop'])


if __name__ == '__main__':
    main()
