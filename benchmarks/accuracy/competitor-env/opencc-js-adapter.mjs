import crypto from 'node:crypto';
import readline from 'node:readline';
import { createRequire } from 'node:module';
import OpenCC from '/opt/opencc-js/node_modules/opencc-js/dist/esm/full.js';

const require = createRequire(import.meta.url);
const packageJson = require('/opt/opencc-js/node_modules/opencc-js/package.json');
const config = JSON.stringify({ from: 'cn', to: 'twp' });
const converter = OpenCC.Converter({ from: 'cn', to: 'twp' });
const input = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });

function respond(value) {
  process.stdout.write(`${JSON.stringify(value)}\n`);
}

for await (const line of input) {
  let requestId = null;
  try {
    const request = JSON.parse(line);
    if (request === null || Array.isArray(request) || typeof request !== 'object') {
      throw new Error('request must be an object');
    }
    requestId = request.id ?? null;
    if (request.op === 'probe') {
      respond({
        ok: true,
        id: requestId,
        engine: 'opencc-js-cn-twp',
        family: 'opencc',
        version: packageJson.version,
        config: 'cn -> twp',
        config_sha256: crypto.createHash('sha256').update(config).digest('hex'),
      });
      continue;
    }
    if (request.op !== 'convert' || typeof request.text !== 'string') {
      throw new Error('convert request requires string text');
    }
    respond({ ok: true, id: requestId, output: converter(request.text) });
  } catch (error) {
    respond({ ok: false, id: requestId, error: String(error.message ?? error) });
  }
}
