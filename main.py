#!/usr/bin/env python
"""
Code Tag Cloud
===============

Generates a tag cloud from a source code folder
"""


import sys
import os

from draw_code_tag_cloud import draw_java_tag_cloud, name_cloud, type_cloud, behavior_cloud, all_cloud, \
    draw_csharp_tag_cloud, draw_kotlin_tag_cloud, draw_js_tag_cloud, draw_ts_tag_cloud


def main(folder: str, code_type: str, cloud_type: str):
    if not os.path.exists(folder):
        sys.stderr.write(f"Folder {folder} does not exist")
        exit(-1)

    if cloud_type == "all":
        token_types = all_cloud()
    elif cloud_type == "name":
        token_types = name_cloud()
    elif cloud_type == "type":
        token_types = type_cloud()
    elif cloud_type == "behavior":
        token_types = behavior_cloud()
    else:
        print(f"Cloud Type {cloud_type} not recognized. Defaulting to 'all'.")
        token_types = all_cloud()

    if code_type == "java":
        draw_java_tag_cloud(folder, token_types, True)
    elif code_type == "kotlin":
        draw_kotlin_tag_cloud(folder, token_types, True)
    elif code_type == "csharp":
        draw_csharp_tag_cloud(folder, token_types, True)
    elif code_type == "js":
        draw_js_tag_cloud(folder, token_types, True)
    elif code_type == "ts":
        draw_ts_tag_cloud(folder, token_types, True)
    else:
        print(f"Code type {code_type} not recognized. Defaulting to java.")
        draw_java_tag_cloud(folder, token_types, True)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.stderr.write(f"""
        Please pass: folder_to_parse code_type(=java) and word_cloud_type(all | name | type | behavior)
        """)
        exit(-1)

    _, folder_arg, code_type_arg, cloud_type_arg = sys.argv
    main(folder_arg, code_type_arg, cloud_type_arg)
