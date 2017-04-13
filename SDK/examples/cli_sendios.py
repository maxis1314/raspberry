#!/usr/bin/env python
# -*- coding: utf-8 -*-


from iospush import ios_push

if __name__ == "__main__":
    message = sys.argv[1]    
    print ios_push(message)
