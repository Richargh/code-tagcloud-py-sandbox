class RentingFacade {
    #availableBooks = new Map();
    #rentedBooks = new Map();

    rent(id){
        if(!this.#availableBooks.has(id)){
            return null;
        }
        const book = this.#availableBooks.get(id);
        this.#availableBooks.delete(id);
        this.#rentedBooks.set(id, book);

        return book;
    }
}