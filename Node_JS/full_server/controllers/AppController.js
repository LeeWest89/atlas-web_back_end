// creates AppController class with static method getHomepage
class AppController {
  static getHomepage(request, response) {
    response.send(200, 'Hello Holberton School!');
  }
}

module.export = AppController;
