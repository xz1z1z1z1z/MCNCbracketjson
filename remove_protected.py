import json


protected_json = dict

with open("./bracket.json.protected", "r", encoding="utf-8") as f:
    protected_json = json.load(f)

for match in protected_json["Matches"]:
    pb_new = []
    
    for pb in match["PicksBans"]:
        if pb["Type"] != "Protected":
            pb_new.append(pb)
    
    match["PicksBans"] = pb_new
    

with open("bracket.json", "w") as outfile:
    json.dump(protected_json, outfile)
