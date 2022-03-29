import pip._vendor.requests as requests
import json


def get_names(type_of_robot):
    try:
        url = f"https://cybermoves.herokuapp.com/api/public/allNamesByType?robotType={type_of_robot}"
        res = requests.get(url)
        if res:
            resJson = json.loads(res.text)
            for command in resJson:
                print(command["name"])
    except:
        print("error")


def get_commands(name):
    try:
        url = f"https://cybermoves.herokuapp.com/api/public/commandByName?name={name}"
        res = requests.get(url)
        if res:
            resJson = json.loads(res.text)
            return resJson
    except:
        print("error")
