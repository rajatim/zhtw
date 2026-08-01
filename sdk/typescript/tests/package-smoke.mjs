import assert from 'node:assert/strict';

import * as zhtw from '../dist/index.node.mjs';

assert.equal(zhtw.convert('服务器上的软件'), '伺服器上的軟體');
assert.ok(zhtw.check('服务器').length > 0);
assert.equal(zhtw.lookup('服务器').output, '伺服器');
