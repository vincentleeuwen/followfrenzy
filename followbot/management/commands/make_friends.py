from django.core.management.base import BaseCommand, CommandError
from followbot import bots
import time
from random import randint

class Command(BaseCommand):
  help = 'Eerste command'

  def handle(self, *args, **options):
	time.sleep(randint(23, 257))
	print 'Making friends started...'
	mkf = bots.MakeFriends()
	mkf.filter_candidates()
	mkf.befriend_candidates()