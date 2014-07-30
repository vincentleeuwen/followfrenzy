# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TwitterAccounts'
        db.create_table(u'followbot_twitteraccounts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'followbot', ['TwitterAccounts'])

        # Adding model 'NoLongerFriends'
        db.create_table(u'followbot_nolongerfriends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('followed_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('follower_of', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'followbot', ['NoLongerFriends'])

        # Adding model 'Friends'
        db.create_table(u'followbot_friends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('followed_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('follower_of', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('friend', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'followbot', ['Friends'])

        # Adding model 'FriendList'
        db.create_table(u'followbot_friendlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('follower_of', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'followbot', ['FriendList'])


    def backwards(self, orm):
        # Deleting model 'TwitterAccounts'
        db.delete_table(u'followbot_twitteraccounts')

        # Deleting model 'NoLongerFriends'
        db.delete_table(u'followbot_nolongerfriends')

        # Deleting model 'Friends'
        db.delete_table(u'followbot_friends')

        # Deleting model 'FriendList'
        db.delete_table(u'followbot_friendlist')


    models = {
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
            'followed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'follower_of': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        },
        u'followbot.twitteraccounts': {
            'Meta': {'object_name': 'TwitterAccounts'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['followbot']