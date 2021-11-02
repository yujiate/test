import json
import os
with open("Chase/chase_train.json", "r") as f:
    tmp = json.load(f)
if os.path.exists("utterance.txt"):
    os.remove("utterance.txt")
with open("utterance.txt", "w") as f:
    for j in range(len(tmp)):
        f.write(f"第{j+1}段对话：\n")
        f.write("-" * 200 + "\n")
        for i in range(len(tmp[j]["interaction"])):
            f.write(tmp[j]["interaction"][i]["utterance"] + "\n")
            f.write("schema_linking: ")
            for schema_linking in tmp[j]["interaction"][i]["schema_linking"]:
                if schema_linking["entity"]:
                    f.write(str(schema_linking["entity"]["value"])+" ")
                else:
                    f.write("None")
            f.write("\n")
        f.write("-" * 200 + "\n")
