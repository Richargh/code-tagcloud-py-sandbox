import unittest

from pygments.lexers.jvm import JavaLexer

from draw_code_tag_cloud import name_cloud, type_cloud, behavior_cloud, all_cloud
from extract_code_tags import extract_code_tags


class ExtractJavaTagsTest(unittest.TestCase):
    lexer = JavaLexer()

    def test_extracts_java_record_all(self):
        # given
        source_code = """
        public record AuthorId(String rawValue){ }
        """
        # when
        result = extract_code_tags(self.lexer, all_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId", "String", "RawValue"], result)

    def test_extracts_java_record_names(self):
        # given
        source_code = """
        public record AuthorId(String rawValue){ }
        """
        # when
        result = extract_code_tags(self.lexer, name_cloud(), set(), source_code)
        # then
        self.assertEqual(["String", "RawValue"], result)

    def test_extracts_java_record_types(self):
        # given
        source_code = """
        public record AuthorId(String rawValue){ }
        """
        # when
        result = extract_code_tags(self.lexer, type_cloud(), set(), source_code)
        # then
        self.assertEqual(["AuthorId"], result)

    def test_extracts_java_record_behavior(self):
        # given
        source_code = """
        public record Author(AuthorId id, String name){
            public string greet(String other){
                return "Hi "+other+" I'm "+name";
            }
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        self.assertEqual(["Greet"], result)

    def test_extracts_java_class_behavior(self):
        # given
        source_code = """
        public class Author
        {
            private final AuthorId id;
            private final String name;

            public Author(AuthorId id, String name)
            {
                this.id = id;
                this.name = name;
            }

            public String greet(String other){
                return "Hi "+other+" I'm "+name";
            }
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        # (constructors are also functions, fields are arguments)
        self.assertEqual(["Author", "Id", "Name", "Greet"], result)

    def test_extracts_java_class_behavior_invocation(self):
        # given
        source_code = """
        public class RentingFacade implements ForRenting {

            private final Map<BookId, Book> availableBooks;
            private final Map<BookId, Book> rentedBooks;
        
            public Optional<Book> rent(BookId id){
                if(!availableBooks.containsKey(id)){
                    return Optional.empty();
                }
        
                var book = availableBooks.remove(id);
                rentedBooks.put(book);
        
                return Optional.of(book);
            }
        
        }
        """
        # when
        result = extract_code_tags(self.lexer, behavior_cloud(), set(), source_code)
        # then
        # (constructors are also functions, fields are arguments)
        expected = ["Rent", "ContainsKey", "Empty", "Remove", "Put", "Of"]
        self.assertEqual(expected, result)
