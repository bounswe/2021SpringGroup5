export function toTitleCase(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

export function validateAlphaNumeric(str) {
  let char, i;
  for (i = 0; i < str.length; i++) {
    char = str.charCodeAt(i);
    if (!((char > 47 && char < 58) || (char > 64 && char < 91) || (char > 96 && char < 123))) {
      return false;
    }
  }
  return true;
}

export function validateContainsNumberAndLetter(str) {
  let containsNumber = false;
  let containsLetter = false;
  let char, i;
  for (i = 0; i < str.length; i++) {
    char = str.charCodeAt(i);
    if (char > 47 && char < 58) {
      containsNumber = true;
    } else if ((char > 64 && char < 91) || (char > 96 && char < 123)) {
      containsLetter = true;
    }
  }
  return containsNumber && containsLetter;
}

export function validateUsername(str) {
  if (str.length < 4) {
    return false;
  }
  return validateAlphaNumeric(str);
}

export function validateEmail(str) {
  return !!str.includes('@');
}

export function validatePassword(str) {
  if (str.length < 6) {
    return false;
  }
  if (!validateAlphaNumeric(str)) {
    return false;
  }
  return validateContainsNumberAndLetter(str);
}

export function trimDescription(str) {
  return str.split(';')[0];
}

export function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
