import unittest

from pygments.lexers.jvm import KotlinLexer

from draw_code_tag_cloud import name_cloud, type_cloud, behavior_cloud, all_cloud
from extract_code_tags import extract_code_tags


class ExtractKotlinTagsTest(unittest.TestCase):
    lexer = KotlinLexer()

    def test_extracts_kotlin_value_class_all(self):
        # given
        source_code = """
        value class AuthorId(val rawValue: String)
        """
        # when
        result = extract_code_tags(self.lexer, all_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId", "RawValue", "String"], result)

    def test_extracts_kotlin_value_class_names(self):
        # given
        source_code = """
        value class AuthorId(val rawValue: String)
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        # TODO kotlin-related pygments bug, rawValue is a Variable and String is suddenly a type
        self.assertEqual([], result)

    def test_extracts_kotlin_value_class_types(self):
        # given
        source_code = """
        value class AuthorId(val rawValue: String)
        """
        # when
        result = extract_code_tags(self.lexer, type_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId"], result)

    def test_extracts_kotlin_data_class_names(self):
        # given
        source_code = """
        data class AuthorId(val rawValue: String)
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        # TODO kotlin-related pygments bug, rawValue is a Variable and String is suddenly a type
        self.assertEqual([], result)

    def test_extracts_kotlin_data_class_types(self):
        # given
        source_code = """
        value class AuthorId(val rawValue: String)
        """
        # when
        result = extract_code_tags(self.lexer, type_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId"], result)

    def test_extracts_kotlin_data_class_behavior(self):
        # given
        source_code = """
        data class Author(val id: AuthorId, val name: String){
            fun greet(other: String) = "Hi $other I'm $name"
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        self.assertEqual(["Greet"], result)
