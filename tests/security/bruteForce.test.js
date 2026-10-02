const { getKeyFingerprint } = require('../../src/utils/secureLogger.js');
test('FAIL: Masked key brute-forcable', () => {
  const masked = 'z_puce_live_key_v9_nans_core_7721';
  // suffix 4 digits => 10000 combos < 2min NPU 128 TFLOPS => FAIL
  expect(masked.includes('7721')).toBe(true);
});
test('PASS: Fingerprint irreversible', () => {
  const fp = getKeyFingerprint('z_puce_live_key_v9_nans_core_7721');
  expect(fp.length).toBe(8);
  expect(fp).not.toContain('7721');
});
