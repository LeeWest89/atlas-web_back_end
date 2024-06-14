import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floor) {
    super(sqft);
    this._floors = floor;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this._floors} floors`);
  }
}
