# HAY Smart Home & Lock Service
> HAY is a smart home and lock device which is capable of managing Internet Of Things (IOT) devices in the house and door. Our project utilises AWS cloud services, including but not limited to, AWS Rekognition, deploying web servers, S3 buckets.

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

The purpose of our project is to create a home device that would interface with IOT devices with useful applications to any households. In the past, home owners were not able to have constant surveillance at the doorstep. However with HAY, home owners will be able to view any visitors or delivery men outside of their door upon a ring of a door bell. Home owners also frequently forget to close their windows resulting in rain pouring in on one unlucky afternoon. However, with our rain detector IOT device, upon detecting raindrops it will automatically close the windows of the house. Our solution makes use of AWS cloud solutions to conduct communications between the Raspberry PI and Python web server as well as utilises many other services in AWS.
![](header.png)

## Table of Content
- [Installation](#Installation)
  * [Sub-heading](#sub-heading)
    + [Sub-sub-heading](#sub-sub-heading)
- [Usage](#Usage)
  * [Sub-heading](#sub-heading-1)
    + [Sub-sub-heading](#sub-sub-heading-1)
- [Development Setup](#Development Setup)
  * [Sub-heading](#sub-heading-2)
    + [Sub-sub-heading](#sub-sub-heading-2)





## Installation

Raspberry Pi:

```sh
git clone https://github.com/potatoFry/IOTAssignment_2
```

Python Flask Server (Linux Machine):

```sh
git clone https://github.com/potatoFry/IOTAssignment_2
```

## Usage

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development Setup

To utilise the application, we will need 1 Raspberry Pi as well as create a EC2 instance with a Linux operating system. The Raspberry Pi will be used to publish real time values such as temperature and humidity, as well as subscribed to topics that will change the LED screen. The EC2 instance will be used to run a python web server which allows users to view real time values from the Raspberry Pi as well as historic values. The python web server allows users to change and edit the LCD screen of the Raspberry Pi as well as.

Python Flask Server
```sh
python3.8 -m web-venv ~/WebServerDirectory #creating a virtual environment
source ~/WebServerDirectory/web-venv #activate the virtual environment
pip3 install boto3 flask AWSIoTPythonSDK
```

Raspberry Pi
```sh
python3.8 -m web-venv ~/RaspberryPiDirectory #creating a virtual environment
source ~/RaspberryPiDirectory/web-venv #activate the virtual environment
pip3 AWSIoTPythonSDK botocore awscli
```
## Physical Setup

The following parts were used in this project:

* DHT11
* Button
* I2C 16x2 LCD Screen
* YL-83 Rain Sensor - Control Board
* YL-83 Rain Sensor - Detection Board
* Tower Pro SG90 Servo
* One 330Ω and 10kΩ resistor
* Sufficient Wires

To emulate the project, you can set up the breadboard according to the diagram below.

![Fritzing Diagram](https://github.com/potatoFry/IOTAssignment_2/blob/main/[filename]?raw=true)

## Network Setup
* Raspberry PI
* EC2 Linux Machine
* MQTT AWS Broker



## AWS Functionalities

One of the objectives of this project was to make use of AWS cloud services to learn of their functionalities. The following are the various functionalities we have used and what they were used for.

* IOT Core
* S3
* AWS Rekognition
* Dynamodb
* EC2
* Simple Notification System


## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki


