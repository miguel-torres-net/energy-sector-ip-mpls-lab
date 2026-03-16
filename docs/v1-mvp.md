# V1 MVP Scope (Minimal)

## Objective

Deliver a working lab path between outstation and control center with:

- MPLS L3VPN transport in the service-provider domain.
- IPsec site-to-site protection between gateways.

## In-scope components

- Service provider configs:
  - `configs/service-provider/p1-frr.conf`
  - `configs/service-provider/rr1-frr.conf`
  - `configs/service-provider/pe1-junos`
  - `configs/service-provider/pe2-junos`
- Gateway configs:
  - `configs/outstation/gw1/swanctl.conf`
  - `configs/control-center/gw2/swanctl.conf`

## MVP acceptance criteria

- PE and RR VPN control plane is established for VRF `OT-WAN`.
- IPsec child SA `lan-lan` is established between `gw1` and `gw2`.
- Subnet traffic `172.16.1.0/24` <-> `172.16.2.0/24` is reachable through encrypted gateways.
