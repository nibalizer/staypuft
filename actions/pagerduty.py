
import requests
import datetime


def get_vanguard(bot, user, channel, msg, config):
    get_schedule(bot, user, channel, msg, config, 'P0HJODC')

def get_sentinel(bot, user, channel, msg, config):
    get_schedule(bot, user, channel, msg, config, 'PBQSZ8I')

def get_schedule(bot, user, channel, msg, config, SCHEDULE_ID):
    d = datetime.datetime.now()
    today = "{0}-{1}-{2}".format(d.year,d.month,d.day)
    tomorrow = "{0}-{1}-{2}".format(d.year,d.month,(d.day+1))
    SUBDOMAIN = config.pagerduty_SUBDOMAIN
    API_ACCESS_KEY = config.pagerduty_API_ACCESS_KEY
    url = 'https://{0}.pagerduty.com/api/v1/schedules/{1}/users'.format(SUBDOMAIN, SCHEDULE_ID)
    headers = {
    'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
    'Content-Type': 'application/json',
    }
    params = {
    'since':today,
    'until':tomorrow,
    }
    r = requests.get(url, headers=headers, params=params)
    oncall = [i['name'].encode('ascii', 'ignore') for i in r.json()['users']]
    bot.msg(channel, ", ".join(oncall))


#mock the bot
class mybot():

    def msg(self, chan, resp):
        print resp

#mock the config
class myconfig():
    zuul_status = 'http://zuul.openstack.org/status.json'

if __name__ == "__main__":
    import sys 
    bot = mybot()
    config = myconfig()
    get_vanguard(bot, 'nibalizer', '#ghostbusters', '{0}'.format(sys.argv[1]), config)


