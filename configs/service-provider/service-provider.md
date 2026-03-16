# Service Provider Configuration Summary

This document summarizes the service provider domain from:

- `configs/service-provider/p1-frr.conf`
- `configs/service-provider/rr1-frr.conf`
- `configs/service-provider/pe1-junos`
- `configs/service-provider/pe2-junos`

## Device roles

| Device | Platform | Role | Router ID / Loopback | AS |
| --- | --- | --- | --- | --- |
| `p1` | FRR 8.4.4 | Core P router | `10.255.0.1` | N/A (no BGP process) |
| `RR1-FRR` | FRR 8.4.4 | Route Reflector | `10.255.0.11` | `65000` |
| `PE1-JUNOS` | Junos 25.4R1.12 | Provider Edge + CE handoff | `10.255.0.101/32` | `65000` |
| `PE2-JUNOS` | Junos 25.4R1.12 | Provider Edge + CE handoff | `10.255.0.102/32` | `65000` |

## Underlay (ISIS + MPLS)

### ISIS core

- Core protocol name is `CORE` on FRR and `isis` on Junos.
- All core nodes are configured as level-2 only:
  - FRR: `is-type level-2-only`
  - Junos: `set protocols isis level 1 disable`
- Loopbacks are passive in ISIS on all nodes.
- Configured ISO NET/NSAP values:
  - `p1`: `49.0001.0000.0000.0002.00`
  - `RR1-FRR`: `49.0001.0000.0000.0011.00`
  - `PE1-JUNOS`: `49.0001.0000.0000.0101.00`
  - `PE2-JUNOS`: `49.0001.0000.0000.0102.00`

### MPLS/LDP

- MPLS is enabled on core-facing interfaces on all SP nodes.
- LDP is explicitly configured on:
  - `p1`: router-id `10.255.0.1`, transport-address `10.255.0.1`, interfaces `ens19` and `ens20`
  - `PE1-JUNOS`: `ge-0/0/0.0`
  - `PE2-JUNOS`: `ge-0/0/0.0`

## BGP control plane

### iBGP route reflection (VPNv4)

- RR is `RR1-FRR` in AS `65000`.
- RR cluster-id: `10.255.0.11`.
- RR clients:
  - `10.255.0.101` (PE1)
  - `10.255.0.102` (PE2)
- Address family used for SP VPN routes:
  - FRR RR: `address-family ipv4 vpn`
  - Junos PEs: `family inet-vpn unicast`

### PE-CE eBGP inside VRF `OT-WAN`

- Both PEs host VRF `OT-WAN`.
- Shared VRF target on both PEs: `target:65000:100`.
- Per-PE route distinguisher:
  - PE1: `65000:101`
  - PE2: `65000:102`
- CE-facing BGP sessions:
  - PE1 VRF group `CE1`: local `10.0.1.0`, neighbor `10.0.1.1`, peer-as `65010`
  - PE2 VRF group `CE2`: local `10.0.2.0`, neighbor `10.0.2.1`, peer-as `65020`

## Interface addressing (from configs)

### PE1-JUNOS

- Core-facing: `ge-0/0/0.0 = 10.0.0.0/31` (inet + iso + mpls)
- CE-facing: `ge-0/0/1.0 = 10.0.1.0/31`
- Loopback: `lo0.0 = 10.255.0.101/32`
- Management: `fxp0.0 = 192.168.1.211/24`

### PE2-JUNOS

- Core-facing: `ge-0/0/0.0 = 10.0.0.3/31` (inet + iso + mpls)
- CE-facing: `ge-0/0/1.0 = 10.0.2.0/31`
- Loopback: `lo0.0 = 10.255.0.102/32`
- Management: `fxp0.0 = 192.168.1.213/24`

### FRR nodes

- `p1` router-id: `10.255.0.1`
- `RR1-FRR` BGP router-id / cluster-id: `10.255.0.11`
- `p1` has ISIS + MPLS on `ens19`, `ens20`, `ens21`
- `RR1-FRR` has ISIS + MPLS on `ens19`

## Operational intent (as configured)

- ISIS provides SP underlay reachability between loopbacks.
- LDP provides MPLS label distribution across the core.
- RR centralizes VPNv4 control-plane exchange between PEs.
- VRF `OT-WAN` stitches CE1 and CE2 routes through the MPLS L3VPN domain.
