#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : bianbian
# @Site    : Asia/Shanghai
# @File    : gitlab_response_example.py
# @Software: bianbian's PyCharm
# @Time    : 2018/1/4 17:41

response = \
    {
        "before": "95790bf891e76fee5e1747ab589903a6a1f80f22",
        "after": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
        "ref": "refs/heads/master",
        "user_id": 4,
        "user_name": "John Smith",
        "repository": {
            "name": "Diaspora",
            "url": "git@localhost:diaspora.git",
            "description": "",
            "homepage": "http://localhost/diaspora",
        },
        "commits": [
            {
                "id": "b6568db1bc1dcd7f8b4d5a946b0b91f9dacd7327",
                "message": "Update Catalan translation to e38cb41.",
                "timestamp": "2011-12-12T14:27:31+02:00",
                "url": "http://localhost/diaspora/commits/b6568db1bc1dcd7f8b4d5a946b0b91f9dacd7327",
                "author": {
                    "name": "Jordi Mallach",
                    "email": "jordi@softcatala.org",
                }
            },
            {
                "id": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                "message": "fixed readme",
                "timestamp": "2012-01-03T23:36:29+02:00",
                "url": "http://localhost/diaspora/commits/da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                "author": {
                    "name": "GitLab dev user",
                    "email": "gitlabdev@dv6700.(none)",
                },
            },
        ],
        "total_commits_count": 4,
    }