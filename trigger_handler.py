import re

triggers_available = []

#import triggers.gerrit_hpcloud
#triggers_available.append(triggers.gerrit_hpcloud.search_and_respond)

#import triggers.gozer_jira
#triggers_available.append(triggers.gozer_jira.search_and_respond)


def trigger_handler(bot, user, channel, msg, config):
    stripped_msg = msg.lstrip()

    if channel == bot.nickname:
        channel = user
    for trigger in triggers_available:
        trigger(bot, user, channel, msg, config)




