import update_es
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
cipher='31:59:e9:9b:47:81:c5:7f:1a:22:27:30:d3:59:c0:c2:e4:e6:8c:b4:74:d0:94:3a:fc:79:f7:45:b7:84:2e:49:77:28:b0:88:3e:d6:a5:d9:68:32:e4:33:91:e5:f2:a2:6b:9d:79:f7:f9:3c:ba:ab:f6:2b:f4:16:a0:13:8d:f6:e7:73:eb:b4:8e:1d:81:68:07:65:94:88:00:5e:c7:ca:f9:2e:82:ab:7b:51:b1:76:20:7f:a8:8f:72:6a:9c:c9:47:0e:dd:f0:ad:7b:21:e7:a5:05:14:0e:01:a4:43:80:35:f7:c1:81:e0:2d:d7:2f:93:55:d4:46:9e:d2:8e:c5:a2:45:09:84:ca:f6:7d:cd:79:be:83:3e:21:13:e3:94:8c:25:3a:56:5e:0f:ff:63:1c:b2:98:ba:f3:4a:76:93:9f:93:73:88:d5:c3:04:60:05:4e:1d:24:4e:44:b2:18:cc:8a:73:c3:6a:37:fc:0e:e2:43:e7:c7:0e:65:42:b9:e7:f0:0e:ec:9b:7d:db:42:ac:1f:44:d2:90:0a:ba:08:89:fd:95:78:1d:00:af:32:9b:66:60:b3:96:fc:ff:13:b7:d3:3e:99:d3:5a:24:a3:5f:d1:ec:c4:c5:0b:ce:4e:42:cc:8b:7f:2a:44:03:6d:9a:de:01:c4:3a:14:60:08:e6:e9:d0:ca:e6:bc:ca:13:b5:5e:9a:8f:c6:4f:a8:cb:08:33:a2:37:9c:07:25:64:fd:cb:84:4f:66:56:85:fb:c9:c2:47:f5:eb:44:06:82:c0:33:a4:65:29:f6:4f:da:7d:68:6f:41:92:29:69:1e:a3:d2:2f:4c:d0:42:ee:96:2f:12:da:1e:a3:7f:b2:52:cb:56:5c:e0:83:98:1b:75:22:97:e8:91:0e:7f:af:c7:eb:7f:c5:72:66:9e:33:20:13:53:4a:37:ec:c2:bb:13:f2:2f:f3:f2:8a:62:88:25:eb:f2:f3:f0:9f:37:70:84:c1:60:dc:4f:cb:23:2f:fc:7e:2b:47:f5:be:ba:66:30:11:af:07:1e:91:35:db:8e:4f:b6:98:ad:3d:ab:b5:32:fc:b3:a9:e4:dd:47:08:a6:9b:0b:a2:f6:60:2d:e7:1d:76:95:23:01:6e:11:15:8a:a2:ed:61:bf:30:49:9a:1c:9d:ca:fd:fd:73:e6:7f:fc:e4:2a:da:b5:cb:27:3e:6c:95:56:ea:1f:96:4e:12:58:40:48:21:0e:e5:be:05:fc:b1:52:09:cb:4c:2b:7f:d8:c0:9d:bf:df:33:91:b6:8f:9f:bf:b1:21:4b:37:b8:9c:35:84:d4:89:47:89:63:6c:5b:b9:e7:b1:f0:bc:91:c2:08:d1:a2:23:1f:f5:13:a4:f4:cb:83:02:30:78:5d:c5:35:4a:a4:25:f0:26:81:94:1d:26:4b:35:1e:0e:46:47:e6:d8:65:3a:01:bc:2a:96:4d:e3:d8:a3:9d:9d:c4:b3:02:32:18:fd:5f:6c:0b:de:44:99:d3:f5:fe:65:6f:8f:58:23:23:c6:67:36:a8:cd:30:1a:72:ab:c1:63:03:1d:e1:58:b2:97:6e:62:83:e6:16:4a:4f:82:38:c9:aa:bb:68:5d:89:8c:ea:bf:e8:23:9e:db:8d:cf:c5:97:1b:c7:2e:a8:b1:51:4a:98:04:34:a7:99:78:f1:10:82:02:46:bd:1e:8d:07:4b:d5:70:5f:80:4e:7a:11:5a:d6:95:65:4f:65:33:42:c6:48:bc:db:5f:10:23:db:59:46:98:6d:8a:1c:81:41:65:3a:48:bb:45:fb:a6:ce:d5:4b:4c:87:b2:11:dc:3d:23:9f:3b:97:b9:b0:7d:99:36:60:b3:d5:1f:66:bc:65:53:b9:63:ca:5e:8c:4d:66:42:ae:67:21:a9:e0:ea:18:2d:c2:87:7f:09:36:a6:c6:6d:4e:7f:62:1f:7a:2e:93:10:cf:7f:91:8a:fc:b6:e4:67:61:1f:ed:2d:ac:8f:1d:5b:0c:2e:d6:86:75:a8:59:5d:36:e5:4e:9c:f4:6e:2c:88:ad:9e:48:da:94:72:b1:c2:cf:27:da:28:0a:1e:f1:b0:90:e7:63:9a:2d:cc:61:2b:aa:93:50:cd:0e:0b:97:ff:c5:f6:a9:10:b0:15:af:c1:75:a8:ef:af:37:6d:0a:c2:21:2a:0c:b5:18:6d:70:d9:1e:91:3f:4f:66:5c:b8:7f:2f:e7:d5:63:52:36:fa:3e:3f:99:55:76:8f:24:20:ba:64:0e:93:34:08:65:44:13:dd:8b:80:93:50:b2:75:3b:07:1a:9f:20:d9:05:05:e8:07:d8:0f:0d:18:a3:8b:3c:fa:51:24:d0:28:98:ff:94:64'


es = Elasticsearch('10.0.19.112:9200')
s = Search(using=es, index=INDEX_packet)
s = s[0:10000]
q = Q('match_phrase', layers__kerberos_cipher = cipher) & Q('match_phrase', indicator = 'normal')
s1 = s.query(q)
response = s1.execute()

print(response)