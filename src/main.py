from preformatting import preformat
from temp_data import temp_data

if __name__ == "__main__":
    print("running")
    commands = temp_data["commands"]
    print(preformat(commands[1]))
