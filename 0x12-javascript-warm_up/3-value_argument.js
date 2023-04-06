#!/usr/bin/node
const args = process.args.slice(2);

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
