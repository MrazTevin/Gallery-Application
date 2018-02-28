# Gallery Application

![Tevin's Gallery](https://www.dropbox.com/s/vgwvqj45as6i2sx/Screenshot%202018-02-28%2015.13.13.png?dl=0 "A personal gallery application that displays images for others to see.")

## Specifications

> Please see[SPECIFICATIONS.md](https://github.com/MrazTevin/SPECS.md) for details
  on the behaviour driven development of this app


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
1.Git
  2.Python: 3.6.4 versions
  3.Django: 1.11 or greater version
  4.Have Internet connection
  5.Virtual Environment
  6.Gunicorn
  7.Chrome Browser

```

### Installing

> Follow this procedure to get my project up and running in your Desktop or Laptop.

```
> Install Django Framework '''$pip install django==1.11'''
> Install Python Version --3.6.4
> Install gunicorn in (virtual) -python3.6 -m pip install gunicorn
> Install the Heroku Cli
> $ git clone https://github.com/MrazTevin/Gallery-Application.git
> $ Python3.6 -m venv Virtual
> $ Source virtual/bin/activate
> [See deployed Version At]
```

## Running the tests
* To test the functionalities of this app run the command below on your terminal:
  1.First cd Gallery-Application/exhibit then;
  ```
  $Python3.6 manage.py test
  ```  

###  End to end tests
1. Save : Will test if one is able to save i.e save the image location.
2. Delete : Will test if one is able to delete i.e delete the image location.
3. Instance : Will test the instance of the class i.e TestInstance of Image Class

```
def test_save_method(self):
    self.outdoor.save_location()
    location = Location.objects.all()
    self.assertTrue(location)
```

### Coding style Tests

- This tests will enable us write methods that we need for our app to function, which we will       include in our models file

```
def save_location(self):
      self.save()

  def delete_location(self):
      self.save()
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Python](https://maven.apache.org/) - Dependency Management
* [Bootstrap3](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [UI KIT](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [MDB Bootstrap](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [Heroku](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Authors

* **Tevin Milla** - *Initial work* - [PingPong](https://mraztevin.github.io/Ping-Pong/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Moringa School
