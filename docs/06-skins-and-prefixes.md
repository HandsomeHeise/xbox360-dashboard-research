# Private skins and visual prefixes

A private copy of 291 default dashboard visuals supplies submenu styling. A narrow COLR patch leaves all other bytes identical, preserving classes, bindings, geometry, frame names, animations and actions. This repository describes the technique without distributing the skin.

## Shared palette entries

A light color can serve text, icons and panels simultaneously. Darkening every light value can erase foreground content. The implementation keeps shared foreground entries light and uses targeted runtime contrast for background figures and text.

Check all timeline/state frames, not only initial properties; an animation can restore a native color later.

## Explicit qualification is not inherited lookup

A Visual property can name a private namespace, such as xbOnlineSubmenu. Native list attachment may still reopen a row prototype by visual ID plus inherited prefix before INIT. Qualifying the visible property alone does not satisfy that lookup.

The observed scene wrapper handles GET_VISUALPREFIX before INIT. The associated static 17559 list observations are sub_9220AE80 and sub_92205600. Register classes/visuals in DASH for dashboard scenes; XAM has an independent runtime.

## Scope overrides

Apply a submenu prefix only while an owned session is active and the object/message is valid. Preserve application-specific nonempty prefixes. Replacing every prefix globally can break components that depend on their own visuals.

Guide styles use their own load/reload path. A common palette does not merge DASH and XAM registries.

Test first attachment, focus frames, disabled/pressed states, scrolling/recycled rows, inserted items, modal children and B return. A row can show its background while missing its focus prototype.
