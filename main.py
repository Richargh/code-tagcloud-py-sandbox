#!/usr/bin/env python
"""
Code Tag Cloud
===============

Generates a tag cloud from a source code folder
"""


import sys
import os
import argparse

from draw_code_tag_cloud import draw_java_tag_cloud, name_cloud, type_cloud, behavior_cloud, all_cloud, \
    draw_csharp_tag_cloud, draw_kotlin_tag_cloud, draw_js_tag_cloud, draw_ts_tag_cloud


def main(folder: str, code_type: str, cloud_type: str, exclude_tags: list[str]):
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

    print(f"Ignoring {len(exclude_tags)} tags. First are {exclude_tags[:5]}")

    if code_type == "java":
        draw_java_tag_cloud(folder, token_types, set(exclude_tags), True)
    elif code_type == "kotlin":
        draw_kotlin_tag_cloud(folder, token_types, set(exclude_tags), True)
    elif code_type == "csharp":
        draw_csharp_tag_cloud(folder, token_types, set(exclude_tags), True)
    elif code_type == "js":
        draw_js_tag_cloud(folder, token_types, set(exclude_tags), True)
    elif code_type == "ts":
        draw_ts_tag_cloud(folder, token_types, set(exclude_tags), True)
    else:
        print(f"Code type {code_type} not recognized. Defaulting to java.")
        draw_java_tag_cloud(folder, token_types, set(exclude_tags), True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Tag Cloud from Code",
        add_help=True)

    parser.add_argument('folder',
                        type=str,
                        help='the folder to parse')
    parser.add_argument('code_type',
                        choices=['java', 'kotlin', 'csharp', 'js', 'ts'],
                        help='the type of the code to parse')
    parser.add_argument('syntax_type',
                        choices=['all', 'name', 'type', 'behavior'],
                        help='What syntax to consider for the tag cloud')
    parser.add_argument('-e', '--exclude',
                        type=str,
                        help='What tags to exclude from the cloud')
    # parser.add_argument("-h", "--help", help="show help", required=False, default="")

    args = parser.parse_args()

    if args.syntax_type is None:
        print(f"Three arguments expected, got less")
        parser.print_help()
        raise SystemExit(2)

    exclude = args.exclude.split(" ") if args.exclude is not None else []
    main(args.folder, args.code_type, args.syntax_type, exclude)
