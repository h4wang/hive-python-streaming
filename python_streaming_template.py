#!/usr/bin/python
"""
Template for Hive-python transformation
Add your own methods to utilize Python streaming analysis
Author: Hua Wang
"""
import sys
from operator import itemgetter

class Transform:
    def stripLine(self,line):
        """clean input"""
        line = line.strip()
        line = str(line).replace("[", '').replace(']', '').replace('{', '').replace('},', ';').replace('}', '').replace('"','')
        return line

    def buildListOfDict (self,input_string):
        """Take string that was array of structs in Hive and build into list of dict in python"""
        arr = []
        input_string = input_string.split(';')
        for i in range(len(input_string)):
            arr.append(dict(item.split(":") for item in input_string[i].split(",")))
        return arr

if __name__ == '__main__':
    tf = Transform()
    for line in sys.stdin:
        stripped_line = tf.stripLine(line)
        #provide input columns
        campaign_id,strategy_id,uuid,vt_period,imp,pf,num_click = stripped_line.split('\t')
        #transform complex colomns into list of dicts
        imp_list = tf.buildListOfDict(imp)
        pf_list = tf.buildListOfDict(pf)

        #main calculation codes go here

        #outputs go here - must be string
        output = [campaign_id, strategy_id, uuid, str(num_imp), num_click, str(num_conv), category]
        print '\t'.join(output)




























