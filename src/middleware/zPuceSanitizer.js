// zPuceSanitizer.js - DLP V9 cloche hermétique
export function sanitizeHardwareLog(log){
  const allowed = ['requestId','statusCode','latencyMs','temperatureCelsius','computePowerTflops','key_fp','timestamp'];
  const out={};
  for(const k of allowed){ if(log[k]!==undefined) out[k]=log[k]; }
  return out;
}
export function getSafeLogContext(){
  return { timestamp: new Date().toISOString() };
}
