#Slack Push Notification
''' This script is used to get a Push Notification on Mobile using Slack.'''
import slack
import os
def slack_message(message, filename):
    token = os.environ.get('SLACK_TOKEN')
    sc = slack.WebClient(token)
    sc.chat_postMessage(channel= 'python-notifications',
                        text= '<< ' + os.path.basename(filename) + ' >>\n\n' + message,
                        username= 'Python-Script',
                        icon_emoji= ':sunglasses:')

    print('\n***** SLACK Push Notification Successfully Sent. *****\n')
