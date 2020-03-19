import datetime
import json
import pprint
import sys

class NameError(Exception):
    pass


if __name__ == "__main__":

    sample = {
        "--name": None,
        "--deadline": None,
        "--description": None
    }

    data = {}

    if sys.argv[1] == "add":
        for argument in range(2, len(sys.argv)):
            if sys.argv[argument] == "--name":
                sample["--name"] = sys.argv[argument + 1]
            if sys.argv[argument] == '--deadline':
                sample["--deadline"] = sys.argv[argument + 1]
            if sys.argv[argument] == "--description":
                sample["--description"] = sys.argv[argument + 1]
        id_hash = hash(str(sample))
        temp = []
        if sample["--name"] == None:
            raise NameError("Enter the name")
        else:
            try:
                with open("sample.json", "r") as json_file:
                    data = json.load(json_file)

                temp[id_hash] = []
                temp[id_hash].append(sample)

            except:
                data.update({id_hash: sample})
                with open("sample.json", 'w') as outfile:
                    json.dump(data, outfile)

    if sys.argv[1] == "update":
        with open("sample.json", "r") as outfile:
            data = json.load(outfile)
            ident = sys.argv[-1]
            if ident in data:
                for element in data[ident]:
                    for item in range(len(sys.argv)-1):
                        if element == sys.argv[item]:
                            with open("sample.json", "w") as outfile:
                                data[ident][element] = sys.argv[item+1]
                                json.dump(data, outfile)


    if sys.argv[1] == "remove":
        with open("sample.json", "r") as outfile:
            data = json.load(outfile)
            for element in data:
                if sys.argv[2] == element:
                    break
            with open("sample.json", "w") as outfile:
                del (data[element])
                json.dump(data, outfile)


    if sys.argv[1] == "list":
        with open("sample.json", "r") as outfile:
            data = json.load(outfile)
        if sys.argv[2] == "--all":
            for key, value in data.items():
                outputText = 'hash: ' + str(key) + "\n" +\
                             ' name: ' + str(value["--name"]) + "\n" + \
                             ' deadline: ' + str(value["--deadline"]) + "\n" +\
                             ' description: ' + str(value["--description"]) + "\n"

                print(outputText)
        elif sys.argv[2] == "--today":
            for key, value in data.items():
                if value["--deadline"] == datetime.date.today().__str__():
                    outputText = 'hash: ' + str(key) + "\n" + \
                                 ' name: ' + str(value["--name"]) + "\n" + \
                                 ' deadline: ' + str(value["--deadline"]) + "\n" + \
                                 ' description: ' + str(value["--description"]) + "\n"

                    print(outputText)
