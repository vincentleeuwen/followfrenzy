from django.db import models

# Create your models here.
class TwitterAccounts(models.Model):
	screen_name = models.CharField(max_length=100)
	# user_id = models.BigIntegerField(unique=True)
	active = models.BooleanField(default=True)
	added_on = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)

	def __unicode__(self):
		return u'%s' % self.screen_name

class FriendList(models.Model):
	screen_name = models.CharField(max_length=100)
	user_id = models.BigIntegerField(unique=True)
	added_on = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
	follower_of = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return u'%s' % self.screen_name

class Friends(models.Model):
	screen_name = models.CharField(max_length=100)
	user_id = models.BigIntegerField(unique=True)
	followed_on = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
	follower_of = models.CharField(max_length=100, blank=True)
	friend = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s' % self.screen_name

class NoLongerFriends(models.Model):
	screen_name = models.CharField(max_length=100)
	user_id = models.BigIntegerField(unique=True)
	unfollowed_on = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
	follower_of = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return u'%s' % self.screen_name	

class APIkeys(models.Model):
	consumer_key = models.CharField(max_length=100)
	consumer_secret = models.CharField(max_length=100)
	access_token = models.CharField(max_length=100)
	access_token_secret = models.CharField(max_length=100)
	post_api = models.BooleanField(default=True)
	twitter_account = models.CharField(max_length=100, blank=True)

class MainAccount(models.Model):
	twitter_account = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return u'%s' % self.twitter_account	

