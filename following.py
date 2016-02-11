import argparse

import tweepy

import config as cf

auth = tweepy.OAuthHandler(cf.CONSUMER_KEY, cf.CONSUMER_SECRET)
auth.set_access_token(cf.ACCESS_TOKEN, cf.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def get_following_accounts_url(user_name, output_path=None):
    following_ids = api.friends_ids(user_name)
    user_lookup_limit = 100
    followings = list()
    for i in xrange(0, len(following_ids), user_lookup_limit):
        followings += api.lookup_users(
                user_ids=following_ids[i: i + user_lookup_limit])
    followings_account_urls = ["https://twitter.com/%s" % user.screen_name
                               for user in followings]
    if output_path is None:
        for url in followings_account_urls:
            print url
    else:
        with open(output_path, 'w') as f:
            f.write("\n".join(followings_account_urls))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Get a list of twitter following accounts...")
    parser.add_argument(
            "user_name",
            type=str,
            help="Name of the user you want to get the following accounts")
    parser.add_argument("--output_path", type=str, default=None)
    args = parser.parse_args()
    args = vars(args)

    get_following_accounts_url(**args)
