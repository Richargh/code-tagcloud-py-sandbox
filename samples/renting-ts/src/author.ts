export class Author {

    constructor(private readonly id: AuthorId, private name: string) {
    }

    greet(other: string): string {
        return `Hi ${other} I'm ${this.name}`;
    }
}

export class AuthorId {
    constructor(private readonly rawValue: string) {
    }
}
