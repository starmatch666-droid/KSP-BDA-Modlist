# Science Lab Auto Transmit

KSP stock science labs stop processing when their output buffer is nearly
full, but they do not transmit the accumulated science automatically. This
small plugin checks every vessel in the save. Loaded labs use the original
`TransmitScience()` method. Unloaded labs are read from their
`ProtoVessel` snapshots and their completed science is settled directly when
the vessel has a science-capable CommNet path and transmitter hardware.

The plugin does not add, duplicate, or modify science. It also does not bypass
CommNet, antenna range, electric charge, or transmission time. A lab is skipped
while it is already transmitting, has no science-capable connection, or has no
available transmitter.

## Default Behavior

- Threshold: 99% of `ModuleScienceConverter.scienceCap`
- Scan interval: every 5 seconds
- Retry interval after a transmission attempt: 20 seconds
- Each science lab is handled independently
- Unloaded-lab transmission: enabled

Stock conversion stops just below `scienceCap`, so the default 99% threshold
is used instead of requiring an exact 100% value. The threshold can be changed
in `ScienceLabAutoTransmit.cfg`.

## Requirements

- KSP 1.12.5
- No Harmony or other plugin dependency

## Install

Copy this repository's
`patches/ScienceLabAutoTransmit/GameData/ScienceLabAutoTransmit` directory into
the KSP installation's `GameData` directory.

The resulting layout is:

```text
GameData/ScienceLabAutoTransmit/
  Plugins/ScienceLabAutoTransmit.dll
  ScienceLabAutoTransmit.cfg
  ScienceLabAutoTransmit.version
```

Restart KSP after installation.

## Configuration

Edit `ScienceLabAutoTransmit.cfg` and restart KSP:

```text
SCIENCE_LAB_AUTO_TRANSMIT
{
    thresholdPercent = 99
    checkIntervalSeconds = 5
    retryIntervalSeconds = 20
    verboseLogging = True
    transmitUnloadedLabs = True
}
```

`thresholdPercent` is clamped to the range 50-99.9 because stock converter
output is normally blocked just below its configured cap.

## Limitations

- Unloaded labs are transmitted by directly settling their persisted
  `storedScience`. This intentionally skips the stock transmission animation
  and transmission-time delay, while still requiring a science-capable
  CommNet path and transmitter hardware.
- The plugin transmits already-accumulated science from unloaded labs. It does
  not replace stock background conversion or add offline science processing
  when the lab has not accumulated science in its persisted buffer.
- A lab without a science-capable CommNet path waits silently and retries on a
  later scan.
- Transmission is still asynchronous and retains the stock antenna range,
  electricity, and transmission behavior.

## Build

From the patch directory:

```powershell
.\Source\build.ps1
```

The script compiles against the local KSP 1.12.5 assemblies and deploys the
plugin to the local KSP `GameData` directory.
