# Exercise Diagram Direction

Standard Physics diagrams should move toward compact, web-native SVG.

Use SVG for recurring diagram families:

- Cartesian axes
- vectors and components
- vector addition
- force diagrams
- electric and magnetic field arrows
- simple ray diagrams
- simple circuits
- qualitative graphs

The target visual contract is:

- compact `viewBox` around meaningful content
- consistent arrowhead size
- standard axis and grid stroke weights
- readable labels using the site typography where possible
- stable vector colors from the Web Clases Rocedg palette
- no large unused canvas areas
- accessible `alt` text or surrounding captions in templates

This branch only improves containment for existing assets. It does not introduce a diagram generation framework or convert the full asset library.
