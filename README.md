# Codedigger Backend API

[![Codedigger][codedigger-shield]][Codedigger]
[![Codedigger API][codedigger-api-shield]][API]
[![Codedigger API][codedigger-api-doc-shield]][API-DOC]


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

[![Apache License][license-shield]][license-url]
[![Contributor Covenant][code-of-conduct-shield]][code-of-conduct-url]

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Discord][discord-shield]][discord-url]

## Table of Contents

1. [Introduction](#introduction)
1. [Getting Started](#getting-started)
	1. [Fork, clone locally and create a branch](#fork-clone-locally--create-a-branch)
	1. [Setting Environment First Time](#setting-environment-first-time)
		1. [Basic Requirements](#basic-requirements)
		1. [Creating Virtual Environment](#creating-virtual-environment)
		1. [Installing Requirements](#installing-requirements)
		1. [Setting up Database and Environment File](#setting-up-database-and-environment-file)
		1. [Migrating Database](#migrating-database)
		1. [Create Superuser](#create-superuser)
	1. [Starting Development Server](#starting-development-server)
	1. [Leaving the virtual environment](#leaving-the-virtual-environment)
	1. [Update requirements file](#update-requirements-file-critical)
	1. [Update Database](#update-database)  
1. [Code of Conduct](#code-of-conduct)
1. [Contributing](#contributing)
1. [License](#license)
1. [How to Get Help](#how-to-get-help)


## Introduction

This is the backdoor REST [API] developed to do complex calclations, provide and store data for [Codedigger] Website. 

Codedigger aims at accumulating the data of competitive programming platforms ([Codeforces], [Codechef], [Atcoder], [SPOJ] and [UVA Online Judge]) into one platform. We used their publicly available APIs and introduced several unique features into our application such as friends, mentors, ladders, upsolve, problem and contest filter. This can be the ultimate stop for everyone practicing competitive programming.

User can practice topicwise list to expertise any topic, levelwise list to practice based on rating and difficulty, or can create their own list and follow that. They can filter problems based on difficulty, tag, or solved by mentor from all the sites combined at one place.

Upsolving means to solve those problems, you're not able to solve during the contest. With the help of codedigger, you will be able to upsolve codeforces, codechef, and atcoder contests in an easy and better way.


## Getting Started

### Fork, clone locally & create a branch

Fork [Codedigger Backend](https://help.github.com/articles/fork-a-repo) repository and clone at your local 

```sh
git clone https://github.com/<yourGithubUsername>/Backend.git
cd Backend/
```

Create a branch with a descriptive name. A good branch name would be : 
```sh
git checkout -b feature/AmazingFeature
```
```sh
git checkout -b bugfix/user
```

### Setting Environment First Time

#### Basic Requirements 
1. [Python](https://www.python.org/downloads/)
1. [pip](https://pip.pypa.io/en/stable/installation/)

#### Creating [Virtual Environment](https://docs.python.org/3/library/venv.html) 

A virtual environment is a tool that helps keep dependencies required and the project isolated. If you wish to install a new library and write
```
pip install name_of_library
``` 
on the terminal without activating an environment, all the packages will be installed globally which is not a good practice if you’re working with different projects on your computer.

If this sounds a bit complicated, don’t worry so much because a virtual environment is just a directory that will contain all the necessary files for our project to run.

**Installing venv (required once)**

**Windows**
```
py -m pip install --user virtualenv
py -m venv env
```
**Linux**
```
python3 -m pip install --user virtualenv
python3 -m venv env
```

You have to start virtual environment everytime you start new terminal -

**Windows**

Using gitbash
```
. env/Scripts/activate
```
Using Powershell
```
. env\Scripts\activate
```
**Linux**
```
source env/bin/activate
```

#### Installing Requirements 
**Windows**
```
pip install -r requirements.txt
```
**Linux**
```
pip3 install -r requirements.txt
```

#### Setting up Database and Environment File

**Requirement- MySQL**

You can download MySQL from [here](https://www.mysql.com/downloads/) or download [XAMPP](https://www.apachefriends.org/download.html).

Start MySQL server and create a database.

**Configuring Environment Variables**

cd to codedigger directory, this is our working directory. For now we will run all command in this directory only - 
```
cd codedigger/
```

Make environment file in codedigger directory by copying the example file -
```
cp codedigger/.env.example codedigger/.env
``` 

**Database Settings**
```
DB_NAME = codedigger
DB_USER = root
DB_PASSWORD = 
DB_HOST = 127.0.0.1
DB_PORT = 3306
```

**GMAIL Settings**

You need to [turn on less secure app access](https://support.google.com/accounts/answer/6010255?hl=en) for sending mails. 
```
EMAIL_HOST_USER = your_mail_id
EMAIL_HOST_PASSWORD = your_password
```

#### Migrating Database
**Windows**
```
py manage.py migrate
```
**Linux**
```
python3 manage.py migrate
```

#### Create Superuser
**Windows**
```
py manage.py createsupeser
```
**Linux**
```
python3 manage.py createsupeser
```

### Starting Development Server
**Windows**
```
py manage.py runserver
```
**Linux**
```
python3 manage.py runserver
``` 

### Leaving the virtual environment
```
deactivate
```

### Update requirements file (Critical)
If you have installed new dependency, the pip freeze command lists the third-party packages and versions installed in the environment. 

**Windows**
```
pip freeze > requirements.txt
```
**Linux**
```
pip3 freeze > requirements.txt
```

### Update Database  
Everytime you change db models, you need to run makemigrations and migrate to update on database.

**Windows**
```
py manage.py makemigrations
py manage.py migrate
```
**Linux**
```
python3 manage.py makemigrations
python3 manage.py migrate
``` 

## Code of Conduct

This project and everyone participating in it is governed by the [Codedigger Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to contact.codedigger@gmail.com.


## Contributing

We encourage you to participate in this open source project. We love Pull Requests, Bug Reports, ideas, (security) code reviews or any other kind of positive contribution. Please review [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to file an issue or pr.

<!-- LICENSE -->
## License

Copyright 2021 Codedigger

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


<!-- CONTACT -->
## How to Get Help 

Email us - contact.codedigger@gmail.com

[Join][discord-url]! our Discord Community

**[Back to top](#table-of-contents)**


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Code-dig-ger/Backend.svg?style=for-the-badge
[contributors-url]: https://github.com/Code-dig-ger/Backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Code-dig-ger/Backend.svg?style=for-the-badge
[forks-url]: https://github.com/Code-dig-ger/Backend/network/members
[stars-shield]: https://img.shields.io/github/stars/Code-dig-ger/Backend.svg?style=for-the-badge
[stars-url]: https://github.com/Code-dig-ger/Backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/Code-dig-ger/Backend.svg?style=for-the-badge
[issues-url]: https://github.com/Code-dig-ger/Backend/issues
[license-shield]: https://img.shields.io/github/license/Code-dig-ger/Backend.svg?style=for-the-badge
[license-url]: https://github.com/Code-dig-ger/Backend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/codedigger
[code-of-conduct-shield]: https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg?style=for-the-badge
[code-of-conduct-url]: CODE_OF_CONDUCT.md
[discord-shield]: https://img.shields.io/badge/-Discord-555?style=for-the-badge&logo=discord&logoColor=white
[discord-url]: https://discord.gg/4ZeNgUn7cF
[API]: https://api.codedigger.tech/
[API-DOC]: http://docs.codedigger.tech/
[Codedigger]: https://codedigger.tech
[Codeforces]: https://codeforces.com/
[Codechef]: https://www.codechef.com/
[Atcoder]: https://atcoder.jp/
[SPOJ]: https://www.spoj.com/
[UVA Online Judge]: https://onlinejudge.org/
[codedigger-shield]: https://img.shields.io/badge/-Codedigger-555?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAuFJREFUOE+t1G1IE3EcB/DvFEPnmDrN5sPKxKGixgqns5n0oiezMl8EQSgESW8SqiFBRdCLMEhCKyopyNIsDErrRdmDmrFUlKInsGTMBW63ebc5t91s3ba43c5tmCHkwb24O/jc9////f4/AVb4Eqywh6VBoTANwoRqMIwStD2jsOUcflM2o/3zxNjcwGgvTZLGv4VZDIpEqShQNyFeVAuSiAFlAigC6lf3ECWIgtdFg3HSzMy74fv6ru5TsLjM4XAkKMstxo4Dz+Cck4I0YeG2BkEAjMsNr8sNxkXDQ9rMuuvt1e7JqVEeDYGrM+U4cnYUDlsSSCKEsbCVQPnrDgh8vgjQS9PwWO123dVbKo+RmmDREHiydQjixC1cKgLsUqPsFmSW50OiyEVCgRw+N5sslJAFvU4ajh/6EUNb52YAfg7MV1bg2IW3oWQEoh0z2NRQhST5WvgYJrDEwP6FgwvvaEzdfrht/uf0Gw48pGmGepcmHFyvkkG+pyTweTHIw9xP2D219GtbqcHh4xx4ovkp5Iq9bDX5QhQfVkOSLf0HyEE8aPvw5TnR07ebAzUtvcgp2sclNAKUGcV1pZDkpC8TpDH78esL05O+Sg6sbWyGulITahUC6zZKkVtTtmzQ0v/+GjU43MCBhaqtaGgaWEhIEoiaNUNRvx0phdlL7GFoyWzB9Hce7PylN77k20aA021axIvLAicj2IcCqxlShQzJRdmQKDfA7/EEqxxZFMfk1LjhZgdbwWDbsCnTs/JQf34EDmtCeHH4bVA9uoIYYWywffh+pOGx2R261vYyD0F8i2xs9ikrX4Wqul447akBKJCWu0u7LmOVOJ4DnW4w7CmhbKThRud+x3eddvHR498IU9JQUnEJIvFBkKZoHla2X0RsciI7GFjUS2nHu013Hze6KWp66eEQ/iUuToakNTXw+pWg5zLyzhz1w+czOT9NjJFDYz3zJpNheePrPyfuik/sP0+iITNZPL3cAAAAAElFTkSuQmCC
[codedigger-api-shield]: https://img.shields.io/badge/Codedigger-API-yellowgreen?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAuFJREFUOE+t1G1IE3EcB/DvFEPnmDrN5sPKxKGixgqns5n0oiezMl8EQSgESW8SqiFBRdCLMEhCKyopyNIsDErrRdmDmrFUlKInsGTMBW63ebc5t91s3ba43c5tmCHkwb24O/jc9////f4/AVb4Eqywh6VBoTANwoRqMIwStD2jsOUcflM2o/3zxNjcwGgvTZLGv4VZDIpEqShQNyFeVAuSiAFlAigC6lf3ECWIgtdFg3HSzMy74fv6ru5TsLjM4XAkKMstxo4Dz+Cck4I0YeG2BkEAjMsNr8sNxkXDQ9rMuuvt1e7JqVEeDYGrM+U4cnYUDlsSSCKEsbCVQPnrDgh8vgjQS9PwWO123dVbKo+RmmDREHiydQjixC1cKgLsUqPsFmSW50OiyEVCgRw+N5sslJAFvU4ajh/6EUNb52YAfg7MV1bg2IW3oWQEoh0z2NRQhST5WvgYJrDEwP6FgwvvaEzdfrht/uf0Gw48pGmGepcmHFyvkkG+pyTweTHIw9xP2D219GtbqcHh4xx4ovkp5Iq9bDX5QhQfVkOSLf0HyEE8aPvw5TnR07ebAzUtvcgp2sclNAKUGcV1pZDkpC8TpDH78esL05O+Sg6sbWyGulITahUC6zZKkVtTtmzQ0v/+GjU43MCBhaqtaGgaWEhIEoiaNUNRvx0phdlL7GFoyWzB9Hce7PylN77k20aA021axIvLAicj2IcCqxlShQzJRdmQKDfA7/EEqxxZFMfk1LjhZgdbwWDbsCnTs/JQf34EDmtCeHH4bVA9uoIYYWywffh+pOGx2R261vYyD0F8i2xs9ikrX4Wqul447akBKJCWu0u7LmOVOJ4DnW4w7CmhbKThRud+x3eddvHR498IU9JQUnEJIvFBkKZoHla2X0RsciI7GFjUS2nHu013Hze6KWp66eEQ/iUuToakNTXw+pWg5zLyzhz1w+czOT9NjJFDYz3zJpNheePrPyfuik/sP0+iITNZPL3cAAAAAElFTkSuQmCC
[codedigger-api-doc-shield]: https://img.shields.io/badge/Codedigger%20API-Doc-yellowgreen?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAuFJREFUOE+t1G1IE3EcB/DvFEPnmDrN5sPKxKGixgqns5n0oiezMl8EQSgESW8SqiFBRdCLMEhCKyopyNIsDErrRdmDmrFUlKInsGTMBW63ebc5t91s3ba43c5tmCHkwb24O/jc9////f4/AVb4Eqywh6VBoTANwoRqMIwStD2jsOUcflM2o/3zxNjcwGgvTZLGv4VZDIpEqShQNyFeVAuSiAFlAigC6lf3ECWIgtdFg3HSzMy74fv6ru5TsLjM4XAkKMstxo4Dz+Cck4I0YeG2BkEAjMsNr8sNxkXDQ9rMuuvt1e7JqVEeDYGrM+U4cnYUDlsSSCKEsbCVQPnrDgh8vgjQS9PwWO123dVbKo+RmmDREHiydQjixC1cKgLsUqPsFmSW50OiyEVCgRw+N5sslJAFvU4ajh/6EUNb52YAfg7MV1bg2IW3oWQEoh0z2NRQhST5WvgYJrDEwP6FgwvvaEzdfrht/uf0Gw48pGmGepcmHFyvkkG+pyTweTHIw9xP2D219GtbqcHh4xx4ovkp5Iq9bDX5QhQfVkOSLf0HyEE8aPvw5TnR07ebAzUtvcgp2sclNAKUGcV1pZDkpC8TpDH78esL05O+Sg6sbWyGulITahUC6zZKkVtTtmzQ0v/+GjU43MCBhaqtaGgaWEhIEoiaNUNRvx0phdlL7GFoyWzB9Hce7PylN77k20aA021axIvLAicj2IcCqxlShQzJRdmQKDfA7/EEqxxZFMfk1LjhZgdbwWDbsCnTs/JQf34EDmtCeHH4bVA9uoIYYWywffh+pOGx2R261vYyD0F8i2xs9ikrX4Wqul447akBKJCWu0u7LmOVOJ4DnW4w7CmhbKThRud+x3eddvHR498IU9JQUnEJIvFBkKZoHla2X0RsciI7GFjUS2nHu013Hze6KWp66eEQ/iUuToakNTXw+pWg5zLyzhz1w+czOT9NjJFDYz3zJpNheePrPyfuik/sP0+iITNZPL3cAAAAAElFTkSuQmCC
