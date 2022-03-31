export default class Building {
  constructor (sqft) {
    if (this.constructor !== Building) {
      if (!this.evacuationWarningMessage) throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Get

  get sqft() {
    return this._sqft;
  }

  // Set

  set sqft(sqft) {
    return this._sqft = sqft;
  }
}
