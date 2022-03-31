import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
      this._amount = amount;
      this._currency = currency;
  }

  // Getters

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  // Setters

  set amount(amount) {
    return this._amount = amount;
  }

  set currency(currency) {
    return this._currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`
  }

  convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
