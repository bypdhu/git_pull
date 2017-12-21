
#gitpull usage

## health
```
   GET /health
    
   Response
    {
      "msg": "success"
    }
```

## git pull
```
    POST /gitpull
    Content-Type: application/json
    {
        "basedir": "",  # default: /home/admin/conf/ansible_playbooks/
        "repository", "",  # default: ALL_REPOSITORIES
        "branch", ""
    }

```