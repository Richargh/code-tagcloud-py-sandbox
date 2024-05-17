import {Book, BookId} from "./book";
import {ForRenting} from "./for-renting";

class RentingFacade implements ForRenting {
    private readonly availableBooks = new Map<BookId, Book>();
    private readonly rentedBooks = new Map<BookId, Book>();

    rent(id: BookId): Book | null {
        if(!this.availableBooks.has(id)){
            return null;
        }
        const book = this.availableBooks.get(id);
        this.availableBooks.delete(id);
        this.rentedBooks.set(id, book);

        return book;
    }
}