import unittest

from pygments.lexers.javascript import TypeScriptLexer

from draw_code_tag_cloud import name_cloud, type_cloud, behavior_cloud
from extract_code_tags import extract_code_tags


class ExtractJavascriptTagsTest(unittest.TestCase):
    lexer = TypeScriptLexer()

    def test_extracts_js_object_names(self):
        # given
        source_code = """
        const authorId = {
            rawValue: rawValue
        };
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId", "RawValue"], result)

    def test_extracts_js_object_shorthand_names(self):
        # given
        source_code = """
        const authorId = {
            rawValue
        };
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId", "RawValue"], result)

    def test_extracts_js_class_names(self):
        # given
        source_code = """
        class AuthorId {
            constructor(rawValue){
                this.#rawValue = rawValue;
            }
        }
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        expected = ["AuthorId", "RawValue", "RawValue", "RawValue"]
        self.assertEqual(expected, result)

    def test_extracts_js_class_function_behavior(self):
        # given
        source_code = """
        class Author {
            
            constructor(id, name){
                this.#id = id;
                this.#name = name;
            }
        
            greet(other){
                return `Hi ${other} I'm ${name}`;
            } 
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        # TODO js-related pygments bug, function name considered Name.Other
        self.assertEqual([], result)

    def test_extracts_js_class_lambda_behavior(self):
        # given
        source_code = """
        class Author {

            constructor(id, name){
                this.#id = id;
                this.#name = name;
            }

            greet = (other) => `Hi ${other} I'm ${name}`;
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        # TODO js-related pygments bug, function name considered Name.Other
        self.assertEqual([], result)
