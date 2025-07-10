import User, { validateEmail } from './User.js';

const user = new User('sagar');
console.log(user.getInfo());

const email = 'srisaagar@gmail.com';
console.log(`Is "${email}" a valid email?`, validateEmail(email));