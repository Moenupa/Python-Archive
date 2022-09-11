#!/bin/python
import json

def stringify(filepath):
    '''
    Give a filepath and return a json-string
    Sample Input: 
    [[0,0,0],[0,0,0]]
    [[0,0,0],[0,0,0]]
    '''
    with open(filepath) as fp:
        lines=fp.read().splitlines()
        string = "{\"frames\":["+",".join(lines)+"]}"
        return string

def post_process(string, camera_angle_x = 0):
    data_list = json.loads(string)["frames"] # a list
    out = { "camera_angle_x": camera_angle_x,"frames": [] }
    for i in range(len(data_list)):
        new_obj = {
            "file_path": "./train/"+format(i, "04")+"_shot.png",
            "rotation": 0.6,
            "transform_matrix": data_list[i]
        }
        out["frames"].append(new_obj)
    with open("out.json", "w") as fp:
        json.dump(out, fp, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    post_process(stringify("src.json"), 0)