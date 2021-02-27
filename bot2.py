# -*- coding: utf-8 -*-
import tweepy
import random


consumer_key = 'rwUd61NPZh6yrIcmbQpQH60zR'
consumer_secret = 'WKQfEY8qhJc9OuBSmK1wVHyFspnfFl52Cf0b5mxTbxrtIAmGmS'

key = '1365469304502812675-DwHAmh0ehliTmcOzjLgvCsPVgrK5H0'
secret = 'o4Sn7tHVkD3HodU6dQSTOkCgqpNhLgxdgnFFQsRXvnfRi'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)








def tweetsend2():
    print("oi")
    public_tweets = api.search(q='jimin -filter:retweets', count=1, geocode="-11.800399,-48.339055,2500km", since="2018-06-09", tweet_mode="extended")
    for tweet in public_tweets:
        print(tweet.full_text)
        print(tweet.user.screen_name)
        print(tweet.user.id)
        recipient_id = tweet.user.id
        text = "Oiiie, você podia por favor ver no meu fixado? Eu to em uma situação complicada de dinheiro, e em uns 30 segundos você poderia me ajudar sem gastar nada, por favor, eu realmente preciso"
        try:
            number = ('1',
            '2',
            '3',

            )
            numberident = (random.choice(number))
            print(numberident)
            numberchance = "2" in numberident
            api.send_direct_message(recipient_id, text)
            if numberchance == True:
                try:
                    api.create_friendship(tweet.user.id)
                except:
                    print("deu erro")
        except:
            pass



while True:
            tweetsend2()
            import time
            time.sleep(160)
