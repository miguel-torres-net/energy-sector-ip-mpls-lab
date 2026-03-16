# Validation Scenarios (Minimal)

This page tracks baseline test scenarios for the current lab state.

## Scenario 1: SP control-plane convergence

- Goal: ISIS/LDP/BGP VPN control plane converges between `PE1`, `PE2`, and `RR1`.
- Inputs: `configs/service-provider/*.conf`, `configs/service-provider/pe*-junos`.
- Expected result: VRF `OT-WAN` routes can be exchanged between PE nodes via RR.

## Scenario 2: IPsec tunnel establishment

- Goal: Site-to-site IKEv2/IPsec tunnel comes up between `gw1` and `gw2`.
- Inputs: `configs/outstation/gw1/swanctl.conf`, `configs/control-center/gw2/swanctl.conf`.
- Expected result: Child SA `lan-lan` installed for `172.16.1.0/24` <-> `172.16.2.0/24`.

## Scenario 3: End-to-end protected reachability

- Goal: Traffic between outstation LAN and control-center LAN traverses SP and is encrypted at gateways.
- Inputs: scenario 1 + scenario 2 successful.
- Expected result: Bidirectional reachability across protected subnets.
