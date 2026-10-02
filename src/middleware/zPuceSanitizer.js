export function sanitizeHardwareLog(log){const a=['requestId','statusCode','latencyMs','key_fp','timestamp'];const o={};for(const k of a)if(log[k]!=null)o[k]=log[k];return o;}
