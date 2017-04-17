Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_
and this project adheres to `Semantic Versioning <http://semver.org/>`_. This
project defines the API as the set of high-level functions performed by the
user. For example, 1.0.0 will have three capabilities: impedance testing,
TS fitting of speaker data, and modeling of speaker performance using TS
parameters. Any adition to removal of high-level capabilities would be a change
to the API.


Unreleased
~~~~~~~~~~
Added
^^^^^

- Daily Debian Packaging and Windows AppVeyor builds (triggered by [build] in
  commit tag)
- Impedance tester works!

Changed
^^^^^^^

- More stable and accurate impedance fitting algorithm
- Fitting algorithm now uses frequency dependent Re and Le
- Updated to Qt5
- Lots of visual formatting & UI improvements
- Moved user data from AppDataLocation to DocumentsLocation

Removed
^^^^^^^

- none

0.0.1 - 2017-03-23
~~~~~~~~~~~~~~~~~~
Added
^^^^^

- Speaker Modeler:

  - "holding" plots so you can see more than one speaker's model at a time

- Impedance Fitter

  - Includes frequency dependent Re and Le
  - Exporting fit data to speaker modeler

0.0.0 - 2016-03-21
~~~~~~~~~~~~~~~~~~
Added
^^^^^

- Speaker Modeler

  - Input any T/S, Qs, and box parameters and it will calculate and plot
    theoretical impedance & SPL
  - Can calculated B2 closed box and QB3-B4-C4 ported enclosure parameters from
    T/S
  - Save/Load driver specification files
  - Save/Load impedance magnitude and phase data as ZMA/ZDA files

- Impedance Tester

  - can output a chirped sine wave from 20Hz to 20kHz to any available output
    device. (Turn down your speaker volume if you are testing this on amplified
    speakers, this is intended for circuit testing not for listening -- although
    you can listen to it.)
  - Simultaneously records two-channel input data from any input device while
    chirped sine is played. Calculates and displays frequency components of one
    of the channels
