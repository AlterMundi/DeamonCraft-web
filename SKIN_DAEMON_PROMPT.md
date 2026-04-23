# Prompt para Generar Skin 3D de Daemon

> Para usar con Gemini 2.5 Flash Image (nano-banana) o Stable Diffusion / DALL-E
> Formato final: PNG 64x64px (pixel art) o 128x128px (skinview3d compatible)

---

## Prompt Principal

```
Minecraft skin, front view, full body, 64x64 pixels.

Character: "Daemon" — an autonomous AI entity that lives inside Minecraft servers.

Design specs:
- Color palette: deep void black (#0B0C15) as base, with daemon orange (#FF5722) accents on chest emblem and eyes, cyan (#00E5FF) circuit-like patterns on arms and legs.
- Head: dark hood or helmet with glowing cyan eyes and subtle orange trim. Mysterious but not evil.
- Torso: black base with an orange "D" rune or daemon symbol on the chest. Cyan circuit lines pulsing from the center.
- Arms: dark with cyan digital patterns (like traces on a circuit board). Right hand slightly brighter (active state).
- Legs: dark boots with orange accents. Cyan lines running down the sides.
- Back: minimal design, a subtle orange glow at the center (daemon core).
- Style: faithful to Minecraft aesthetic but clearly unique and memorable. Not a generic Steve reskin.
- Mood: powerful, always-active, guardian-like, tech-mystical.

No background. Transparent or flat color. Crisp pixel edges. Minecraft skin format.
```

---

## Variantes por SOUL

### Leñador (Lumberjack SOUL)
```
Same Daemon base skin but with:
- Red plaid shirt texture over black torso
- Denim-like blue pants
- Axe held in hand (if possible in skin format)
- Slightly rugged, outdoorsy look
- Orange accents maintained for brand consistency
```

### Arquitecta (Architect SOUL)
```
Same Daemon base skin but with:
- White hard-hat or engineer cap
- Blueprint-style cyan patterns more geometric
- Clean lines, symmetrical design
- Subtle gold/orange measuring tape detail
```

### Tutora (Tutor SOUL)
```
Same Daemon base skin but with:
- Glasses (pixel art style)
- Book or scroll held in hand
- Softer cyan glow (less aggressive)
- Warm orange accents suggesting patience
```

### Guerrero (Warrior SOUL)
```
Same Daemon base skin but with:
- Light armor plates on shoulders
- Sword or shield detail
- More aggressive orange glow
- Scar or battle marks (subtle)
```

---

## Especificaciones Técnicas

| Parámetro | Valor |
|---|---|
| **Resolución** | 64x64 px (estándar Minecraft) o 128x128 px (HD) |
| **Formato** | PNG con transparencia |
| **Color depth** | 8-bit o 24-bit |
| **Naming** | `skin-daemon.png` (base), `soul-lumberjack.png`, `soul-architect.png`, etc. |
| **Viewer test** | Cargar en skinview3d para ver rotación 3D antes de deploy |

---

## Post-proceso sugerido

1. Generar con IA
2. Pasar por un pixel art upscaler si es necesario (pero mantener estética Minecraft)
3. Verificar que los ojos sean claramente visibles y expresivos
4. Test en skinview3d con fondo oscuro (#0B0C15)
5. Ajustar brillo si el glow naranja/cyan no se lee bien en 3D

---

## Referencias visuales sugeridas

- Minecraft skins: Technoblade, Dream (para iconicidad)
- Cyberpunk aesthetics: circuit patterns, neon accents
- Dark souls / Hollow Knight: hooded mysterious figures
- Tron: cyan/orange digital lines on black

---

*Prompt preparado por DaemonCraft / AlterMundi — Abril 2026*
