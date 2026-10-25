"""Original SDK-free illustration of virtual source discovery after restoration."""
from dataclasses import dataclass


@dataclass
class NativeHub:
    restored: bool = False
    # Invented arrangement: Bing changes the index of Settings.
    captions: tuple = ("Home", "Bing", "Games", "Settings")

    def indexed_text(self, index, *, item_data):
        if not self.restored or not item_data:
            return None
        return self.captions[index]


def discover(hub, wanted):
    for index in range(len(hub.captions)):
        caption = hub.indexed_text(index, item_data=True)
        if caption and caption.casefold() == wanted.casefold():
            return index
    return None


hub = NativeHub()
assert discover(hub, "Settings") is None
hub.restored = True
assert hub.indexed_text(3, item_data=False) is None
selected = discover(hub, "Settings")
assert selected == 3
print("Restore origin -> read indexed source with item_data=True -> SET_CURSEL", selected)
print("Next: wait for the native target, validate owner/profile, and dispatch once.")
