from instagram.client import InstagramAPI

api =InstagramAPI(client_secret=settings.CLIENT_SECRET,
                   access_token=settings.ACCESS_TOKEN)

result = api.tag_recent_media(tag_name='naturalcalamity')
media = result[0]

for m in media:
    print (m.images)
    print (m.user)
    print (m.tags)