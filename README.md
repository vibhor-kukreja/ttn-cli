# ttn-cli
Basic CLI utility

## To make build

Make sure you have the latest versions of setuptools and wheel installed:

```javascript
python3 -m pip install --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```javascript
python3 setup.py sdist bdist_wheel
```

## To Run In Development Mode

Setup a virtual environment to install the package
```
virtualenv venv -p python3.6
```

Then to install the package in development mode
```
python setup.py develop
```

To enter shell
```
ttn_cli
```

For reference, follow this
[article](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html).
