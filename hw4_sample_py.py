# -*- coding: utf-8 -*-
"""hw4_sample.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pCHAUrmqRd-Xg7DEwnlYU68IzOCyyG1v
"""

from pyspark import SparkContext
import itertools
 
if __name__=='__main__':
    sc = SparkContext()
    rdd = sc.textFile('/data/share/bdm/weekly-patterns-nyc-2019-2020/*')
    header = rdd.first()
    rdd.sample(False, 0.01) \
        .coalesce(1) \
        .mapPartitions(lambda x: itertools.chain([header], x)) \
        .saveAsTextFile('weekly-patterns-nyc-2019-2020-sample')