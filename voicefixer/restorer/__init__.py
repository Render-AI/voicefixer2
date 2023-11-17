# import os
# import torch
# import urllib.request
# from cached_path import cached_path

# meta = {
#     "voicefixer_fe": {
#         "path": os.path.join(
#             os.path.expanduser("~"),
#             ".cache/voicefixer/analysis_module/checkpoints/vf.ckpt",
#         ),
#         "url": "https://huggingface.co/voicefixer/voicefixer/resolve/main/model/vf.ckpt?download=true",
#     },
# }

# if not os.path.exists(meta["voicefixer_fe"]["path"]):
#     os.makedirs(os.path.dirname(meta["voicefixer_fe"]["path"]), exist_ok=True)
#     print("Downloading the main structure of voicefixer")

#     urllib.request.urlretrieve(
#         meta["voicefixer_fe"]["url"], meta["voicefixer_fe"]["path"]
#     )
#     print(
#         "Weights downloaded in: {} Size: {}".format(
#             meta["voicefixer_fe"]["path"],
#             os.path.getsize(meta["voicefixer_fe"]["path"]),
#         )
#     )

#     # cmd = "wget "+ meta["voicefixer_fe"]['url'] + " -O " + meta["voicefixer_fe"]['path']
#     # os.system(cmd)
#     # temp = torch.load(meta["voicefixer_fe"]['path'])
#     # torch.save(temp['state_dict'], os.path.join(os.path.expanduser('~'), ".cache/voicefixer/analysis_module/checkpoints/vf.ckpt"))
