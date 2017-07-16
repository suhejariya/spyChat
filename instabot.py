# Importing Libraries
import requests, urllib
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt




#Globaly Declared
APP_ACCESS_TOKEN = '5724669034.e13938e.ebe6c8e25e324d89995aef8dec130b9e'

BASE_URL = 'https://api.instagram.com/v1/'





#Function to get your own info

def self_info():
    try:
        request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
        print colored('GET request url : %s','blue') % (request_url)
        user_info = requests.get(request_url).json()

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                print colored('Username: %s','blue') % (user_info['data']['username'])
                pic= user_info['data']['profile_picture']+'.jpeg'
                print colored("profile pic url:%s",'blue')%(pic)
                print colored('full-name: %s', 'blue') % (user_info['data']['full_name'])
                print colored('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
                print colored('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
                print colored('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
            else:
                print colored('User does not exist!!','red')
        else:
            print colored('Status code other than 200 received!','red')
    except:
        print colored("ERROR!",'red')
        exit()




#Function to get the ID of a user by username

def get_user_id(insta_username):
    try:
        request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
        print colored('GET request url : %s','blue') % (request_url)
        user_info = requests.get(request_url).json()

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                return user_info['data'][0]['id']
            else:
                return None
        else:
            print colored('Status code other than 200 received!','red')

    except:
        print colored("ERROR!", 'red')
        exit()





#Function to get the info of a user by username

def get_user_info(insta_username):
    try:
        user_id = get_user_id(insta_username)
        if user_id == None:
            print colored('Instauser Of This Username does not exist!','red')
            exit()
        request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
        print colored('GET request url : %s','blue') % (request_url)
        user_info = requests.get(request_url).json()

        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                print colored('Username: %s','blue') % (user_info['data']['username'])
                print colored('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
                pic = user_info['data']['profile_picture'] + '.jpeg'
                print colored("profile pic url:%s", 'blue') % (pic)
                print colored('full-name: %s', 'blue') % (user_info['data']['full_name'])
                print colored('No. of followers: %s', 'blue') % (user_info['data']['counts']['followed_by'])
                print colored('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
                print colored('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
            else:
                print colored('There is no data exists for this user!','red')
        else:
            print colored('Status code other than 200 received!','red')

    except:
        print colored("ERROR!", 'red')
        exit()



#Function to get your recent post

def get_own_post():
    try:
        request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        own_media = requests.get(request_url).json()

        if own_media['meta']['code'] == 200:
            if len(own_media['data']):
                image_name = own_media['data'][0]['id'] + '.jpeg'
                image_url = own_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print 'Your image has been downloaded!'
            else:
                print 'Post does not exist!'
        else:
            print 'Status code other than 200 received!'
    except:
        print colored("ERROR!", 'red')
        exit()


#Function to get the recent post of a user by username

def get_user_post(insta_username):
    try:
        user_id = get_user_id(insta_username)
        if user_id == None:
            print colored('Instauser Of This Username does not exist!', 'red')
            exit()
        request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
        print colored('GET request url : %s','blue') % (request_url)
        user_media = requests.get(request_url).json()

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                image_name = user_media['data'][0]['id'] + '.jpeg'
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                # Fetching users recent post by passing link to the function as parameter
                print colored('The Image From users Recent Posts has been downloaded!','green')
            else:
                print colored('Post does not exist!', 'red')
        else:
            print colored('Status code other than 200 received!','red')

    except:
        print colored("ERROR!", 'red')
        exit()



#Function declaration to get the ID of the recent post of a user by username

def get_post_id(insta_username):
    try:
        user_id = get_user_id(insta_username)
        if user_id == None:
            print colored('InstaUser of this Username does not exist!','red')
            exit()
        request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
        print colored('GET request url : %s','blue') % (request_url)
        user_media = requests.get(request_url).json()

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                return user_media['data'][0]['id']
            else:
                print colored('There is no recent post of the user!','red')
                exit()
        else:
            print colored('Status code other than 200 received!','red')
    except:
        print colored("ERROR!", 'red')
        exit()




#Function declaration to like the recent post of a user

def like_a_post(insta_username):
    try:
        media_id = get_post_id(insta_username)
        request_url = (BASE_URL + 'media/%s/likes') % (media_id)
        payload = {"access_token": APP_ACCESS_TOKEN}
        print colored('POST request url : %s','blue') % (request_url)
        post_a_like = requests.post(request_url, payload).json()
        if post_a_like['meta']['code'] == 200:
            print colored('Like was successful!','green')
        else:
            print colored('Your like was unsuccessful.Please Try again!','red')
    except:
        print colored("ERROR!", 'red')
        exit()





#Function to Get the like lists on the recent post of a user

def get_like_list(insta_username):
    try:
        media_id = get_post_id(insta_username)
        request_url = BASE_URL + 'media/%s/likes?access_token=%s' % (media_id, APP_ACCESS_TOKEN)
        print colored('GET request url : %s', 'blue') % (request_url)
        like_list = requests.get(request_url).json()

        if like_list['meta']['code'] == 200:
            if len(like_list['data']):
                position = 1
                print colored("List of people who Liked Your Recent post", 'blue')
                for users in like_list['data']:
                    if users['username']!= None:
                        print position, colored(users['username'],'green')
                        position = position + 1
                    else:
                        print colored('No one had liked Your post!', 'red')
            else:
                print colored("User Does not have any post",'red')
        else:
            print colored('Status code other than 200 recieved', 'red')

    except:
        print colored("ERROR!", 'red')
        exit()




#Function to Get the lists of comments on  the recent post of a user

def get_comment_list(insta_username):
    try:
        media_id = get_post_id(insta_username)
        request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (media_id, APP_ACCESS_TOKEN)
        print colored('GET request url : %s', 'blue') % (request_url)
        comment_list = requests.get(request_url).json()

        if comment_list['meta']['code'] == 200:
            if len(comment_list['data']):
                position = 1
                print colored("List of people who commented Your Recent post", 'blue')
                for users in comment_list['data']:
                    if users['username'] != None:
                        print position, colored(users['username'], 'green')
                        position = position + 1
                    else:
                        print colored('No one had commented on Your post!', 'red')
            else:
                print colored("User Does not have any post", 'red')
        else:
            print colored('Status code other than 200 recieved', 'red')

    except:
        print colored("ERROR!", 'red')
        exit()






#Function to make a comment on the recent post of the user


def post_a_comment(insta_username):
    try:
        media_id = get_post_id(insta_username)
        comment_text = raw_input(colored("Please Write Your comment: ",'blue'))
        payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
        request_url = (BASE_URL + 'media/%s/comments') % (media_id)
        print colored('POST request url : %s','blue') % (request_url)

        post_comment = requests.post(request_url, payload).json()
        if post_comment['meta']['code'] == 200:
            print colored("Successfully added a new comment!",'green')
        else:
            print colored("Unable to add comment.Please Try again!!",'red')


    except:
        print colored("ERROR!", 'red')
        exit()


#Function to make delete negative comments from the recent post

def deleting_negative_comments(insta_username):
    try:
        media_id = get_post_id(insta_username)
        request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        comment_info = requests.get(request_url).json()

        if comment_info['meta']['code'] == 200:
            if len(comment_info['data']):
                # Here's a naive implementation of how to delete the negative comments :)
                for x in range(0, len(comment_info['data'])):
                    comment_id = comment_info['data'][x]['id']
                    comment_text = comment_info['data'][x]['text']
                    blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                    if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                        print 'Negative comment : %s' % (comment_text)
                        delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                        media_id, comment_id, APP_ACCESS_TOKEN)
                        print 'DELETE request url : %s' % (delete_url)
                        delete_info = requests.delete(delete_url).json()

                        if delete_info['meta']['code'] == 200:
                            print 'Comment successfully deleted!\n'
                        else:
                            print 'Unable to delete comment!'
                    else:
                        print 'Positive comment : %s\n' % (comment_text)
            else:
                print 'There are no existing comments on the post!'
        else:
            print 'Status code other than 200 received!'
    except:
        print colored("ERROR!", 'red')
        exit()





#Function to get location-id
def location_search():
    try:
        lat=float(raw_input("Enter lat:"))
        lng=float(raw_input("Enter lng:"))
        request_url = (BASE_URL + 'locations/search?lat=%f&lng=%f&access_token=%s') % (lat,lng ,APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        info = requests.get(request_url).json()

        if info['meta']['code'] == 200:
            if len(info['data']):
                return info['data'][0]['id']
            else:
                print "No data found"
        else:
            print 'Status code other than 200 received!'
            print "Status code received:", info['meta']['code']
    except:
        print colored("ERROR!", 'red')
        exit()





#Function to find location name
def location(loc):
    try:
        request_url = (BASE_URL + 'locations/%s?access_token=%s') % (loc, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        info = requests.get(request_url).json()

        if info['meta']['code'] == 200:
            if len(info['data']):
                print "location-name:%s"%(info['data']['name'])
                print "latitude:%f"%(info['data']['latitude'])
                print "longitude:%f"%(info['data']['longitude'])
            else:
                print 'No data found!'
        else:
            print 'Status code other than 200 received!'
            print "Status code received:",info['meta']['code']
    except:
        print colored("ERROR!", 'red')
        exit()






#Defining the Main function under which above sub-function works by calling

def start_bot():
    print colored('Hey! Welcome in instaBot :)', 'blue')
    while True:
        print colored('Select your menu options:','blue')
        print colored("Select Option:'A'  To Get your own details\n",'green')
        print colored("Select Option:'B'  To Get details of a user by username\n",'green')
        print colored("Select Option:'C'  To Get your own recent post\n",'green')
        print colored("Select Option:'D'  To Get the recent post of a user by username\n",'green')
        print colored("Select Option:'E'  To Get a list of people who have liked the recent post of a user\n",'green')
        print colored("Select Option:'F'  To Like the recent post of a user\n",'green')
        print colored("Select Option:'G'  To Get a list of comments on the recent post of a user\n",'green')
        print colored("Select Option:'H'  To Make a comment on the recent post of a user\n",'green')
        print colored("Select Option:'I'  To delete negative comments\n",'green')
        print colored("Select Option:'J'  To find location\n",'green')
        print colored("Select Option:'K'  To Exit\n",'green')

        choice = raw_input(colored("Enter you choice: ",'blue'))
        if choice.upper() == "A":
            self_info()
        elif choice.upper() == "B":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_user_info(insta_username)
        elif choice.upper() == "C":
            get_own_post()
        elif choice.upper() == "D":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_user_post(insta_username)
        elif choice.upper() == "E":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_like_list(insta_username)
        elif choice.upper() == "F":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            like_a_post(insta_username)
        elif choice.upper() == "G":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_comment_list(insta_username)
        elif choice.upper() == "H":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            post_a_comment(insta_username)
        elif choice.upper() == "I":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            deleting_negative_comments(insta_username)
        elif choice.upper() == "J":
            loc=location_search()
            location(loc)
        elif choice.upper()=="K":
            exit()

        else:
            print colored("ERROR:Wrong Choice",'red')





#Calling the main function

start_bot()