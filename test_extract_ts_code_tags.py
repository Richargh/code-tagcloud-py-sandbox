import unittest

from pygments.lexers.javascript import TypeScriptLexer

from draw_code_tag_cloud import name_cloud, type_cloud, behavior_cloud
from extract_code_tags import extract_code_tags


class ExtractTypeScriptTagsTest(unittest.TestCase):
    lexer = TypeScriptLexer()

    def test_extracts_ts_object_names(self):
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

    def test_extracts_ts_object_shorthand_names(self):
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

    def test_extracts_ts_class_names(self):
        # given
        source_code = """
        class AuthorId {
            constructor(private readonly rawValue: string){
            }
        }
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        expected = ["AuthorId", "RawValue"]
        self.assertEqual(expected, result)

    def test_extracts_ts_class_function_behavior(self):
        # given
        source_code = """
        class Author {

            constructor(private readonly id: AuthorId, private name: string) {
            }
        
            greet(other: string): string {
                return `Hi ${other} I'm ${this.name}`;
            }
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        self.assertEqual([], result)

    def test_extracts_ts_class_lambda_behavior(self):
        # given
        source_code = """
        class Author {

            constructor(private readonly id: AuthorId, private name: string) {
            }
        
            greet = (other: string) => `Hi ${other} I'm ${this.name}`;
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        # TODO record-related pygments bug, function name considered Name.Other
        self.assertEqual([], result)
