import requests, argparse

def after_date():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="paste the project ID as the first argument")
    parser.add_argument("timestamp", help="paste the project ID as the first argument")
    parser.add_argument("token", help="paste your Optimizely v2 REST API token as the second argument")
    args = parser.parse_args()
    project_id = args.project_id
    token = args.token
    timestamp = args.timestamp

    experiment_list = requests.get("https://api.optimizely.com/v2/experiments?project_id=%s" % project_id, headers={'Authorization': 'Bearer %s' % token})

    if experiment_list.status_code == 200:
        for exp in experiment_list.json():
           if exp['created'] > str(timestamp):
                print(exp['name'], exp['id'])

after_date()
