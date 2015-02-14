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
        try:
            stripped_line = tf.stripLine(line)
            #provide input columns
            campaign_id,strategy_id,uuid,vt_period,imp,pf,num_click = stripped_line.split('\t')
            #transform colomns into list of dicts

            num_imp, events = tf.prepare_inputs(imp, pf)

            num_conv, updated_events = attribution(events, int(vt_period))
            touchpoints = build_touchpoints(updated_events)
            category = find_category(touchpoints, num_conv)
            output_cols = [campaign_id, strategy_id, uuid, str(num_imp), num_click, str(num_conv), category]
            print '\t'.join(outputCols)
        except Exception,err:
            continue



























