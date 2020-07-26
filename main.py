#!/usr/bin/python3
# coding=utf-8
import requests
import time
import json
import sys
import os
from wps import *



# 解决https访问警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

def _wps_checkin(data):
    sid = data['wps_checkin']

    print("\n            ===模拟[我的wps小程序]签到===")
    for item in sid:
        print("\n    为{}签到---↓".format(item['name']))
        wps_clockin(item['sid'])


def _wps_invite(data):
    
    wps_inv = data['wps_invite']

    print("\n\n            ===邀请僵尸账号获得额外会员=== ")
    for item in wps_inv:
        print("    为{}邀请---↓".format(item['name']))
        wps_invite(sid=[], invite_userid=item['invite_userid'])

def _docer_checkin(data):
    sid = data['wps_checkin']
    print("\n            ===模拟[稻壳会员]签到===")
    for item in sid:
        print("    为{}签到---↓".format(item['name']))
        docer_checkin(item['sid'])




if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    print("--------------------------"+now+"----------------------------")
    """ root_dir = os.path.split(os.path.realpath(__file__))[0]
    f = open(root_dir+'/data.json', 'r', encoding="utf8") """
    data = {
    "wps_checkin": [
        {
            "name": "user1",
            "sid": "V02SdInIkwdIV0Ff-4kGKgiu5H4DQlo00a89062a001f1dbca2"
        }
    ],
    "wps_invite": [
        {
            "name": "user1",
            "invite_userid": 522042530,
            "sid": [ ]
        }
    ]

    }
    # f.close()

    _wps_checkin(data)
    _wps_invite(data)
    #_docer_checkin(data)
