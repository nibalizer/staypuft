

import re

def search_and_respond(bot, user, channel, msg, config):
    pattern = re.compile('GOZ-\d+')
    results = pattern.findall(msg)
    bot.logger.log("gerrit_hp {0}".format(results))
    for i in results:
        bot.msg(channel, make_jira_url(i))


def make_jira_url(change):
    return "https://jira.hpcloud.net/browse/{0}".format(change)


