const { createHash } = require('crypto');

//create a hash with SHA256 in base64
function hash(input) {
    return createHash('sha256').update(input).digest('base64');
}

//input password to hash
let password = 'hola34!';
const hash1 = hash(password);
console.log(hash1);
