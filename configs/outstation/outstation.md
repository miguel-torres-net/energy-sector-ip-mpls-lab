# Outstation Site Summary

This directory contains the outstation-side gateway IPsec configuration.

## Current artifacts

- Gateway config: `configs/outstation/gw1/swanctl.conf`
- Gateway summary: `configs/outstation/gw1/gw1.md`

## Outstation-side network intent (from current config)

- Site gateway is `gw1` with WAN endpoint `10.100.100.1`.
- Protected local subnet is `172.16.1.0/24`.
- Remote protected subnet is `172.16.2.0/24`.
- Tunnel uses IKEv2 with PSK and starts on matching traffic (`trap|start`).

## Notes

- This repo currently documents the gateway-to-gateway encryption plane for the outstation side.
- CE/outstation host service configs are not yet included in this folder.
