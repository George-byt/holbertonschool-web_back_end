export default class Currency {
  constructor (code, name) {
    this._code = code;
    this._name = name;
  }

  // Getters

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  // Setters

  set code(code) {
    return this._code = code;
  }

  set name(name) {
    return this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
