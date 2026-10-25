# Xbox 360 dashboard research

Practical research on dashboard UI reconstruction and native integration, focused on **Retail 17559**. This repository explains the discoveries, earlier failure modes, and how to apply the findings in your own development environment.

This is a research handbook, not a replacement dashboard distribution. It contains original documentation, resource names, build-specific address observations and small independent examples. It includes no Microsoft system binaries, SDK files, retail UI assets, private client implementation or console logs.

## Start here

| Your goal | Read |
|---|---|
| Understand scope and current results | [Status and evidence](docs/01-status-and-evidence.md) |
| Make a first local experiment | [How to use](docs/02-how-to-use.md) |
| Decode, edit and validate UI | [Formats](docs/03-formats.md), [converter pitfalls](docs/04-converter-pitfalls.md) |
| Replace a scene and preserve its children | [Provider routing](docs/05-provider-routing.md), [scene contracts](docs/07-scene-contracts.md) |
| Style controls and focus | [Skins](docs/06-skins-and-prefixes.md), [rendering](docs/08-rendering-and-focus.md) |
| Build Home and route real actions | [Home/libraries](docs/10-home-and-libraries.md), [native actions](docs/11-native-actions.md) |
| Study startup or the Guide | [Boot/sign-in](docs/12-boot-and-signin.md), [Guide](docs/13-guide.md) |
| Validate and investigate failures | [Verification/deployment](docs/14-verification-and-deployment.md), [troubleshooting](docs/15-troubleshooting.md) |

Also read [runtime ownership](docs/09-runtime-and-lifetimes.md), the [glossary](GLOSSARY.md), [evidence map](EVIDENCE.md), and [contribution guide](CONTRIBUTING.md).

## Current scope

The evidence includes custom Home/Social/Games/Music/Video/Apps/Settings pages, profile-aware recent titles and installed libraries, boot/sign-in replacements, a private submenu skin, 117 scoped dashboard resource replacements and 72 Guide scene members. **363 dashboard XUR resources does not mean 363 menus.** The inventory includes helpers, slots, skins and wizard steps.

The latest reported implementation checkpoint is **148 passing host tests**. System navigation was observed on an earlier deployed Xbox build after fixing virtual Twist source selection. Many individual scenes and service-dependent actions still need hardware acceptance. Recent full-screen backdrop/masking cosmetics were deployed, but the latest screenshot still showed a duplicated outer header. The System overview now keeps native categories on the left and embeds the native Console options in a right-hand tile workspace. Hardware acceptance of this correction is pending. External categories retain their authoritative native application routes.

## Try the examples

With Python 3, from this repository:

```text
python examples/inspect_inventory.py
python examples/route_model.py
python examples/gradient_budget.py
```

These inspect research data or model a contract. They do not connect to a console, use an SDK or build a dashboard. The numbered guides describe integration with resources you supply independently.

Machine-readable references: [resources](data/resource-inventory.json), [17559 addresses](data/retail17559-addresses.json), [action IDs](data/action-ids.json), [evidence records](data/evidence.json). Verify artifact identity, instructions and ABI before using any address.

Original material is [MIT licensed](LICENSE). This grants no rights to third-party binaries, artwork, SDK components or trademarks. Xbox is a Microsoft trademark; this project is independent.
