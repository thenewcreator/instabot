 #importing package which download the data from given url and importing request package

import requests, urllib

# import Textblob for semantic analysis of a sentence
from textblob import TextBlob


from textblob.sentiments import NaiveBayesAnalyzer

#to find the images of disaster hit places
from disaster import result,media

#my access token
APP_ACCESS_TOKEN = '1788144271.8935d8e.ff497546819c4b8caa1b8a3d7fd7aeec'

 # instagram base url
BASE_URL = 'https://api.instagram.com/v1/'

'''
to retreive and display the information of self
'''


def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)       # fetching data from instagram using "user/self" end point
    print 'GET request url : %s' % (request_url)     #  display the GET url
    user_info = requests.get(request_url).json()      #get the data from the url above mentioned using requests package and json()

    if user_info['meta']['code'] == 200:          #checks the status code of request. if 200 then accepted otherwise the else part will work
        if len(user_info['data']):                  #checking if we have anything in data of user
            print 'Username: %s' % (user_info['data']['username'])               #prints id
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])   #prints no of followers
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])   #prints no of users i am following
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])   #prints no of posts
        else:
            print 'User does not exist!'    #invalid user name
    else:
        print 'Status code other than 200 received!'


'''
get the ID of a user by username
'''


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)   #searching id from instagram using "user/search" end point
    print 'GET request url : %s' % (request_url)     #display the GET url
    user_info = requests.get(request_url).json()        # get the data from the url above mentioned using requests package and using json()

    if user_info['meta']['code'] ==200:      #checks request
        if len(user_info['data']):             #checks data
            return user_info['data'][0]['id']  #stores the id in id variable
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


'''
 get the info of a user by username
'''


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)  #get user id
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)  #fetches recent media of the user
    print 'GET request url : %s' % (request_url)      #prints get url
    user_info = requests.get(request_url).json()      # get the data from the url above mentioned using requests package and using json()

    if user_info['meta']['code'] == 200:       #checks status code of request
        if len(user_info['data']):        #checks data of friends
            print 'Username: %s' % (user_info['data']['username'])     #prints username
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by']) #prints no of followers of the user
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])    #prints no of people following
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])    #prints no of posts
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


'''
Function to get your recent post
'''


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)      #requests url of recent media
    print 'GET request url : %s' % (request_url)    #get url
    own_media = requests.get(request_url).json()      #get the url from above data using request and json

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):   #checks the data
            image_name = own_media['data'][0]['id'] + '.jpeg'    #fetching post id from data and storing it in image_name
            image_url = own_media['data'][0]['images']['standard_resolution']['url']      #getting url of post and storing in image_url
            urllib.urlretrieve(image_url, image_name)  #retriving the image from image_url and saving in image_name with jpeg extension
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


'''
Function to get the recent post of a user by username
'''


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)      # calling get_user_id() fucntion and getting insta id
    if user_id == None:
        print 'User does not exist!'       #prints if user id is none
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)  #getting users list of media
    print 'GET request url : %s' % (request_url) #prints get url
    user_media = requests.get(request_url).json()  #get the data from the url above mentioned using requests package and using json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):  #checks the data
            image_name = user_media['data'][0]['id'] + '.jpeg'   #fetching post id from data and storing it in image_name
            image_url = user_media['data'][0]['images']['standard_resolution']['url'] #getting url of post and storing in image_url
            urllib.urlretrieve(image_url, image_name) #retriving the image from image_url and saving in image_name
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to get the ID of the recent post of a user by username
'''

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)   #calling get_user_id() fucntion
    if user_id == None:
        print 'User does not exist!'  #if user_id is none
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)   #fetches nedia
    print 'GET request url : %s' % (request_url)   #prints get_url
    user_media = requests.get(request_url).json()   #get the data from the url above mentioned using requests package and using json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):  #checks data
            return user_media['data'][0]['id']   #return user media and store it in id
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()



'''
Function to like the recent post of a user
'''


def get_like_list(insta_username):
    media_id = get_post_id(insta_username)   #calls get_post_id and store it in media_id
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)   #requests url to like the post
    payload = {"access_token": APP_ACCESS_TOKEN}   # payload as a dictionary
    print 'POST request url : %s' % (request_url)  # display the POST url
    post_a_like = requests.post(request_url, payload).json()   #posting  the data to the url above mentioned using requests package and using json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'


'''
Function to make a comment on the recent post of the user
'''


def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)  #calls get_post and store it in media_id
    comment_text = raw_input("Your comment: ")  #to comment
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}   #creating payload dictionary as passing accesstoken and comment text in it
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)   #requests url
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

'''
Function to delete negative comments from the recent post
'''

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)  #calls get_post_id and store it in media_id
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)  #requests url
    print 'GET request url : %s' % (request_url)   #print get url
    comment_info = requests.get(request_url).json()    #posting the data of the url above mentioned using requests package and using json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
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


def start_bot():  #contain various menu options
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get a list of people who have liked the recent post of a user\n"
        print "f.Like the recent post of a user\n"
        print "g.Get a list of comments on the recent post of a user\n"
        print "h.Make a comment on the recent post of a user\n"
        print "i.Delete negative comments from the recent post of a user\n"
        print "j.Exit"

#calls the function according to the choices
        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="e":
           insta_username = raw_input("Enter the username of the user: ")
           get_like_list(insta_username)
        elif choice=="f":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="g":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="h":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="i":
           insta_username = raw_input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot() #recalls the start_bot