#!/usr/bin/env python3
import sys, os

print( 'sys.argv[0] = {}'.format( sys.argv[0] ) )
print( 'cwd: ' + os.getcwd() )
pathname = os.path.dirname( sys.argv[0] )
print( 'pathname: ' + pathname )
fullpath = os.path.abspath( pathname )
print( 'fullpath: ' + fullpath )
