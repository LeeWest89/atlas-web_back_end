import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    this._amount = newAmount;
  }

  get currency() {
    return this._currency;
  }

  set currency(Currency) {
    this._currency = Currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  convertPrice(conversionRate) {
    return `${this._amount * conversionRate} ${new Currency(this._currency.code, this._currency.name).displayFullCurrency()}`;
  }
}
