export class Author {

    constructor(id, name) {
        this.#id = id;
        this.#name = name;
    }

    greet(other) {
        return `Hi ${other} I'm ${this.#name}`;
    }
}
