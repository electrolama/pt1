# Contributing

pt1 welcomes corrections, test reports, enclosure observations, examples, and
hardware improvements. The review burden should scale with the physical risk of the
change.

## Good first contributions

- reproduce and clarify a setup or troubleshooting step;
- add tested host/driver notes with version information;
- contribute enclosure print settings and fit photographs;
- improve alt text, diagrams, or link quality;
- add a safe example in another serial library; or
- document a measured behavior with the full setup and uncertainty.

## Hardware-change workflow

1. Describe the problem, affected revision, and constraints in an issue.
2. Fork the repository and create a focused branch.
3. Duplicate the relevant revision directory when the physical design changes.
4. Make the smallest coherent source change.
5. Run and record ERC/DRC or mechanical checks.
6. Generate review artifacts without presenting them as a release pack.
7. Prototype and test at a level appropriate to USB and power-path risk.
8. Update documentation, revision notes, and compatibility statements.
9. Open a pull request with evidence and remaining uncertainty.

## Review checklist

### All changes

- [ ] Scope and motivation are clear.
- [ ] Affected revisions are named.
- [ ] Existing user files and unrelated changes are preserved.
- [ ] Documentation links and examples were checked.
- [ ] `mkdocs build --strict` passes.

### Electrical changes

- [ ] ERC/DRC results and approved exceptions are attached.
- [ ] Power-off, startup, fault, and back-power paths were considered.
- [ ] USB 2.0 routing and return paths were reviewed when affected.
- [ ] Absolute maximums, ratings, and component availability were checked.
- [ ] Prototype evidence and test conditions are included.

### Mechanical changes

- [ ] Editable source is included when available.
- [ ] Board, connector, header, and fastener compatibility is stated.
- [ ] Slicer settings and physical fit evidence are included.

## Good problem reports

State the PCB revision, enclosure variant, host OS, cable, power source, target load,
wiring, serial driver/application, expected result, actual result, and exact
reproduction sequence. Include DTR/RI observations for power-control issues and
remove personal or secret information from logs.

## Documentation style

- Write for an experienced maker who is new to pt1.
- Lead with the practical outcome, then explain mechanism and caveats.
- Label measured, calculated, datasheet-derived, and inferred facts.
- Use the signal names present in source files; mention aliases once.
- Include accessible alt text for meaningful images.
- Put new images only under `documentation/assets/images/`.
- Preserve the original assets under `pinout/` unless that pipeline is the explicit
  subject of the change.

The root [CONTRIBUTING file](https://github.com/electrolama/pt1/blob/main/CONTRIBUTING.md)
contains the concise pull-request requirements used on GitHub.

