import {
  validateAlphaNumeric,
  validateContainsNumberAndLetter,
  validateUsername,
  validateEmail,
  validatePassword,
} from '../helpers/functions';

test('test validate alphanumeric', () => {
  expect(validateAlphaNumeric('abcdefghijklmopqrstuvwxyz')).toBe(true);
  expect(validateAlphaNumeric('1234567890')).toBe(true);
  expect(validateAlphaNumeric('!_@*?={[]}')).toBe(false);
});

test('test validate contains number and letter', () => {
  expect(validateContainsNumberAndLetter('abcdefghijklmopqrstuvwxyz')).toBe(false);
  expect(validateContainsNumberAndLetter('1234567890')).toBe(false);
  expect(validateContainsNumberAndLetter('!_@*?={[]}')).toBe(false);
  expect(validateContainsNumberAndLetter('1a')).toBe(true);
  expect(validateContainsNumberAndLetter('A1')).toBe(true);
});

test('test validate username', () => {
  expect(validateUsername('t')).toBe(false);
  expect(validateUsername('test')).toBe(true);
  expect(validateUsername('test@test')).toBe(false);
});

test('test validate email', () => {
  expect(validateEmail('test@test.com')).toBe(true);
  expect(validateEmail('test')).toBe(false);
});

test('test validate password', () => {
  expect(validatePassword('pw')).toBe(false);
  expect(validatePassword('password')).toBe(false);
  expect(validatePassword('123456')).toBe(false);
  expect(validatePassword('password123456')).toBe(true);
});
