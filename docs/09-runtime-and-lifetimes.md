# UI thread, ownership and lifetimes

## Tree mutation

Create, attach, reorder and destroy on the UI path outside render traversal. Frame-start polling can miss a scene created later in that frame. A successful creation hook can prepare known roots before first render, while excluding private backdrop roots to avoid recursion.

Render hooks should inspect/change verified draw state, not rebuild the tree. Bound ancestry/child walks and guard invalid handles and cycles.

## Invalidation

Title/dashboard changes invalidate native handles. A nonzero address can become stale after unload. Resolve dynamic modules again. Profile changes invalidate action requests and return intent.

Carry owner, profile snapshot and session generation through asynchronous work. Recheck them at dispatch and handle controller disconnect/ownership explicitly.

## Copy data, not native pointers

The recent model contains title IDs, timestamps, strings, artwork locators and availability flags. Reacquire and validate native title records for dispatch. Bound lengths/counts; reject range arithmetic overflow and check every page crossed by native data.

Acquire/release the native library, wait while busy and verify active owner. Host fixtures can prove stale-session rejection but cannot certify native object lifetime across frames.

## Memory-backed artwork

XUI can retain a memory locator beyond scene closure. The inspected bridge copies pixels to a pinned system-heap cache bounded to 8 MiB for the client lifetime. Copied bytes outlive Close/Reset; native title pointers do not cross that boundary.

Do not free backing pixels when Home closes. Retention must still be bounded and deduplicated, with shutdown ownership defined. Keeping the locator string alive does not preserve freed bytes in a title heap.

On partial creation, destroy only valid objects you own. Cancel pending routes on timeout/profile/title invalidation and retain a visible Original recovery route. Missing caches must not trap the user behind a blank cover.
