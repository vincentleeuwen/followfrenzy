from followbot.models import *
from django.contrib.admin import ModelAdmin, site


class TwitterAccountsAdmin(ModelAdmin):
	list_display = ('screen_name', 'active' ,'added_on')
	ordering = ('added_on',)

class FriendListAdmin(ModelAdmin):
	list_display = ('screen_name', 'user_id' ,'added_on', 'follower_of')
	ordering = ('added_on',)
	list_filter = ('follower_of',)

class FriendsAdmin(ModelAdmin):
	list_display = ('screen_name', 'user_id', 'followed_on', 'follower_of', 'friend')
	ordering = ('-followed_on',)
	list_filter = ('friend', 'follower_of')

class NoLongerFriendsAdmin(ModelAdmin):
	list_display = ('screen_name', 'user_id', 'unfollowed_on', 'follower_of')
	ordering = ('-unfollowed_on',)

class APIkeysAdmin(ModelAdmin):
	list_display = ('twitter_account',)

class MainAccountAdmin(ModelAdmin):
	list_display = ('twitter_account',)

site.register(TwitterAccounts, TwitterAccountsAdmin)
site.register(FriendList, FriendListAdmin)
site.register(Friends, FriendsAdmin)
site.register(NoLongerFriends, NoLongerFriendsAdmin)
site.register(APIkeys, APIkeysAdmin)
site.register(MainAccount, MainAccountAdmin)