# MechJeb Infinite Fuel

MechJeb 2.15.x calculates maneuver-node burn timing from finite
`StageStats/VacStats`. KSP's `Infinite Propellant` cheat is not considered by
that calculation, so a burn which can physically continue for 30 minutes may
be reported as only a few seconds long. The node executor then warps to the
wrong ignition point.

This small Harmony plugin fixes only that calculation. When KSP's
`CheatOptions.InfinitePropellant` is enabled, it computes:

```text
total burn time = node delta-v / current limited maximum acceleration
ignition time   = node time - total burn time / 2
```

The vessel mass is treated as constant because the infinite-propellant cheat
keeps the resource amounts full. When the cheat is disabled, MechJeb's original
finite-fuel calculation is used unchanged.

## Requirements

- KSP 1.12.5
- Harmony 2
- MechJeb2 2.15.x

## Install

Copy this directory's `GameData/MechJebInfiniteFuel` directory into the KSP
installation's `GameData` directory:

```text
GameData/MechJebInfiniteFuel/Plugins/MechJebInfiniteFuel.dll
```

Restart KSP after installing.

## Use

1. Enable KSP's `Infinite Propellant` cheat.
2. Create a maneuver node.
3. In MechJeb's Node Executor, check `Node Burn Length` and
   `Node Burn Countdown`.
4. Enable `Autowarp`; MechJeb should now warp toward the real half-burn point.

The stock KSP Maneuver Tool can still display its own finite-fuel estimate.
Use MechJeb's patched Node Burn Length for execution. Very long burns should be
executed with physical time warp; the current Better Time Warp profile provides
4x, 8x, and 12x physics warp.

## Build

Run:

```powershell
.\Source\build.ps1
```

The script uses the local KSP 1.12.5 assemblies, builds the DLL, and copies it
to `GameData/MechJebInfiniteFuel/Plugins`.

## Scope

This is intentionally narrow. It does not change thrust, Isp, mass,
propellant consumption, MechJeb's node solver, or normal finite-fuel behavior.
