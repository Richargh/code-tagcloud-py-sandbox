import glob
import os.path

from pygments.token import Token
import progressbar


def extract_folder_tags(folder: str, glob_pattern: str, extractor) -> list[str]:
    result = []

    file_paths = glob.glob(folder + glob_pattern, recursive=True)
    for file_path in progressbar.progressbar(file_paths):
        tags = extract_file_tags(file_path, extractor)
        if len(tags) > 0:
            result.extend(tags)

    return result


def extract_file_tags(file_path, extractor):
    result = []
    # print(f"{file_path}")
    if os.path.isfile(file_path):
        with open(file_path) as source_code_file:
            source_code = source_code_file.read()
            result.extend(extractor(source_code))

    return result


def extract_code_tags(lexer, token_types: set[Token], excluded_tokens: set[str], source_code: str) -> list[str]:
    result = []
    for token_type, tokens in lexer.get_tokens(source_code):
        # print(f"  [{token_type}] {tokens}")
        if token_type in token_types:
            prepared_token = (tokens[0].upper() + tokens[1:]).strip()
            if prepared_token not in excluded_tokens:
                result.append(prepared_token)
    return result
