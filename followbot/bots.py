from followbot.models import *
import tweepy, time, logging, pytz
from random import randint, choice
from datetime import datetime

main_account = MainAccount.objects.all().first().twitter_account

def get_POST_accounts():
	accounts = []
	for k in APIkeys.objects.filter(twitter_account=main_account):
		auth = tweepy.OAuthHandler(k.consumer_key, k.consumer_secret)
		auth.set_access_token(k.access_token, k.access_token_secret)
		auth1 = tweepy.auth.OAuthHandler(k.consumer_key, k.consumer_secret)
		auth1.set_access_token(k.access_token, k.access_token_secret)
		api = tweepy.API(auth1)
		accounts.append(api)
	return accounts

def get_GET_accounts():
	accounts = []
	for k in APIkeys.objects.all().exclude(twitter_account=main_account):
		auth = tweepy.OAuthHandler(k.consumer_key, k.consumer_secret)
		auth.set_access_token(k.access_token, k.access_token_secret)
		auth1 = tweepy.auth.OAuthHandler(k.consumer_key, k.consumer_secret)
		auth1.set_access_token(k.access_token, k.access_token_secret)
		api = tweepy.API(auth1)
		accounts.append(api)
	return accounts

def get_all_accounts():
	accounts = []
	for k in APIkeys.objects.all():
		auth = tweepy.OAuthHandler(k.consumer_key, k.consumer_secret)
		auth.set_access_token(k.access_token, k.access_token_secret)
		auth1 = tweepy.auth.OAuthHandler(k.consumer_key, k.consumer_secret)
		auth1.set_access_token(k.access_token, k.access_token_secret)
		api = tweepy.API(auth1)
		accounts.append(api)
	return accounts


class FindPotentialFriends:

	def get_followers(self):
		self.posts = get_POST_accounts()
		self.gets = get_GET_accounts()
		self.all = get_all_accounts()
		self.users = []
		counter = 0
		for account in TwitterAccounts.objects.filter(active=True):
			for page in tweepy.Cursor(choice(self.all).followers, screen_name=account.screen_name).pages():
			    # t = (page, account.screen_name)

			    counter += 1
			    print 'page #', counter
			    for user in page:
					print user.screen_name, user.id
					fl, created = FriendList.objects.get_or_create(screen_name=user.screen_name, user_id=user.id)
					fl.follower_of = account.screen_name
					fl.save()
			    time.sleep(randint(61,72)) # needs to be 60 at least to dodge rate limits


		# print self.users
	

	# def save_follower_list(self):
	# 	# print self.users, 2
	# 	for user in self.users:
	# 		print user.screen_name, user.id
	# 		fl, created = FriendList.objects.get_or_create(screen_name=user.screen_name, user_id=user.id)
	# 		fl.follower_of = self.screen_name
	# 		fl.save()


class MakeFriends:

	def filter_candidates(self):
		print 'started'
		self.follow_list = []
		candidates = FriendList.objects.all().order_by('added_on')		
		for user in candidates:
			if len(Friends.objects.filter(user_id=user.user_id)) == 0 and len(NoLongerFriends.objects.filter(user_id=user.user_id)) == 0:
				self.follow_list.append(user)
		print len(self.follow_list)

	def befriend_candidates(self):
		self.posts = get_POST_accounts()
		self.gets = get_GET_accounts()
		new_follows = 0
		for user in self.follow_list[:randint(290,320)]:
			# check if user has a default profile image
			print user.screen_name
			try:
				c = choice(self.gets)
				usercheck = c.get_user(user_id=user.user_id)
				if not 'default_profile' in usercheck.profile_image_url:
					# make friends
					try:
						u = choice(self.posts).create_friendship(user_id=user.user_id)
						print 'friends with ', user.screen_name
					except:
						# already following

						u = None 
					if u:
						try:
							f = Friends.objects.create(user_id=user.user_id, screen_name=user.screen_name, follower_of=user.follower_of)
							f.save()
							new_follows += 1
							print "new friend #", new_follows, user.screen_name
						except:
							print 'Unable to save', user.screen_name, 'to Friend Table'
				user.delete()
				time.sleep(randint(61,70))
			except Exception as e:
				print e
				print "screen_name:", user.screen_name, "; key: ", c
		print "New friends made:", new_follows


class FriendShipChecker:

	def timecheck(self):
		self.unfriend_candidates = []
		# check how long since user added
		for friend in Friends.objects.filter(friend=False).order_by('followed_on'):
			u=datetime.utcnow()
			u=u.replace(tzinfo=pytz.utc)
			d = u - friend.followed_on.replace(tzinfo=pytz.utc)
			# print d
			# print d.days
			if d.days >= 5:
				self.unfriend_candidates.append(friend)

	def friend_or_unfriend(self):
		self.posts = get_POST_accounts()
		self.gets = get_GET_accounts()
		self.new_friends = 0
		self.no_longer_friends = 0
		for friend in self.unfriend_candidates[:randint(290,320)]:
			try:
				u = choice(self.gets).show_friendship(source_screen_name=friend.screen_name, target_screen_name=main_account)
				if u[0].following:
					# we're friends!
					friend.friend = True
					friend.save()
					self.new_friends += 1
				else:
					# unfriend
					# time.sleep(randint(55,143))
					try:
						choice(self.posts).destroy_friendship(user_id=friend.user_id)
						unfriend = True
					except:
						print 'Problem unfriending', friend.screen_name
						unfriend = False
					if unfriend:
						try:
							nlf, created = NoLongerFriends.objects.get_or_create(screen_name=friend.screen_name, user_id=friend.user_id)
							nlf.follower_of = friend.follower_of
							nlf.save()
							friend.delete()
							self.no_longer_friends += 1
						except Exception as e:
							print e
							# logging.error('Error creationg NoLongerFriends object', friend.screen_name)
			except Exception as e:
				print e

			time.sleep(randint(61,70))
		print "New Friends:", self.new_friends
		print "Friends removed", self.no_longer_friends

















