## Sorting App

### 1. Create Virtual Environment
Install `pipenv` package
Go to the root folder **mp_sort**
``` 
> cd %USERPROFILE%\Downloads\d2w_mini_projects\mp_sort
pip install --user pipenv
```

If you are running the above commands in Vocareum, you may encounter the following message at the end of the installation.

```
WARNING: The script virtualenv is installed in '/voc/work/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The scripts pipenv and pipenv-resolver are installed in '/voc/work/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

It is basically saying that you need to add the newly installed pipenv program into the PATH so that you can use it from anywhere in the terminal. To do that, run the following command in the terminal.
```
export PATH='/voc/work/.local/bin':$PATH
```

From the root folder `mp_sort`, install packages specified in the `Pipfile`.
```
pipenv install
pipenv shell
```

### 2. Using Transcrypt
Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use Transcrypt library which can compile and translate Python script into a Javascript file. To compile library.py, first we need to go into the static folder.
```
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort\app\static
> dir
```

The output should be like the following:
```
library.py
```

Run Transcrypt on `library.py`:
```
python -m transcrypt -b -n library
```

The option -b means to build the javascript library. Once it is done, you should be able to see a folder called __target__ containing several files. To see the content of that folder:
```
> dir
> dir __target__
```

The output should be like the following:
``` __target__/
library.js
library.project
math.js
org.transcrypt.__runtime__.js
random.js
```

You should see `library.js` created inside this folder.


### 3. Run Flask
```
flask run
```

The output should be like the following:
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. 
To stop the web app, type `CTRL+C`.


### In `ex1.html`
### Task 1: Generate Random Integers
The event `onclick` is binded to the function `generate()` in your `library.py`. Fill in this function to do the following:
- generate 10 random integers and store it into the global variable `array`,
- create a single string containing all the numbers. For example, `3, 1, 2, 4, 8, 6, 5, 9, 0, 7.`

### Task 2: Sorting Numbers
The event `onclick` is binded to the function `sortnumber1()` in your `library.py`. Fill in this function to do the following:
- get the random numbers from `generate` HTML id. Hint: use `document.getElementById(id).innerHTML` to get the numbers,
- remove the other characters and create a list of integers called `sortedarray`,
- sort the list using either bubble sort or insertion sort,
- create a single string containing the sorted numbers.


### In `ex2.html`
### Task 3: Creating a Text Input
In this exercise, instead of randomly generate the numbers, you will ask the user to enter the sequence of numbers using a Text Input.

### Task 4: Sorting User Input
This button's event `onclick` is binded to `sortnumber2()` function in your `library.py`. Modify that function to do the following:
- get the string from the text input stored in the variable `value`,
- split the string using comma as a separator,
- remove all trailing whitespaces and convert them to numbers,
- sort the list of numbers,
- create a single string containing the sorted numbers and store it to `array_str`.






