# Project_1
Initializating project of a "smart door lock" with internet connection.

There are a bunch of possibilities regarding the evolution of the project, including sms messages, IP cam integration, finger print integration, etc...

The main goal is to communicate it with an IoT cloud service and ensure a safe monitoring in real time to residences and buildings, where, in a safety case, the system shall send a message to cloud and/or throughth an online sms service to chosen people.

## Environment setup
To install all dependencies for this project using included packages on CPython, use the following commands on terminal.

### For development

A virtual environment is recommended, but optional.

- On Windows:
```ps
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements_windows.txt
```
> In Windows, as some required headers files aren't available, GPIOSimulator is used instead of RPi.GPIO to allow development and (limited) testing on this platform.

- On Ubuntu:
```sh
python3 -m venv .venv
source ./.venv/bin/activate
python3 -m pip install -r requirements_others.txt
```
> If `venv` package is missing, use `apt-get update -y && apt-get install -y python3-venv` before

### For execution on Raspiberry
```sh
python3 -m pip install -r requirements_others.txt
```