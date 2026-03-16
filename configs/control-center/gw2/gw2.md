# GW2 IPsec Configuration Summary

This document summarizes `configs/control-center/gw2/swanctl.conf`.

## Connection profile

- Connection name: `gw2-gw1`
- IKE version: `2`
- Local gateway address: `10.200.200.1`
- Remote gateway address: `10.100.100.1`

## IKE authentication

- Local auth method: `psk`
- Local identity: `10.200.200.1`
- Remote auth method: `psk`
- Remote identity: `10.100.100.1`

## Child SA (`lan-lan`)

- Local traffic selector: `172.16.2.0/24`
- Remote traffic selector: `172.16.1.0/24`
- XFRM inbound interface ID: `1`
- XFRM outbound interface ID: `1`
- Start action: `trap|start` (install trap policy and initiate when traffic matches)

## Shared secret mapping

- Secret entry: `ike-gw1-gw2`
- Peer IDs bound to this PSK:
  - `id-gw1 = 10.100.100.1`
  - `id-gw2 = 10.200.200.1`
- Secret value is present in config and currently masked as `"SECRET"`.
