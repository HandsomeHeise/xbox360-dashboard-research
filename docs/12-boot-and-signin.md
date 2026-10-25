# Boot loading, sign-in avatars and handoff

Startup presentation substitutes a custom loading scene plus profile, empty/action and skip sign-in slot resources. Match signinpr scope as well as the member. Another package's similar filename must not be intercepted.

Keep native sign-in controller, profile selection and actions. Avatar-related native state can continue behind custom surfaces/ribbon/headings. A custom background does not implement an avatar renderer or sign-in service.

## Motion and selection

The loading replacement explicitly finds its animation object and starts the timeline. Creation without working animation is failure: fall back to the native loader. Verify loop and transition timing on hardware.

Sign-in ribbon positioning is bounded and windows around selection when more than five slots exist. Retain native slot-to-profile/action identity; do not reorder by visible label alone.

## Boot handoff

The native avatar hub can appear between loading completion and private backdrop attachment. A boot-only bridge masks it only with a valid cover. The eight-second timeout begins with the first masked frame, not while loading is still active.

Release the bridge when the backdrop attaches or timeout expires. A failed resource must leave usable native UI. Reset state at lifecycle boundaries.

Prepare known hub/home/template/slot roots before first render. Mutate the tree outside rendering; masking changes drawing only. Header clones must use runtime/localized text.

A later substitution failure should stop new replacements without undoing valid existing private slot layout. A total reset is different: all retained handles must be invalidated.

Check cold boot, auto-sign-in, signed-out startup, multiple profiles, skip, profile switch, failed cache and reconnect. Inspect a transition sequence: one final screenshot cannot establish the absence of a native flash or stalled handoff.
