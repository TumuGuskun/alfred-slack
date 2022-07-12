from pprint import pprint
import subprocess
from slack_sdk import WebClient
from dotenv import dotenv_values


def main() -> None:
    env_values = dotenv_values()
    slack_token = env_values.get('SLACK_TOKEN')

    client = WebClient(token=slack_token)

    # for result in client.conversations_list(types='public_channel'):
    #     for channel in result['channels']:
    #         if channel['name'] == 'infra-watercooler':
    #             pprint(channel)
    #             break

    infra_watercooler_id = "C027NLF94TA"
    team_id = 'T03Q236LG'

    slack_url = f'slack://channel?id={infra_watercooler_id}&team={team_id}'
    subprocess.call(['open', '-a', 'Slack', slack_url])


if __name__ == '__main__':
    main()
