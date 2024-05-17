export class Book {

    constructor(private readonly id: BookId, private title: string, private authorId: string) {
    }
}

export class BookId {
    constructor(private readonly rawValue: string) {
    }
}
