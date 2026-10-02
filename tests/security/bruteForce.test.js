test('fp',()=>{const c=require('crypto'); const fp=c.createHash('sha256').update('key').digest('hex').slice(0,8); if(fp.length!=8) throw new Error();});
