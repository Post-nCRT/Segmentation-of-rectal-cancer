import json
with open('H:\\dataset.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)

for j in range(1,3062):
    x={'image':'./imagesTr/colon_%04d'%j+'.nii.gz','label':'./labelsTr/colon_%04d'%j+'.nii.gz'}
    json_data["training"].append(x)


with open('H:\\dataset.json',"w") as f:
     json.dump(json_data,f)
