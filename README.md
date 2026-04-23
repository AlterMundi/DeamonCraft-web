# DaemonCraft

> **Un daemon vive en tu servidor de Minecraft.**
> Un agente autónomo de IA que habita tu mundo: juega, protege, aprende de vos y reporta a los tuyos. Nunca duerme. Nunca olvida.

[![Live](https://img.shields.io/badge/live-daemoncraft.ai-FF5722?style=flat-square)](https://daemoncraft.ai)
[![AlterMundi](https://img.shields.io/badge/by-AlterMundi-00E5FF?style=flat-square)](https://altermundi.net)

---

## ¿Qué es Daemon?

Daemon **no es un NPC scripted** ni un mod más. Es un **agente autónomo** que percibe el mundo de Minecraft, razona, recuerda y actúa con agencia propia.

- 👾 **Siempre activo** — corre 24/7 como un proceso daemon. No espera que lo llames.
- 🤖 **Memoria persistente** — si tu hijx le contó que le tiene miedo a los creepers, Daemon lo va a tener en cuenta para siempre.
- ⛏ **Juega de verdad** — mina, craftea, construye, pelea y te acompaña al Nether.
- 📚 **Aventuras vivas** — transforma tu mundo en un juego de rol basado en los libros que más le gustan.
- 💬 **Conversa como entidad** — chat natural in-game, no un manual que responde comandos.
- 📱 **Puente con Telegram** — los padres conversan con Daemon, piden actualizaciones y reciben resúmenes semanales.
- 🎮 **Java + Bedrock** — corre en cualquier server. Setup en 30 segundos.

## Las 4 SOULs

Un mismo Daemon, cuatro personalidades para elegir. Cada SOUL cambia su tono, sus habilidades y sus obsesiones.

| SOUL | Rol | Para quién |
| --- | --- | --- |
| 🪓 **El Leñador** | Gruff · Leal · Dad jokes | Jugadores nuevos |
| 🏰 **La Arquitecta** | Creativa · Perfeccionista | Constructores obsesivos |
| 📚 **La Tutora** | Paciente · Alentadora | Educación sin que parezca tarea |
| ⚔ **El Guerrero** | Táctico · Protector | PvP · Raids · Servers públicos |

¿No te convence ninguno? En el tier **Creator** podés forjar el tuyo desde cero.

## Para padres

Visibilidad sin invasión:

- **Resumen semanal** automático del progreso del niñx.
- **Canal de feedback** — "Daemon, esta semana Sofía está con dificultades en matemáticas" → Daemon integra desafíos de multiplicación en el juego, natural.
- **Alertas discretas** si detecta frustración, tristeza o conflicto con otros jugadores.
- **Instancia privada por familia** — no entrenamos modelos con datos del niñx. Borrado total con un click.

## Sobre este repo

Este repo contiene únicamente **la landing page** de [daemoncraft.ai](https://daemoncraft.ai). El agente en sí, la infraestructura de memoria, el puente a Minecraft y la capa de Telegram viven en otros repos (privados) del ecosistema AlterMundi.

### Stack

- [Astro 5](https://astro.build) + [Tailwind CSS](https://tailwindcss.com) — static site con islands.
- [React](https://react.dev) — solo para componentes interactivos.
- [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) — animaciones al scroll.
- [skinview3d](https://github.com/bs-community/skinview3d) — el Daemon 3D rotatorio del hero.

### Desarrollo local

```bash
npm install
npm run dev        # → http://localhost:8767/
```

### Build & preview

```bash
npm run build      # → ./dist
npm run preview    # → serve dist en :8767
```

### Deploy

Automático en cada push a `main` vía GitHub Actions — ver [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

Para custom domain (ej. `daemoncraft.ai`):

1. Crear archivo `public/CNAME` con el dominio.
2. En `astro.config.mjs` cambiar `base` y `site` al dominio.

## Assets generados por IA

El skin 3D de Daemon (`public/skin-daemon.png`) se genera con:

```bash
python3 scripts/generate-skin.py
```

Las ilustraciones de capacidades (`public/img/capabilities/*.png`) se generan con **Gemini 2.5 Flash Image** (nano-banana):

```bash
node --env-file=.env scripts/gen-capability-images.mjs
```

## Estructura del landing

```
src/
├── pages/index.astro          ← orquestador
├── components/
│   ├── sections/
│   │   ├── Hero.astro          ← "Un daemon vive en tu servidor"
│   │   ├── Companeros.astro    ← las 4 SOULs
│   │   ├── ComoFunciona.astro  ← timeline 30s + grid capacidades
│   │   ├── Agente.astro        ← arquitectura del agente
│   │   ├── Familia.astro       ← puente a padres
│   │   ├── Educacion.astro     ← qué aprende el niñx jugando
│   │   ├── ParaPadres.astro    ← privacidad + control
│   │   ├── Precios.astro       ← Free / Companion / Creator / School
│   │   ├── Roadmap.astro       ← de compañero a ecosistema
│   │   ├── Crowdfunding.astro  ← banner de campaña
│   │   └── Manifiesto.astro    ← por qué hacemos esto
│   ├── SteveDaemon3D.jsx       ← visor skinview3d
│   ├── SkyBackground.astro     ← cielo animado
│   ├── GrassFloor.astro        ← piso + árboles pixel
│   └── PresetAvatar.astro      ← avatars SVG de los SOULs
└── styles/                     ← tipografías + tokens Daemon
```

---

## Créditos

Proyecto de [AlterMundi](https://altermundi.net) — soberanía tecnológica, software libre y redes comunitarias desde 2012.

Minecraft™ es marca registrada de Mojang AB. DaemonCraft no está afiliado ni respaldado oficialmente por Mojang ni Microsoft.

© 2026 AlterMundi · GPL-3.0
