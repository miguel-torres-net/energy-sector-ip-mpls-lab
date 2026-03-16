# Control Center Site Summary

This directory contains the control-center-side gateway IPsec configuration.

## Current artifacts

- Gateway config: `configs/control-center/gw2/swanctl.conf`
- Gateway summary: `configs/control-center/gw2/gw2.md`

## Control-center-side network intent (from current config)

- Site gateway is `gw2` with WAN endpoint `10.200.200.1`.
- Protected local subnet is `172.16.2.0/24`.
- Remote protected subnet is `172.16.1.0/24`.
- Tunnel uses IKEv2 with PSK and starts on matching traffic (`trap|start`).

## Notes

- This repo currently documents the gateway-to-gateway encryption plane for the control center side.
- CE/control-center host service configs are not yet included in this folder.
