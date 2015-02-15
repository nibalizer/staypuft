
import requests
latest_type_ref = 'https://raw.githubusercontent.com/puppetlabs/puppet-docs/master/source/references/3.7.4/type.json'


def puppet_type_ref(bot, user, channel, msg, config):
    """  prefix is 'puppettype puppet type file"""
    r = requests.get(latest_type_ref)
    print msg
    words = msg.split(' ')
    print words[3]
    puppet_type = words[3]
    
    puppet_type_description = r.json()[puppet_type]['description'].replace('\n', ' ')[:512].encode('ascii','ignore')
    bot.msg(channel, puppet_type_description)
    parameters = r.json()[puppet_type]['attributes'].keys()
    params = [i.encode('ascii', 'ignore') for i in parameters]
    type_parameters = "Parameters: {0}".format(",".join(params))
    bot.msg(channel, type_parameters)


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
    puppet_type_ref(bot, 'nibalizer', '#ghostbusters', '{0}'.format(sys.argv[1]), config)


