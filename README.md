DOCUMENTATION FOR STREAM 3 FINAL PROJECT - THE DJANGO SITE
----------------------------------------------------------

### Table of Contents

[Description](#description)

[Testing](#testing)

[Installation](#installation)

[Usage](#usage)

[Credits](#credits)

### Description

A live version of the site can be accessed by following this [link](https://gamershub.herokuapp.com/)

#### Stream Three Final Project - Gamers Hub.

Gamers Hub is a fictional all purpose online community for gamers and like minded people. The idea behind it came from my passion of games and game development. Its purpose is to unite gamers and like minded people, it will give them a place to share and voice there opinions by using django-disqus to comment on blog posts. The also have the option of creating their own blog posts which can also be commented on by fellow gamers. There is a profile page of which they can set some basic information about their self. We also have a store front which will allow them to purchase any gaming product they desire, as long as we have it in stock.

[Back to Table Of Contents](#table-of-contents)

### Testing

TODO

[Back to Table Of Contents](#table-of-contents)

### Installation

Firstly clone the project from Github, you can do with the following command in a terminal/console window:

`git clone https://github.com/gunnerjnr/stream-three-final-project.git`

Once you have cloned the project, you will need to set up a virtual environment to use the project offline. This assumes you already have Python and Pip installed. If you do not then please see the following links. 

[Python](https://www.python.org/downloads/) - Note we use version 2.7 of Python.

[Pip - Official Installation Guide](https://pip.pypa.io/en/latest/installing/)

Also please see the following link for setting up a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv)

Once all this is completed you should simply be able to run the command `pip install -r requirements.txt` from your activated virtual environment terminal/console window to install all the neccessary packages needed to run the project. Once this completes you should be able to now simply run the command `python manage.py runserver` and it should fire up the development server where you can navigate to `localhost:8000` to browse the site offline.

[Back to Table Of Contents](#table-of-contents)

### Usage

Django Bootstrap Forms - Used for responsive layout and design.
Django Paypal - Used for making Paypal single payments.
Django Disqus - Used for integrating Disqus comments into the blog posts.

[Back to Table Of Contents]

### Credits

Code Institute - For the lessons on Full Stack Development.

[Back to Table Of Contents](#table-of-contents)
