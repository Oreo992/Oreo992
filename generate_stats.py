import json

with open("stats.json") as f:
    s = json.load(f)

def fmt(n):
    if n >= 1_000_000: return f"{n/1_000_000:.2f}M"
    if n >= 1_000: return f"{n/1_000:.1f}K"
    return str(n)

tokens     = fmt(s["tokens_consumed"])
projects   = str(s["projects_built"])
prompts    = fmt(s["prompts_written"]) + "+"
agents     = str(s["agents_deployed"])
memory     = str(s["memory_systems"])
models     = "  ·  ".join(s["models_used"])
year       = s["year"]

W, H = 820, 300
ORANGE = "#f4a261"
AMBER  = "#e9c46a"
DIM    = "#6b4e2a"
BG     = "#1a0f05"
CARD   = "#231508"
BORDER = "#3d2410"
WHITE  = "#f5ede0"
MUTED  = "#a07850"

def stat_block(x, y, label, value, color=ORANGE):
    return f"""
    <rect x="{x}" y="{y}" width="150" height="80" rx="8"
          fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
    <text x="{x+75}" y="{y+34}" text-anchor="middle"
          font-family="monospace" font-size="26" font-weight="bold" fill="{color}">{value}</text>
    <text x="{x+75}" y="{y+58}" text-anchor="middle"
          font-family="monospace" font-size="10" fill="{MUTED}" letter-spacing="0.5">{label}</text>
    """

svg = f"""<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{BG}"/>
      <stop offset="100%" style="stop-color:#120a02"/>
    </linearGradient>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{ORANGE};stop-opacity:0"/>
      <stop offset="50%" style="stop-color:{ORANGE};stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:{ORANGE};stop-opacity:0"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#bg)" rx="14"/>
  <rect width="{W}" height="{H}" fill="none" stroke="{BORDER}" stroke-width="1" rx="14"/>

  <!-- Glow line -->
  <rect x="60" y="56" width="700" height="1" fill="url(#glow)"/>

  <!-- Title row -->
  <text x="40" y="38" font-family="monospace" font-size="11"
        fill="{MUTED}" letter-spacing="2">✦  {year} · AI WRAPPED</text>
  <text x="{W-40}" y="38" text-anchor="end" font-family="monospace"
        font-size="11" fill="{DIM}" letter-spacing="1">Jeffrey / Oreo992</text>

  <!-- Hero: Tokens -->
  <text x="40" y="110" font-family="monospace" font-size="11"
        fill="{MUTED}" letter-spacing="1">TOKENS CONSUMED</text>
  <text x="40" y="158" font-family="monospace" font-size="56"
        font-weight="bold" fill="{ORANGE}">{tokens}</text>
  <text x="228" y="158" font-family="monospace" font-size="14"
        fill="{AMBER}">tokens</text>

  <!-- Divider -->
  <line x1="310" y1="72" x2="310" y2="230" stroke="{BORDER}" stroke-width="1"/>

  <!-- Right grid -->
  {stat_block(330,  72, "AI PROJECTS", projects, ORANGE)}
  {stat_block(490,  72, "PROMPTS", prompts, AMBER)}
  {stat_block(650,  72, "AGENTS", agents, ORANGE)}

  {stat_block(330, 162, "MEMORY SYS", memory, AMBER)}

  <!-- Models block -->
  <rect x="490" y="162" width="310" height="80" rx="8"
        fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
  <text x="645" y="196" text-anchor="middle"
        font-family="monospace" font-size="10" fill="{MUTED}" letter-spacing="0.5">MODELS USED</text>
  <text x="645" y="222" text-anchor="middle"
        font-family="monospace" font-size="11" fill="{ORANGE}">{models}</text>

  <!-- Footer -->
  <text x="{W//2}" y="{H-14}" text-anchor="middle"
        font-family="monospace" font-size="9" fill="{DIM}"
        letter-spacing="1">· memory is what makes us real ·</text>
</svg>"""

with open("stats.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("stats.svg generated.")
