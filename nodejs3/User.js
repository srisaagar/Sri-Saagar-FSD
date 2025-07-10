export default class User {
    constructor(name) {
        this.name = name;
    }

    getInfo() {
        return `User: ${this.name}`;
    }
}

export function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}