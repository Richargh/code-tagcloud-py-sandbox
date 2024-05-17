from functools import partial
from pygments.lexers.jvm import JavaLexer, KotlinLexer
from pygments.lexers.dotnet import CSharpLexer
from pygments.lexers.javascript import TypeScriptLexer
from pygments.token import Token

from draw_tag_cloud import draw_tag_cloud
from extract_code_tags import extract_folder_tags, extract_code_tags


def all_cloud() -> set:
    return {
        Token.Name,
        Token.Name.Other,
        Token.Name.Class,
        Token.Name.Function,
        Token.Name.Attribute,
        Token.Name.Variable,
        Token.Keyword.Type
    }


def name_cloud() -> set:
    return {Token.Name, Token.Name.Other}


def type_cloud() -> set:
    return {Token.Name.Class}


def behavior_cloud() -> set:
    return {Token.Name.Function, Token.Name.Attribute}


def draw_java_tag_cloud(folder: str, token_types: set, exclude_tags: set, show: bool) -> None:
    _draw_code_tag_cloud(
        folder,
        '/**/*.java',
        partial(extract_code_tags, JavaLexer(), token_types, exclude_tags),
        show)


def draw_kotlin_tag_cloud(folder: str, token_types: set, exclude_tags: set, show: bool) -> None:
    _draw_code_tag_cloud(
        folder,
        '/**/*.kt',
        partial(extract_code_tags, KotlinLexer(), token_types, exclude_tags),
        show)


def draw_csharp_tag_cloud(folder: str, token_types: set, exclude_tags: set, show: bool) -> None:
    _draw_code_tag_cloud(
        folder,
        '/**/*.cs',
        partial(extract_code_tags, CSharpLexer(), token_types, exclude_tags),
        show)


def draw_ts_tag_cloud(folder: str, token_types: set, exclude_tags: set, show: bool) -> None:
    _draw_code_tag_cloud(
        folder,
        '/**/*.ts',
        partial(extract_code_tags, TypeScriptLexer(), token_types, exclude_tags),
        show)


def draw_js_tag_cloud(folder: str, token_types: set, exclude_tags: set, show: bool) -> None:
    _draw_code_tag_cloud(
        folder,
        '/**/*.js',
        partial(extract_code_tags, TypeScriptLexer(), token_types, exclude_tags),
        show)


# Java pygments
# (interface, record, class) declaration -> Token.Name.Class
# method declaration -> Token.Name.Function
# method invocation -> Token.Name.Attribute
# (var, public final, class, record, ...) keywords -> Token.Keyword.Declaration
# parameters, parameter types, fields, field types, generic types: Token.Name


def _draw_code_tag_cloud(folder: str, glob_pattern: str, extractor, show: bool) -> None:
    tags = extract_folder_tags(folder, glob_pattern, extractor)
    draw_tag_cloud(tags, show)
