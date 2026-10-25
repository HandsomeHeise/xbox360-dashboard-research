# Custom Home, recent titles and libraries

Custom Home owns presentation, pages and focus. Native services retain title metadata, launch, media state and protected flows. The observed pages cover Home, Social, Games overview, installed games, Music, Video, Apps and Settings.

Ordinary destinations retain a custom return bookmark. Explicit Original entries opt out deliberately. Give those user intents separate handlers.

## Recent model

The default recent limit is 32 games. Deduplicate by title ID, prefer newer timestamps, remove unavailable/untitled records, and sort by last-played time with stable tie order. Preserve selection by title ID on refresh.

A new profile starts a nonzero session generation. Apply only matching snapshots. Requests contain title ID, profile, session and kind (Play/Details); reject stale or unsupported actions. The native bridge rechecks installation/media and owner at dispatch.

This prevents a tile selected for one profile from launching after another signs in. A recent item alone does not establish current installation.

## Installed games and apps

Distinguish content categories, retain stable focus IDs and use real metadata/availability. Enumeration order is not action identity. Handle busy and empty libraries explicitly.

17559 observations include library acquisition/release/busy checks, title resolution, package access and launch; consult the address inventory. Defensive range guards do not prove another build has the same ABI.

## Real actions and input

The public action table records custom-control extension IDs for store/settings routes. They are not Microsoft command IDs or universal ordinals. The existing native control's command, conditions, confirmations and permissions remain authoritative.

Dispatch once after materialization. Test direction/page changes, A/B behavior and controller reconnect. The observed debug input helper uses an edge-detected LB+RB+X chord; it is not a universal dashboard shortcut.

For every new button, document handler, prerequisites, invalidation and hardware result. A label does not prove that its action exists.
