import json, os, requests
import utils


def post_reports_to_slack():
    global value
    message = ""
    url = "https://hooks.slack.com/services/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"

    test_report_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '.report.json'))  # Add report file name and address here

    summary_json = utils.json_reader(test_report_file)
    # print(summary_json)
    summary = str(summary_json["summary"])
    print(summary)

    if 'failed' in summary:
        bar_color = "#ff0000"
    else:
        bar_color = "#36a64f"

    try:
        slack_message = {
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': ':bomb:* Test Automation Result:*'
                    }
                }
            ],
            "attachments": [
                {"color": bar_color,
                 "title": "Test Report",
                 "text": summary}
            ]
        }

        json_params_encoded = json.dumps(slack_message)
        requests.post(url=url, data=json_params_encoded, headers={"Content-type": "application/json"})

    except Exception as e:
        print(e)


if __name__ == '__main__':
    post_reports_to_slack()
