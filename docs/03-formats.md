# XUI, XUR8 and XUIZ

| Layer | Role | Common trap |
|---|---|---|
| XUI | XML view of scene/visual objects | Assuming XML retains every binary property |
| XUR8 | Retail compiled UI; XUIB version 8 | Treating a self-roundtrip as loader compatibility |
| XUIZ | Archive container, often named .xzp | Guessing format from the extension |
| Locator | Provider/archive scope and member | Matching only a filename |

The studied builders target Retail XUR8 and use a version-12 XML view. These versions describe different representations. A tool accepting a file does not prove it used the right target schema.

## XUR8 validation

The inspected reader consumes signature/version, total size, allocation counts and a section directory. STRN supplies strings, DATA serialized objects/properties, and COLR palette entries. Packed integers have variable lengths; section offsets must be checked against the actual buffer.

Property masks depend on class inheritance order. Compound properties can be shared. Use the target schema to walk the complete DATA section, verify exact consumption, and count allocations according to loader behavior. The public examples use synthetic values and do not include a retail parser/schema.

## XUIZ observations

The studied builders emit flat, uncompressed version-3 XUIZ archives. Validation checks magic, version, declared size, table bounds, member count, name lengths, payload offsets/lengths and required members before making a cache visible. This does not establish that all XZP containers use this variant. Preserve the original format version and reject unsupported variants.

## Locator semantics

A native request can be section://@0,consoles#SystemScene.xur, or SystemScene.xur with a native base argument. The @ scope denotes a resource/application scope, not a user account. Some providers use nonzero or dynamic scopes.

Private archive locators identify the archive and member. Memory locators also bind the consumer to the backing bytes' lifetime. A live string does not keep freed image/archive bytes valid.

No proprietary resource payload is included here.
