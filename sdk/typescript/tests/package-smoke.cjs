const assert = require('node:assert/strict');

const zhtw = require('../dist/index.node.cjs');

assert.equal(zhtw.convert('服务器上的软件'), '伺服器上的軟體');
assert.ok(zhtw.check('服务器').length > 0);
assert.equal(zhtw.lookup('服务器').output, '伺服器');
