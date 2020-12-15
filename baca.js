let fs = require('fs');
let args = fs.readFileSync('tmpfile', {encoding:'utf8', flag:'r'});
console.log(args);