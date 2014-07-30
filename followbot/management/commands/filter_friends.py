from django.core.management.base import BaseCommand, CommandError
from followbot import bots
import time
from random import randint

class Command(BaseCommand):
  help = 'Eerste command'
 
  def handle(self, *args, **options):
	time.sleep(randint(24, 299))
	print 'Filtering friends started...'
	fsc = bots.FriendShipChecker()
	fsc.timecheck()
	# fb.save_follower_list()
	fsc.friend_or_unfriend()
