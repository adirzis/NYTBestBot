import requests
import json
import random
import tweepy

#this is the API request split up into two parts so I can randomize the date:
req_str_1 = 'https://api.nytimes.com/svc/books/v3/lists/full-overview.json?published_date='

req_str_2='&api-key=gjvXVmI63bDT52fqry3dcS5NTKldqJ0D'

#these are the variables for the date:
years=['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
months=['01','02','03','04','05','06','07','08','09','10','11','12']
days=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']

#here is where I will store the the descriptions:
master_list=[]
part1list=[]
part2list=[]

for y in range (1):

    desc_list1=[]
#this will generate the date and run the event:
    ran_date=random.choice(years)+"-"+random.choice(months)+"-"+random.choice(days)
    response_API = requests.get(req_str_1 + ran_date + req_str_2)
#to make sure everything is working well, I will print the staus code:
    print(response_API.status_code)
    #get bestseller data:
    data = response_API.text
    parse_json = json.loads(data)
    #extract descriptions:
    for x in range(1):
        desc_list1.append(parse_json['results']['lists'][x]['books'][x]['description'])
    #add a random description to list:
    part1list.append(random.choice(desc_list1))
#repeat above process for second half of super description:
for y in range (1):

    desc_list2=[]
    ran_date=random.choice(years)+"-"+random.choice(months)+"-"+random.choice(days)
    response_API = requests.get(req_str_1 + ran_date + req_str_2)
    print(response_API.status_code)
    data = response_API.text

    parse_json = json.loads(data)


    for x in range(1):
        desc_list2.append(parse_json['results']['lists'][x]['books'][x]['description'])

    part2list.append(random.choice(desc_list2))
#if both descriptions have text add them together:
for y in range (1):
    if len(part1list[y]) > 5 and len(part2list[y]) > 5:
        master_list.append(part1list[y] + " "+ part2list[y])

#open file and add super description:
with open ('desc_test.txt','a') as f:
    for z in range (1):
        f.write(master_list[z]+"\n")
f.close()


######TWEET SECTION######

consumer_key = "hdxY4plprkibCJ5zbfrDniXou"
consumer_secret = "eTnNIDvWNkVguK7KikRPGWU9QFIdQilRfnZNTJ76Jwjbm5Ex7Q"
access_token = "1515828885966962692-VSUkZYaZPrwScYPu4grz4ftzat6VIg"
access_token_secret = "X9Icwsd9vGGX9Qj88j3WFcKwTfdoTfqI8gH4Y3bpRZQZ3"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

tweettext = ""

#read the entire file with the super descriptions:
with open ('desc_test.txt','r') as f:
    filetext=f.readlines()
f.close()
#read the first line:
with open ('desc_test.txt','r') as f:
    tweettext= f.read()
    tweettext=tweettext.split('\n',1)[0]
f.close()
#delete the first line of the file:
with open ('desc_test.txt','w') as f:
    f.writelines(filetext[1:])
f.close()

#post tweet and confirm when done:
api.update_status(tweettext)
print("Done")
