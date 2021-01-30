# Password Generator
A simple python library which allows you generate random passwords with whatever length you wish

## Features

1. Generate more secure passwords
2. Interactive and non-interactive modes
3. You pick the length!
4. Never worry about generating long passwords (with a trick used in it)

Want to have it ? Let's go for installation, don't worry it will be pretty easy

## Installing

Simply clone the repo:

```shell
git clone https://github.com/000Zer000/Password-Generator
```

And **done**!

If the colors doesn't look proprely (seeing things like `[36m`, `[39m` in the text), The below line **will fix** it:

```shell
pip install -r requirements.txt
```
## Usage

**You can use it in three different ways**!

### Use the `non-interactive.py` script

This script accepts an **optional** length as argument (defaults to **13**), This script is usually for usage in other scripts, Examples:

Example 1:
```
python non-interactive.py
IacRaOG2qqIgR 
```

Example 2:
```
python non-interactive.py 15
C2sdWf2qZIgR2L9
```

### Use the `interactive.py` script
This script allows you generate as much as password as you want

```
python interactive.py

[*] Press <enter> for a random password (q for quit, l for changing the length):
[+] Generated 'Af13FaGKC4avJ'
```

You can enter q to exit, If you press `l` then `<enter>` it askes for a newer length

### The third way
There is a python file named `api.py`, You can access the `PasswordGenerator` class to generate a password !

## What trick did you use
Instead of generating the password and storing it inside a **variable** (which would make your computer unusable for lengths big like 10000), Using a `generator` I avoided using **too much memory**

## Technical info about it
To be honest, there is nothing **too much** technical about it but... Anyway

Using the built-in modules (`random`, `string`) We can easily generate a password

The `random` module helps us to choose a random character 
from a list of characters provided by the `string` module (A-Za-z0-9).

With every request for generation, It tries to access `SystemRandom`. A python class which allows 
closer-to-reality random, which is not available on every platform, So if it was not available, We will 
fallback to python's pusedo-random module (`random`) to generate the random password, The password generation process is pretty easy, using either `random.choice` or `random.SystemRandom.choice`, we choose a single character
from the list provided by string, depending on the method of generation (The second one by my srcipts), 
Actions after it differ,

**First method**:

This method is used by other scripts most of the time, For the length times (for example if length is 13, it will choose a random character 13 times), After it got all those characters, Append it to each other, then print it for the user (If the length is 100000 or something big, This method uses too much memory and may cause unusablity of system)

**Second method**:

Nearly same as above, But instead of waiting for all of characters to get generated, then appending them to each other to print, In this method we print them as fast as we generate it, (So no matter how long you define the length, It won't make your system unusable)

## Contacting me

You can reach me by emailing me (`000Zer000@protonmail.com`)

## License

This small repo is licensed under Apache 2.0, Read [COPYING](https://github.com/000Zer000/Password-Generator/blob/main/COPYING) file for more info