import unittest

from pygments.lexers.dotnet import CSharpLexer

from draw_code_tag_cloud import name_cloud, type_cloud, behavior_cloud
from extract_code_tags import extract_code_tags


class ExtractCsharpTagsTest(unittest.TestCase):
    lexer = CSharpLexer()

    def test_extracts_csharp_record_names(self):
        # given
        source_code = """
        public record AuthorId(string RawValue);
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), source_code)
        # then
        # TODO record-related pygments bug
        self.assertEqual(["record", "RawValue"], result)

    def test_extracts_csharp_record_types(self):
        # given
        source_code = """
        public record AuthorId(string RawValue);
        """
        # when
        result = extract_code_tags(self.lexer, type_cloud(), source_code)
        # then
        # TODO record-related pygments bug, AuthorId considered a function
        self.assertEqual([], result)

    def test_extracts_csharp_record_behavior(self):
        # given
        source_code = """
        public record Author(AuthorId Id, string Name)
        {
            public string Greet() => "Hi I'm "+Name";
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), source_code)
        # then
        self.assertEqual(["Author", "Greet"], result)

    def test_extracts_csharp_class_behavior(self):
        # given
        source_code = """
        public class Author
        {
            public required AuthorId Id { get; init; }
            public required string Name { get; set; }
            
            public Author(AuthorId id, string name)
            {
                this.Id = id;
                this.Name = name;
            }
            
            public string Greet(string other) => $"Hi {other} I'm {name}";
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), source_code)
        # then
        self.assertEqual(["Author", "Greet"], result)

    def test_extracts_csharp_class_behavior_invocation(self):
        # given
        source_code = """
        public class RentingFacade: IRent {

            private readonly Dictionary<BookId, Book> _availableBooks;
            private readonly Dictionary<BookId, Book> _rentedBooks;

            public Book Rent(BookId id){
                if(!_availableBooks.ContainsKey(id)){
                    return null;
                }

                var book = _availableBooks.Remove(id);
                _rentedBooks.Add(book);

                return book;
            }

        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), source_code)
        # then
        # (constructors are also functions, fields are arguments)
        self.assertEqual(["Rent"], result)
