from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
import sys

EVENT_ST="4769"
WARN="warning:ST without TGT"
#WARN="attack:test"
RESULT_NOTGT_real="attack: Golden Ticket is used"
RESULT_NORMAL="normal"
INDEX_real="realtime-*"
INDEX_packet="packet"
DOC_TYPE="doc"

def update_event(ip_src):
    ip_ptn='*'+ip_src+'*'
    es = Elasticsearch('10.0.19.112:9200')
    s = Search(using=es, index=INDEX_real)
    s = s[0:10000]
    q = Q('match', indicator__keyword= WARN) & Q('match', event_id = EVENT_ST) & Q('wildcard', event_data__IpAddress__keyword = ip_ptn)
    s1 = s.query(q)
    response = s1.execute()
    id=''
    index=''
    h = response[len(response)-1]
    id=h.meta.id
    index=h.meta.index
    #print(h.meta.id)

    if len(response) != 0:
        es.update(index=index, doc_type=DOC_TYPE, id=id, body={'doc': {'indicator': RESULT_NOTGT_real}})
        print(RESULT_NOTGT_real)
        return False

    else:
        return True


def update_packet(cipher):
    es = Elasticsearch('10.0.19.112:9200')
    s = Search(using=es, index=INDEX_packet)
    s = s[0:10000]
    q = Q('match_phrase', layers__kerberos_cipher = cipher)
    s1 = s.query(q)
    response = s1.execute()
    id=''
    index=''

    if len(response) == 0:
        return True

    for h in response:
        id=h.meta.id
        index=h.meta.index
        kerberos_msg_type=h.layers.kerberos_msg_type[0]

        if kerberos_msg_type=='12':
            es.update(index=index, doc_type=DOC_TYPE, id=id, body={'doc': {'indicator': 'attack: Golden Ticket is used'}})
            print('attack: Golden Ticket is used')

        if kerberos_msg_type=='14':
            es.update(index=index, doc_type=DOC_TYPE, id=id, body={'doc': {'indicator': 'attack: Silver Ticket is used'}})
            print('attack: Silver Ticket is used')

    return False
