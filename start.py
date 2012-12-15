#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import tweepy
import re
from pit import Pit

OYASUMI_LIST = [
    "おやすみ",
    "寝る",
    "おや",
    "(^o^)ﾉ ＜ おやすみー",
    "おやー"
    ]
OYASUMI_RE = re.compile("|".join(OYASUMI_LIST))

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        
        try:
            if (OYASUMI_RE.search(status.text)):
                out =  u"%s\t%s\t%s\t%s" % (status.text,
                                            status.author.screen_name,
                                            status.created_at,
                                            status.source,)
                #print status.author.lang
                print out
                
        except Exception, e:
            print >> sys.stderr, 'Encounted Exception:', e
            pass
        
    def on_error(self, status_code):
        
        print >> sys.stderr, 'Encounted Exception with status code:', status_code
        return True
    
    def on_timeout(self):
        
        print >> sys.stderr, 'Timeout...'
        return True

        
def main():
    conf   = Pit.get('twitter')
    consumer_key   = conf['consumer_key']
    consumer_secret = conf['consumer_secret']
    access_key = conf['access_token']
    access_secret = conf['access_token_secret']
    
    # create OAuth handler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access token to OAuth handler
    auth.set_access_token(access_key, access_secret)
    
    stream = tweepy.Stream(auth, StreamListener())
    stream.sample()
    
if __name__ == "__main__":
    main()
