# -*- coding:utf-8 =*- 
# @ Time :2018 /3/20 
# @ File : config.py 
#import configparser 
import config_default

__author__ = 'bill'


def merge(defaults,override):
    r={}
    for k,v in defaults.items():
        if k in override:
            if isinstance(v,dict):
                r[k]=merge(v,override[k])
            else:
                r[k]=override[k]
        else:
            r[k]=v
    return r

configs=config_default.configs
apiUrl=f"/{configs['SETTING']['APINAME']}/api/{configs['SETTING']['VERSION']}"

try:
    import config_override
    configs=merge(configs,config_override.configs)
except ImportError:
    pass


