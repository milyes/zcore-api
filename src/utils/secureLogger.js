import crypto from 'crypto';
export function getKeyFingerprint(key){
  if(!key) return null;
  return crypto.createHash('sha256').update(String(key)).digest('hex').slice(0,8);
}
export function secureLog(data){
  const { sanitizeHardwareLog } = require('../middleware/zPuceSanitizer.js');
  return sanitizeHardwareLog(data);
}
