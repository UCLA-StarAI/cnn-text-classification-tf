#! /usr/bin/env python

import sys, re
import numpy as np
import os
import time
import datetime



def sep_file(data_file):
    f_pos = open('xing_test.pos', 'w')
    f_neg = open('xing_test.neg', 'w')
    with open(data_file, "rb") as f_in:
        for line in f_in:
            check = int(line[0])
            if(check==0):
                f_neg.write(line[2:])
            else:
                f_pos.write(line[2:])
    f_pos.close()
    f_neg.close()

if __name__=="__main__":
    data_file = sys.argv[1]
    sep_file(data_file)
    print "done!"
