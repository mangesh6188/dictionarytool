# Merriam-Webster Dictionary Tool

This command-line tool allows you to query the Merriam-Webster dictionary and receive a formatted response with the word definition.

### Prerequisite
Python3, pip3 and Make module should be preinstalled. 

## Installation

1. Clone this repository:

```
git clone https://github.com/mangesh6188/dictionarytool

```

2. Change into the project directory:
```
cd dictionarytool
```

3. Install the required dependencies using make:

```
make install
```

4. Sign up for a Merriam-Webster API key at Merriam-Webster Developer Portal.

## Usage
To use the tool, simply run the main.py script with the word you want to search for:

```
(I) make run word=WORD api_key=API_KEY
E.g - $ make run word=exercise api_key=x-x-x-x
python3 dictionarytool/main.py exercise x-x-x-x
INFO: Successfully able to connect to the dictionary API.
INFO: Defination of exercise : ˈek-sər-ˌsīz (noun): the act of bringing into play or realizing in action : use

(II) python dictionarytool/main.py WORD API_KEY
E.g - $ python3 main.py exercise x-x-x-x
INFO: Successfully able to connect to the dictionary API.
INFO: Defination of exercise : ˈek-sər-ˌsīz (noun): the act of bringing into play or realizing in action : use

The tool will print the definition of the word if found in the dictionary.
```

### Tests
```
Code Checker Pylint Test

$ make lint 
```

```
Unittest (Mock test) - to lookup if getting expected defination for a valid word or check if its invalid word"

$ make test
```

### Build the package

```
setuptools being used to build the dist locally
Ref - https://setuptools.pypa.io/en/latest/setuptools.html

$ make build

To clean old builds
$ make clean

Dockerize the package - 

If you which run it through container then you can build the App below

$ docker build --tag dictionarytool .


Run it locally 

$ docker run --rm dictionary-tool word api_key

```


### All Make Commands

`install`: Installs the required dependencies specified in `requirements.txt`.

`test`: Runs the pytest framework to execute the tests.

`lint`: Runs pylint to check the code for any potential issues.

`build` : Builds a package to distribute

`clean` : to clean older build and dist package folder

You can use the commands by running `make <command>`.


## Scope of Improvement  / Extra points

- We can use Github actions and create a workflow which will build the image and push it to ecr/docker
- API key can be read from the env var, instead of reading it as an argument 
- Use pipfile/poetry to handle the dependencies 
- Make executable so that it can be run by anyone without the need of cloning the repo and installing dependencies and all
- Add integration tests
