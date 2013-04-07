#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, json
from glob import glob
from pprint import pprint

def data_importer(directory, opt='test', fieldname='name_kr'):

    def printer():
        print('\n===' + fieldname.upper() + '===')
        print_filenames(opt)
        print('n(files)\t: '+ str(len(filenames)))
        print('n(items)\t: '+ str(len(fieldlist)))

    def print_filenames(opt):
        if opt != 'all':
            print('Files:')
            pprint(filenames)
        else:
            pass

    filenames = get_filenames(directory, opt)
    fieldlist = get_rawlist(filenames, fieldname)
    printer()
    return fieldlist

def get_filenames(directory, opt):
    allfilenames = all_filenames(directory)
    filenames = select_filenames(allfilenames, opt)
    return filenames

def all_filenames(directory):
    return glob(os.path.join(directory, '*_candidates_*.json'))

def select_filenames(filenames, opt):
    opt = opt.encode('utf-8')
    from pprint import pprint
    if isinstance(opt, int):
        filenames = [filenames[opt]]
    elif isinstance(opt, str):
        if opt == 'all':
            pass
        elif opt == 'test':
            filenames = [filenames[0], filenames[20], filenames[40]]
        elif opt == 'legislators':
            filenames = filenames[:19]
        elif opt == 'mayors':
            filenames = filenames[19:24]
        elif opt == 'presidents':
            filenames = filenames[24:]
        else:
            raise Exception # Options should be in {'all', 'test', 'legistlators', 'mayors', 'presidents'}"
    else:
        raise Exception # Options should either be an integer in [0,40] or string in {'all', 'test', 'legistlators', 'mayors', 'presidents'}
    return filenames

def get_rawlist(filenames, fieldname):
    rawlist = [p[fieldname] for f in filenames for p in read_people(f)]
    return rawlist

def read_people(filename):
    with open(filename, 'r') as f:
        j = f.read()
        people = json.loads(j)
    return people

if __name__ == '__main__':
    fieldlist = data_importer('/home/e9t/data/popong/people', fieldname='education')
    for item in fieldlist:
        print item.encode('utf-8')