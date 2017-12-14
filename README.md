# DOCUMENTATION FOR STREAM 3 FINAL PROJECT - GAMERS HUB

## Table of Contents

[Description](#description)

[Testing](#testing)

[Installation](#installation)

[Usage](#usage)

[Credits](#credits)

## Description

A live version of the site can be accessed by following this [link](https://gamershub.herokuapp.com/).

### Stream Three Final Project - Gamers Hub

Gamers Hub is a fictional, all purpose online community for gamers and like minded people. The idea behind it came from my passion of games and game development.

Its purpose is to unite gamers and like minded people, it will give them a place to share and voice there opinions by utilising the `django-disqus` pkg to comment on blog posts.

The users will also have the option of creating their own blog posts which can also be commented on by fellow gamers.

There is also a profile page of which they can set some basic information about their self if they so wish.

There is also a store front which will allow the users to purchase any gaming product they desire, as long as we have it in stock.

Users can register to the site for free, by doing so they will get access to hidden parts of the site that are not available to just anyone! Such as the store for instance. Also users are not able to crete or edit blog posts unless registered/logged in but they can of course view any that exist already.

[Back to Table Of Contents](#table-of-contents)

## Testing

### Chrome Developer Tools

I have mainly used Google Chromes built in developer tools to help with testing my site over the duration of development. These tools have allowed me to inspect my code and make adjustments along the way in live time to see what certain changes could look like. It has also helped me with responsive design, this is a great tool because it has a selection of devices to choose from as well as normal responsive design where you can also adjust the width and height manually. The console has also come in very helpful along the way for errors with any missing resources, and also with any errors in the Javascript files. Aside form the above mentioned there are other tools in Chrome used for bits and bobs but nothing worth going in to detail about at this time.

### House Hold Devices

I used a number of house hold devices to test my site on also, I can say it seems to work flawlesy on appled devices, I can't seem to fault it there. On android I have come across a couple of weird bugs, the biggest being that if you run the website on an Amazon branded tablet it seems to render in desktop view opposed to mobile view, but I think this is due to the device not forcing refresh, the only way I could get it to render properly in the end was to literally clear the browser history until the beginning of time as Google put it, and it seemed to work fine until the next push to Heroku. Seems a bit strange but I think it is more to do with the device than the site. I also have a friend who tested on his Windows Phone, he seems to get some weird bottom margins and the links in the blog post details also run off the screen like they are not responsive, I have tested this in the site and the urls do seem responsive to a certain degree, but I cannot understand why they don't resize properly like the rest of the site, unless its because the content was copied and pasted, then I guess it could be to do with the encoding perhaps. It is something I will look into further and continue to work on in the near future.

### Built In Django Testing

This is a department I seemed to struggle in, I mainly struggled with coming up for tests to write. Whether it is just because of lack of knowledge or lack of experience I don't know, so I am hoping the tests are sufficient. There are around 8 in total. I would like to add more in due course but due to time constraints I will just have to leave it as is for the time being. A little about the tests. I have focused mainly on writing tests for the accounts app due to it being one of the more important as it contains user information. There are tests for the user login with username or email, as well as various other tests for page rendering, etc.

### Deployment

I deployed the site to Heroku, the only unfortunate thing here is that the only way to test changes live are to push them to Heroku. One thing I regret not doing with this is creating a branch on github for development, instead I stupidly pushed every change to the master branch, and it has a very high commit count and is now quite a messey commit history. I will learn from my mistake and not do the same in the future.

Heroku deployment was ok but I did have a lot of issues with the static files to begin, it was deleting images from the server after the dynos were restarted. because of this I decided to change the storage to Amazon AWS, it functions a lot better. I also used the ClearDB add on for dumping the data from local to heroku for the database to be uploaded.

### Known Bugs

At this time I only know of a few bugs in the site. One is the bug mentioned above with the urls in the blog post detail overlapping the edge of the page on some devices.

Heroku seems to throw out some weird bugs every now and then, one of which is more a warning than a bug where bootstrap forms complains about unreferenced varibales that have not been defined in the template, it seems to do this while processing the template and also the admin panel. As far as I am aware this is nothing to worry about and is quite a common short cut that a lot of developers use. For more information about this please see this [stack overflow answer](https://stackoverflow.com/questions/34797884/getting-error-with-is-popup-variable-in-django-1-9).

Also as of yesterday (13/12/2017) heroku was acting a bit strange and throwing out the below error related to MySQL. It has yet to do it again so I would like to put it down to Heroku maintenance or something. As another student was also recieving this I am pretty confident it is not my site or code causing this.

#### Heroku Stack Trace for MySQL Bug

```python

2017-12-13T13:15:40.481791+00:00 app[web.1]:     self.connect()
2017-12-13T13:15:40.481791+00:00 app[web.1]:   File "/app/.heroku/python/lib/python2.7/site-packages/django/db/backends/base/base.py", line 189, in connect
2017-12-13T13:15:40.481792+00:00 app[web.1]:     self.connection = self.get_new_connection(conn_params)
2017-12-13T13:15:40.481793+00:00 app[web.1]:   File "/app/.heroku/python/lib/python2.7/site-packages/django/db/backends/mysql/base.py", line 274, in get_new_connection
2017-12-13T13:15:40.481793+00:00 app[web.1]:     conn = Database.connect(**conn_params)
2017-12-13T13:15:40.481794+00:00 app[web.1]:   File "/app/.heroku/python/lib/python2.7/site-packages/MySQLdb/__init__.py", line 81, in Connect
2017-12-13T13:15:40.481794+00:00 app[web.1]:     return Connection(*args, **kwargs)
2017-12-13T13:15:40.481795+00:00 app[web.1]:   File "/app/.heroku/python/lib/python2.7/site-packages/MySQLdb/connections.py", line 193, in __init__
2017-12-13T13:15:40.481795+00:00 app[web.1]:     super(Connection, self).__init__(*args, **kwargs2)
2017-12-13T13:15:40.481797+00:00 app[web.1]: OperationalError: (1135, "Can't create a new thread (errno 11); if you are not out of available memory, you can consult the manual for a possible OS-dependent bug")

```

#### CSS Validation Errors

##### gamershubs-dark.css

* Line 301: `#blog-post-detail-thumb img` - Parse Error [empty string]
* Line 302: `#blog-post-detail-thumb img` - Parse Error [empty string]
* Line 324: `.pagination a` - Property transition doesn't exist : `background-color #eeba2c 0.3s background-color #eeba2c 0.3s`
* Line 356: `#profile-img-container img` - Parse Error [empty string]
* Line 569: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* Line 572: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* Line 579: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* Line 586: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* Line 666: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* Line 669: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* Line 675: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* Line 682: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* Line 762: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* Line 765: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* Line 771: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* Line 778: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* Line 823: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* Line 826: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* Line 832: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* Line 839: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* Line 884: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* Line 887: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* Line 893: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* Line 900: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
##### gamershubs.css

* Line 292: `#blog-post-detail-thumb img` - Parse Error [empty string]
* Line 293: `#blog-post-detail-thumb img` - Parse Error [empty string]
* Line 316: `.pagination a` - Property transition doesn't exist : `background-color #eeba2c 0.3s background-color #eeba2c 0.3s`
* Line 343: `#profile-img-container img` - Parse Error [empty string]
* Line 552: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* Line 555: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* Line 562: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* Line 569: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* Line 651: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* Line 654: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* Line 660: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* Line 667: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* Line 749: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* Line 752: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* Line 758: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* Line 765: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* Line 812: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* Line 815: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* Line 821: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* Line 828: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* Line 875: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* Line 878: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* Line 884: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* Line 891: Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]

[Back to Table Of Contents](#table-of-contents)

## Installation

Firstly clone the project from `Github`, you can do with the following command in a terminal/console window:

`git clone https://github.com/gunnerjnr/stream-three-final-project.git`

Once you have cloned the project, you will need to set up a `virtual environment` to use the project offline. This assumes you already have `Python` and `Pip` installed. If you do not then please see the following links.

[Python](https://www.python.org/downloads/) - Note we use `version 2.7` of `Python`.

[Pip - Official Installation Guide](https://pip.pypa.io/en/latest/installing/)

Also please see the following link for setting up a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv)

Once all this is completed you should simply be able to run the command `pip install -r requirements.txt` from your activated `virtual environment` terminal/console window to install all the neccessary packages needed to run the project. Once this completes you should be able to now simply run the command `python manage.py runserver` and it should fire up the development server where you can navigate to `localhost:8000` to browse the site offline.

Or as stated above, a live version of the site can be accessed by following this [link](https://gamershub.herokuapp.com/).

[Back to Table Of Contents](#table-of-contents)

## Usage

[Django Bootstrap Forms](https://django-bootstrap-form.readthedocs.io/en/latest/) - Used for responsive layout and design.

[Django Paypal](https://django-paypal.readthedocs.io/en/latest/) - Used for making `Paypal` single payments.

[Django Disqus](https://django-disqus.readthedocs.io/en/latest/) - Used for integrating `Disqus` comments into the blog posts.

[Solr Thumbnail](https://sorl-thumbnail.readthedocs.io/en/latest/) - Used for resizing the images uploaded by users.

[Django Bootstrap Forms](https://django-bootstrap-form.readthedocs.io/en/latest/) - Used for helping with responsive design.

[Django Storages](https://django-storages.readthedocs.io/en/latest/) - Used for storing static data and media on Amazon AWS Storage.

[Back to Table Of Contents](#table-of-contents)

## Credits

Code Institute - For the lessons on Full Stack Development.

[Back to Table Of Contents](#table-of-contents)
