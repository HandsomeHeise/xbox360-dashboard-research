# Rendering fills, focus and restoration

DASH and XAM have separate XUI implementations. Use the corresponding runtime's classes, messages, brushes and visuals. An SDK wrapper can accidentally link a second runtime even when its types compile.

## Compose after native BeginRender

Native BeginRender/theme composition can reset the color factor. Apply final tint after native composition and preserve native fade alpha. A gradient figure receives RGB from its brush; multiplying the same colors into its draw factor distorts the gradient.

Identify actual figure/text/image classes before applying a style. A generic control is not necessarily a drawable fill. Use bounded ancestor matching to select targets and clear per-draw pending state.

Solid, linear and radial brushes have distinct construction/transform paths. Destroy them through the correct runtime when no consumer retains them.

## EndRender restoration

The verified common render-message prefix includes the drawing context and color factor. Do not overwrite the larger private retail state with an SDK-sized approximation. EndRender restores the previous factor.

For render masking, make the current draw transparent while retaining controls/timelines for navigation and data. Pair Begin/End behavior on every path; otherwise colors can leak into siblings or nested draws.

## Focus is more than a color

Focused/selected/pressed/disabled controls can change frames, animation or prototype. Test recycled list rows and child return, not just the initial screen. Private decoration must be non-hittable.

Shared palette entries require targeted contrast. Scope overrides to owned submenu sessions; common IDs can also exist on unrelated screens.

Mask the native homepage only while a valid private cover exists. Missing cover, invalidation or timeout must release the mask to a usable UI. The duplicated outer header is still an open cosmetic finding; broad masks can hide needed confirmations/status, so locate the actual host first.
