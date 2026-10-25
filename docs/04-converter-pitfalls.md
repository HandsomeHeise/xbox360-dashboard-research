# Converter pitfalls: layout and allocation

A converter self-roundtrip missed two independent Retail 17559 problems.

## Native layout fields disappear

The XML exporter omitted Row, Column, RowSpan, ColumnSpan, LayoutFloat and LayoutLineBreak from binary layout metadata. Recompilation could retain text and IDs while changing the native grid contract.

Read those fields from original XUR8 DATA with the target class schema. Associate them with stable object IDs and restore them into editable XML before compilation. Reject missing/ambiguous identities. After compilation, read generated DATA independently and compare the entire metadata map.

Forms, storage grids and wizard steps are particularly sensitive. A familiar looking landing page does not establish child-layout correctness.

## Gradient arrays undercount the arena

The inspected converter treats indexed gradient arrays as single properties, while the Retail loader reserves 12 bytes for each compound property. A file can roundtrip through the same converter yet declare too little arena space.

The independent reader calculates required compound-property entries and compares header count slot 3. Missing bytes equal max(0, required - declared) times 12. The related loader observation is sub_92202FC0. This predicts an undersized budget, not an exact crash location.

Repairing a packed integer can change header length. Update total file size and all affected section offsets, then reparse and require zero deficit. Overwriting one byte without accounting for an encoding-width change can corrupt the directory.

## Conversion gate

1. Retain an immutable original and local digest.
2. Export XML and restore native layout metadata.
3. Change only required properties.
4. Compile for the correct schema.
5. Independently check DATA consumption, sections and allocation counts.
6. Compare root/class, bindings/actions and binary layout.
7. Re-export to compare intended editable properties.
8. Pack, reopen and hash-read back members.
9. Perform hardware layout/input acceptance.

For a palette-only skin change, patch COLR in place and require every byte outside that section to remain identical. This avoids lossy reconstruction for that narrow task; it does not validate arbitrary patches.

Run python examples/gradient_budget.py for a small synthetic arithmetic illustration.
