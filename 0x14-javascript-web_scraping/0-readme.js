#!/usr/bin/env node

const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
    console.error('Please provide a file path as the first argument');
    process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

