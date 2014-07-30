from django.core.management.base import BaseCommand, CommandError
from followbot import bots
import time
from random import randint


class Command(BaseCommand):
  help = 'Eerste command'

  def handle(self, *args, **options):
	print 'Scouting friends started...'
	fb = bots.FindPotentialFriends()
	fb.get_followers()
	# fb.save_follower_list()
