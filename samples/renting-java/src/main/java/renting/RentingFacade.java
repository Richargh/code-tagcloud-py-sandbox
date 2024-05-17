package renting;

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