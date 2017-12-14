# DOCUMENTATION FOR STREAM 3 FINAL PROJECT - GAMERS HUB

## Table of Contents

[Description](#description)

[Testing](#testing)

[Installation](#installation)

[Usage](#usage)

[Credits](#credits)

---

<p align="center">
<img src='https://github.com/GunnerJnr/stream-three-final-project/blob/master/read-me-img/mobile-preview.png' alt="Mobile Preview">
</p>

## Description

A live version of the site can be accessed by following this [link](https://gamershub.herokuapp.com/).

### Stream Three Final Project - Gamers Hub

Gamers Hub is a fictional, all purpose online community for gamers and like minded people. The idea behind it came from my passion of games, gaming and game development. Its purpose is to unite gamers and like minded people from all across the world, it will give them a place to share and voice there opinions by utilising the `django-disqus` package to comment and have discussions on blog posts. The users will also have the option of creating their own blog posts which can also be commented on by fellow gamers. The user is also able to edit their blog post if they so wish. There is also a user profile page of which they can set some basic information about their self. There is also a store front which will allow the users to purchase any gaming product they desire, as long as we have it in stock. Currently we only have a few items but overtime we will grow and have a lot more on offer, so please bare with us. Users can also register to the site for free, by doing so they will get access to hidden parts of the site that are not available to just anyone! Such as the store for instance. Also users are not able to create or edit blog posts unless they have registered/logged in but they can of course view any blog posts that exist already.

The site can be navigated easily by using the navbar which can be found at the top of the page, it may have a hamburger menu (3 lines) on smaller devices, you simply click the link you want and it will navigate you to the relevant page.

Signing up is a synch, just fill in the form fields and away you go, you are then free to log in which will take you directly to your profile page, from here you can change your password, edit your profile or write a blog post. You may also have noticed you now have some new links in the navbar that were not available before signing up/logging in. You can also view the most viewed blog posts from the navbar to keep up with the latest popular trends.

Forgotten your password ? Don't panic you can eneter the email address you used in the forgotten password form and you will be sent a temporary link that will alow you to log in and change your password.

If you do feel the need to purchase a cool gaming item or piece of attire from our store, its quick and simple, we decided for a quick and easy purchase that we would integrate paypal, this was to keep it quick, simple and hassle free for all our users.

[Back to Table Of Contents](#table-of-contents)

---

## Testing

### Chrome Developer Tools

I have mainly used Google Chromes built in developer tools to help with testing my site over the duration of development. These tools have allowed me to inspect my code and make adjustments along the way in live time to see what certain changes could look like. It has also helped me with responsive design, this is a great tool because it has a selection of devices to choose from as well as normal responsive design where you can also adjust the width and height manually. The console has also come in very helpful along the way for errors with any missing resources, and also with any errors in the Javascript files. Aside form the above mentioned there are other tools in Chrome used for bits and bobs but nothing worth going in to detail about at this time.

### House Hold Devices

I used a number of house hold devices to test my site on also, I can say it seems to work flawlesy on appled devices, I can't seem to fault it there. On android I have come across a couple of weird bugs, the biggest being that if you run the website on an Amazon branded tablet it seems to render in desktop view opposed to mobile view, but I think this is due to the device not forcing refresh, the only way I could get it to render properly in the end was to literally clear the browser history until the beginning of time as Google put it, and it seemed to work fine until the next push to Heroku. Seems a bit strange but I think it is more to do with the device than the site. I also have a friend who tested on his Windows Phone, he seems to get some weird bottom margins and the links in the blog post details also run off the screen like they are not responsive, I have tested this in the site and the urls do seem responsive to a certain degree, but I cannot understand why they don't resize properly like the rest of the site, unless its because the content was copied and pasted, then I guess it could be to do with the encoding perhaps. It is something I will look into further and continue to work on in the near future.

### Built In Django Testing

This is a department I seemed to struggle in, I mainly struggled with coming up for tests to write. Whether it is just because of lack of knowledge or lack of experience I don't know, so I am hoping the tests are sufficient. There are around 8 in total. I would like to add more in due course but due to time constraints I will just have to leave it as is for the time being. A little about the tests. I have focused mainly on writing tests for the accounts app due to it being one of the more important as it contains user information. There are tests for the user login with username or email, as well as various other tests for page rendering, etc.

### Slack Group Code Institute Students

The students on the Slack App, who are part of the same course also played a major part in my testing of the site, it was vital they all test on there different gadgets and devices, and sign up, they pointed out a lot of flaws and bugs in the app. One which was a pretty big expoit, found by Andy, (mormoran), this exploit allowed any user that was registered to edit any users blog post, as you can see this is not ideal and quick a big flaw in the system, luckily it was found and fixed. Andy was also responsible for suggesting I used the class of container opposed to container-fluid. Mainly this is so he didn't keep getting neck ache from panning his head 180 degrees looking at the screen from left to right. I also need to thank the likes of Robin (robinz) and Simen (eventyret) for their continued help throughout the course.There are a number of other students too but there are too many to name.

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

A note on the majority of these CSS Validation warnings/errors, I believe most to be because they use some CSS4 language but we can only validate CSS3 as of now. Also after some research the Empty String error is a know bug for border radius in CSS. However I felt it best I still document them to show I am aware of their existence in the project.

##### [gamershubs-dark.css](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css)

* [Line 301](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L301): `#blog-post-detail-thumb img` - Parse Error [empty string]
* [Line 302](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L302): `#blog-post-detail-thumb img` - Parse Error [empty string]
* [Line 324](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L324): `.pagination a` - Property transition doesn't exist : `background-color #eeba2c 0.3s background-color #eeba2c 0.3s`
* [Line 356](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L356): `#profile-img-container img` - Parse Error [empty string]
* [Line 569](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L569): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* [Line 572](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L572): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* [Line 579](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L579): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* [Line 586](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L586): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* [Line 666](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L666): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* [Line 669](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L669): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* [Line 675](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L675): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* [Line 682](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L682): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* [Line 762](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L762): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* [Line 765](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L765): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* [Line 771](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L771): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* [Line 778](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L778): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* [Line 823](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L823): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* [Line 826](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L826): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* [Line 832](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L832): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* [Line 839](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L839): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]
* [Line 884](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L884): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`          [-webkit-scrollbar]
* [Line 887](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L887): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`    [-webkit-scrollbar-track]
* [Line 893](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L893): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb]
* [Line 900](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub-dark.css#L900): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`    [-webkit-scrollbar-thumb:window-inactive]

##### [gamershubs.css](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css)

* [Line 292](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L292): `#blog-post-detail-thumb img` - Parse Error [empty string]
* [Line 293](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L293): `#blog-post-detail-thumb img` - Parse Error [empty string]
* [Line 316](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L316): `.pagination a` - Property transition doesn't exist : `background-color #eeba2c 0.3s background-color #eeba2c 0.3s`
* [Line 343](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L343): `#profile-img-container img` - Parse Error [empty string]
* [Line 552](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L552): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* [Line 555](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L555): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* [Line 562](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L562): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* [Line 569](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L569): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* [Line 651](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L651): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* [Line 654](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L654): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* [Line 660](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L660): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* [Line 667](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L667): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* [Line 749](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L749): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* [Line 752](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L752): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* [Line 758](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L758): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* [Line 765](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L765): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* [Line 812](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L812): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* [Line 815](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L815): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* [Line 821](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L821): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* [Line 828](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L828): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]
* [Line 875](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L875): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar`           [-webkit-scrollbar]
* [Line 878](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L878): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-track`     [-webkit-scrollbar-track]
* [Line 884](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L884): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb]
* [Line 891](https://github.com/GunnerJnr/stream-three-final-project/blob/master/static/css/gamershub.css#L891): Unknown pseudo-element or pseudo-class `::-webkit-scrollbar-thumb`     [-webkit-scrollbar-thumb:window-inactive]

### Javascript Files

I also just wnated to note I had a small issue with conflicting JS files in the project, it seemed that by using `$(document).ready` I was only able to use the top most linked JS file and the other wouldn't respond, I had no idea why it was doing this, all I can put it down to is the way that Django renders its templates, and because most of the templates extend from `Base.html` that once it had rendered it didnt re render for the newer script. The fix to remedy this problem was simply to remove the `$(document).ready` and all works fine.

### Paypal IPN

I managed to integrate paypal and users can successfully buy or cancel their purchase and will be redirected back to the site. However, I have no functionality in place that would return the user a reciept for purchase, I will rely on paypal to handle this for me as I set up payments using Single Payments.

[Back to Table Of Contents](#table-of-contents)

---

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

---

## Usage

[Django Bootstrap Forms](https://django-bootstrap-form.readthedocs.io/en/latest/) - Used for responsive layout and design.

[Django Paypal](https://django-paypal.readthedocs.io/en/latest/) - Used for making `Paypal` single payments.

[Django Disqus](https://django-disqus.readthedocs.io/en/latest/) - Used for integrating `Disqus` comments into the blog posts.

[Solr Thumbnail](https://sorl-thumbnail.readthedocs.io/en/latest/) - Used for resizing the images uploaded by users.

[Django Bootstrap Forms](https://django-bootstrap-form.readthedocs.io/en/latest/) - Used for helping with responsive design.

[Django Storages](https://django-storages.readthedocs.io/en/latest/) - Used for storing static data and media on Amazon AWS Storage.

[Back to Table Of Contents](#table-of-contents)

---

## Credits

[Code Institute](https://www.codeinstitute.net) - For the lessons on Full Stack Development.

The Slack Community, its been a pleasure! Special thanks go to Yoni Lavi, Nakita, Niel and Tiffany Snell for being the best mentors/helpers out there.

[Back to Table Of Contents](#table-of-contents)

---
