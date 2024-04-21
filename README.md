# WiggleSoilTemperature

## Prepare Raspberry PI

You will need to enable the Raspberry PI to gather ds18b20 data

https://raspberrytips.nl/ds18b20-raspberry-pi/

## Via CLI

Run `wiggle-soil-temperature` to gather soil temperature sensor data

```
wiggle-soil-temperature
```

## Install WiggleSoilTemperature service

In the terminal run `wiggle-soil-temperature-install`. This will install and start a service which runs `wiggle-soil-temperature` on boot.

```
wiggle-soil-temperature-install
```


You can check the status with:

```
systemctl --user status wiggle-soil-temperature.service
```

To stop the service run:

```
systemctl --user stop wiggle-soil-temperature.service
```

To start the service run:

```
systemctl --user start wiggle-soil-temperature.service
```

## Installation for development

Updating packages on Raspberry Pi
```
pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
apt-get install libjpeg-dev zlib1g-dev
```

Installing package
```
pip3 install -e .
```

For installation without dev dependencies
```
pip install --no-dev -r requirements.txt
```