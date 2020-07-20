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

## To Install The Library Locally

Inside the folder containing setup.py
```javascript
python3 setup.py install
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

To Run CLI Commands
```
ttn_cli --help # show all the available options

ttn_cli git --help # shows all the commands related to git

ttn_cli git logs -f <form_date> -a <author-name> show the logs of a particular author

... and many more

ttn_cli network --help # shows all the commands related to network

ttn_cli network show_public_ip # shows public IP of host

ttn_cli network show_private_ip # shows private IP of host
```


For reference, follow this
[article](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html).