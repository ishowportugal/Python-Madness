import twint 

search  = input ("What are you searching for?")
city =  input ("where?")

c = twint .config()
c.Search = search
C.Near = city
c.Limit = 20
c.Popular_tweets = True

twint.run.search(c)