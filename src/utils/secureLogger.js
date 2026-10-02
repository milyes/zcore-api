import crypto from 'crypto'; export function getKeyFingerprint(k){return crypto.createHash('sha256').update(String(k)).digest('hex').slice(0,8);}
