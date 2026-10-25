# Status and evidence

Snapshot: 2026-10-25. Target: Retail 17559. Other dashboard versions require separate ABI, schema and ownership verification.

| Evidence level | Establishes | Does not establish |
|---|---|---|
| Static | Source/package/parser/disassembly findings | A path executed on Xbox |
| Host-tested | A contract passed a host fixture | Native timing, GPU output or service availability |
| Build-validated | Conversion, allocation/layout or archive readback passed | A usable scene on hardware |
| Xbox-observed | A specific console interaction/image | Every sibling destination or later build |
| Pending | Further acceptance is required | Completion or necessarily failure |

## Coverage

The retained manifest contains 363 dashboard XUR resources: 117 explicit scene replacements, 4 existing boot/sign-in replacements and 242 awaiting individual review. Among the 117 are 15 helpers, 2 two-pane lists, 1 category sidebar/native option workspace and 99 native forms/grids with custom surfaces. Scoped providers: consoles 59, network 30, memory 22, gamer 5, gamercar 1.

Another addition contains 15 GamerProfile resources. The Guide table now has 72 members, counted separately from dashboard resources. Private hub tabs replace behavior without one-to-one native resource substitution. Never report these figures as numbers of independent menus.

## Verification progression

An earlier checkpoint recorded 142 host tests, an Xbox Release build, 117 scene round trips, allocation/grid checks and archive readbacks. Later route/message regressions brought the reported total to 147 passing host tests. The 147-test suite and Xbox Release/build validation were rerun during publication; hardware acceptance remains separate.

Earlier Xbox feedback showed Settings unavailable before any private scene creation. The native hub exposed virtual channels while Custom owned navigation. A later route still timed out because source text was requested as a control caption. Indexed item text requires bItemData=TRUE. A subsequent System route was Xbox-observed. Older notes saying pending describe earlier stages.

System success does not certify Account, Privacy, Family, network, storage, purchase or online flows. Verify these independently. Application-specific visual prefixes remain separate styling work where needed.

Recent full-screen backdrop/masking changes were deployed; the latest screenshot still showed a duplicate outer header. Visual acceptance remains open. The System overview now keeps native categories on the left and embeds the native Console options in a right-hand tile workspace. Hardware acceptance of this correction is pending. External categories retain their authoritative native application routes. Keep that distinction when describing the project.

Publish sanitized event summaries, never raw console logs, profile IDs or transport endpoints. Record exact tested build, route, language, profile state and remaining unknowns.
