import re
import Mainbot.subpackage.bot_questions as bot
import Mainbot.subpackage.ChatbotWorkings as cb
# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
def parse_bot_commands(slack_events,starterbot_id):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    try:
        matches = re.search(MENTION_REGEX, message_text)
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)
    except:
        return None


def handle_command(command, channel,slack_client):
    """
        Executes bot command if the command is known
    """
    try:
        response = None
        # This is where you start to implement more commands!
        if command.startswith(EXAMPLE_COMMAND):
            response = "Sure...write some more code then I can do that!"
        elif response==None:
            response=bot.questions(command)
        if response==[]: 
            a = [] 
            a.append(command)
            robo = cb.AbortGreet(a)
            response = robo.greeting()
    except:
            resppnse=None
    try:
        
        # Sends the response back to the channel
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )
        return response, channel
    except:
        return None