#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import islice
import json , sys
from elasticsearch import Elasticsearch , helpers
import threading

_index = 'product_name' # 修改为索引名
_type = 'product' # 修改为类型名
es_url = 'http://localhost:9200/' # 修改为 elasticsearch 服务器

reload(sys)
sys.setdefaultencoding('utf-8')  
es = Elasticsearch(es_url)
#es.indices.create(index='webinfo', ignore=400,body = mapping)
#es.indices.create(index=_index, ignore=400)
chunk_len = 10
num = 0

def bulk_es(chunk_data):
    bulks=[]
    try:
        for i in xrange(chunk_len):
            bulks.append({
                    "_index": _index,
                    "_type": _type,
                    "_source": chunk_data[i]
                })
        helpers.bulk(es, bulks)
    except:
        pass

with open(sys.argv[1]) as f:
    while True:
        lines = list(islice(f, chunk_len))
        num =num +chunk_len
        sys.stdout.write('\r' + 'num:'+'%d' % num)
        sys.stdout.flush()
        bulk_es(lines)
        if not lines:
            print "\n"
            print "task has finished"
            break
