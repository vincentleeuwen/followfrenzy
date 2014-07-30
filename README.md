There are a few basic steps to get the harvestbot going.

Make sure to populate the following database fields via Admin: (after setting up the project on a server and migrating followbot)

1. TwitterAccounts
These are the accounts that provide the followers we're going to follow. For instance, the account of a competitor or some field expert. Make sure you only put one in as being "active"

2. MainAccount
The main account that's beneficiary of the bot. THIS CAN ONLY BE ONE ACCOUNT. 

3. APIKeys
These are the API keys that will be used to make POST and GET requests to the Twitter API. Be sure to include API keys for the account listed under MainAccount. It is also recommended to include a few API keys that belong to other accounts. This makes it less likely to be spotted as a farm and get your account blocked.

After that, use the following management commands to get started:

4. Run `./manage.py scout_friends` to fill up your `friend_list` table with potential followees.

5. Then put daily cron tabs on `./manage.py make_friends` (creating friendships via POST) and `./manage.py filter_friends` (destroying friendships via POST if they don't follow back within 5 days).


That's all. Happy harvesting!