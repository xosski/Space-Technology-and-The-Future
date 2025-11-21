import svgwrite
import math
import os

output_dir = r"C:\SVGExports"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "phantasmal_sheath_sigil.svg")


# Create the SVG drawing
dwg = svgwrite.Drawing(size=("500px", "500px"), profile='tiny', debug=True)
center = (250, 250)

# Core circle
dwg.add(dwg.circle(center=center, r=40, fill="cyan", fill_opacity=0.9))

# Lattice hexagon
hex_points = []
radius = 100
for i in range(6):
    angle = i * 60 + 30
    rad = math.radians(angle)
    x = center[0] + radius * math.cos(rad)
    y = center[1] + radius * math.sin(rad)
    hex_points.append((x, y))
dwg.add(dwg.polygon(points=hex_points, stroke="white", fill="none", stroke_width=2))

# Energy rings
for r in [90, 150]:
    dwg.add(dwg.circle(center=center, r=r, stroke="skyblue", fill="none", stroke_width=1, stroke_dasharray="3,3"))

# Outer dashed ring (Phantasmal Shell)
dwg.add(dwg.circle(center=center, r=180, stroke="deepskyblue", fill="none", stroke_width=2, stroke_dasharray="5,5"))

# Decorative runes
rune_style = {"stroke": "violet", "fill": "mediumorchid", "stroke_width": 1}
rune_offsets = [(0, -160), (160, 0), (-160, 0), (0, 160)]
rune_shapes = [[(10, 0), (20, 20), (0, 30), (-20, 20), (-10, 0)]]
for dx, dy in rune_offsets:
    shifted = [(x + center[0] + dx, y + center[1] + dy) for x, y in rune_shapes[0]]
    dwg.add(dwg.polygon(points=shifted, **rune_style))

# Label
dwg.add(dwg.text("PHANTASMAL SHEATH", insert=(250, 490), text_anchor="middle",
                 fill="white", font_size="14px", font_family="monospace"))

# Save the SVG to the correct path
output_path = os.path.join(output_dir, "phantasmal_sheath_sigil.svg")
dwg.saveas(output_path)