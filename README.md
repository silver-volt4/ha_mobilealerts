# Home Assistant support for Mobile-Alerts

## Overview

This integration acts as proxy server between the Mobile-Alerts gateway and the cloud. It supports various Mobile-Alerts sensors.

Based on the original integration at [PlusPlus-ua/ha_mobilealerts](https://github.com/PlusPlus-ua/ha_mobilealerts) and the [work of @sarnau](https://github.com/sarnau/MMMMobileAlerts).

## Status

As you may know, PlusPlus-ua's repository has been silent for some years now. The integration is slipping more and more out of touch with Home Assistant's API and does not work on newer versions.

I'm not very experienced with Home Assistant development, but I'll do my best to keep this integration working in between HA updates. Due to my lack of expertise, I will not be working on new features. 

However, I'd still like this repository to be *the* updated fork of the integration, so that those with less computer experience don't have to scour GitHub for working forks. Think of me as a maintainer of this repository for the time being.

If you'd like to see something added and think you can code it yourself, please feel free to submit a PR! For as long as I have access to Mobile-Alerts sensors, I'll review and merge your code.

## Installation

Place the `custom_components` folder in your configuration directory (or add its contents to an existing `custom_components` folder). Alternatively install via [HACS](https://hacs.xyz/).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Silver-Volt4&repository=ha_mobilealerts&category=integration)
