# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NoLongerFriends.followed_on'
        db.delete_column(u'followbot_nolongerfriends', 'followed_on')

        # Adding field 'NoLongerFriends.unfollowed_on'
        db.add_column(u'followbot_nolongerfriends', 'unfollowed_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'NoLongerFriends.followed_on'
        db.add_column(u'followbot_nolongerfriends', 'followed_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'NoLongerFriends.unfollowed_on'
        db.delete_column(u'followbot_nolongerfriends', 'unfollowed_on')


    models = {
        u'followbot.apikeys': {
            'Meta': {'object_name': 'APIkeys'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumer_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_api': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'twitter_account': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'followbot.friendlist': {
            'Meta': {'object_name': 'FriendList'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'follower_of': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        },
        u'followbot.friends': {
            'Meta': {'object_name': 'Friends'},
            'followed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'follower_of': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'friend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        },
        u'followbot.nolongerfriends': {
            'Meta': {'object_name': 'NoLongerFriends'},
            'follower_of': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unfollowed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        },
        u'followbot.twitteraccounts': {
            'Meta': {'object_name': 'TwitterAccounts'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['followbot']