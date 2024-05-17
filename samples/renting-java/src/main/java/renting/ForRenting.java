package renting;

public interface ForRenting {
    Optional<Book> rent(BookId id);
}