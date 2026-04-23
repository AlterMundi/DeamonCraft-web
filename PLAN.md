# DaemonCraft — Plan Maestro Multi-Agente

> **Versión:** 1.0  
> **Última actualización:** 22 Abril 2026  
> **Estado:** En construcción activa  
> **Filosofía:** Este documento es un sistema vivo. Se actualiza cada vez que un agente completa, descubre o redefine una tarea. Pensamos en paralelo, no en serie.

---

## 1. Visión del Proyecto

**DaemonCraft** es un agente autónomo de IA que vive dentro de servidores de Minecraft.

- **No es un mod.** Es una entidad cloud-native que se conecta a cualquier servidor Java/Bedrock.
- **No es un bot.** Es un compañero con personalidad persistente, memoria entre sesiones y capacidad de razonar sobre el mundo del juego.
- **No es solo para gamers.** Es una puerta de entrada a la educación, la creatividad y la supervisión parental en entornos digitales.

### El Nombre

`Daemon` tiene triple resonancia intencional:

1. **Técnica:** En sistemas Unix, un *daemon* es un proceso persistente que corre en segundo plano. Es exactamente lo que hace nuestro agente.
2. **Mitología:** El *daemon* de Sócrates era un espíritu guía, una voz interior. Hermes, mensajero de los dioses, conectaba mundos — como nuestro agente conecta Minecraft con el mundo real (padres, educadores).
3. **Gaming:** *Daemon* resuena en Doom, Warhammer 40K, Diablo — universos donde los daemons son entidades poderosas, persistentes y memorables.

**Craft** viene de Minecraft, pero también de *craftsmanship* (artesanía), *witchcraft* (magia), y *aircraft* (algo que vuela, que tiene autonomía).

---

## 2. Arquitectura Multi-Agente del Plan

No trabajamos en serie. Trabajamos como un *swarm* de agentes especializados que operan en paralelo, con sincronización en puntos clave.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DAEMONCRAFT SWARM                                   │
├─────────────┬─────────────┬─────────────┬─────────────┬─────────────────────┤
│   AGENTE    │   AGENTE    │   AGENTE    │   AGENTE    │      AGENTE         │
│   PRODUCTO  │   MARCA     │   GROWTH    │   TECH      │      COMUNIDAD      │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────────────┤
│ • Core AI   │ • Identidad │ • Marketing │ • Backend   │ • Discord/Reddit    │
│ • SOULs     │ • Web       │ • Ventas    │ • Infra     │ • Soporte           │
│ • Gameplay  │ • Contenido │ • PR        │ • Seguridad │ • Feedback loop     │
│ • Features  │ • Narrativa │ • BD        │ • DevOps    │ • Beta testers      │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   AGENTE ORQ     │
                    │  (coordinación)  │
                    └──────────────────┘
```

### Definición de Agentes

| Agente | Responsabilidad | Estado | Líder (humano) |
|--------|----------------|--------|----------------|
| **Producto** | Roadmap de features, SOULs, gameplay loop, UX in-game | 🟡 Activo | Nico |
| **Marca** | Identidad visual, copy, web, narrativa, vídeo | 🟡 Activo | Nico + diseñadores |
| **Growth** | Adquisición, retención, marketing, ventas, partnerships | 🟡 Activo | Nico + community |
| **Tech** | Backend, IA, infra, seguridad, DevOps | 🔴 En definición | Nico + devs |
| **Comunidad** | Discord, beta testers, soporte, feedback loop | 🟡 Activo | Nico |
| **Orquestador** | Sincronización entre agentes, priorización, resolución de conflictos | 🟡 Activo | Nico |

**Leyenda:** 🟢 Completado / 🟡 Activo / 🔴 Pendiente / ⚪ No iniciado

---

## 3. Estado Actual por Agente

### 3.1 AGENTE PRODUCTO

**Objetivo:** Definir qué es DaemonCraft, para quién, y qué hace.

#### Completado ✅
- [x] Definición del concepto central: agente IA autónomo en Minecraft
- [x] Sistema de SOULs: 4 personalidades base (Leñador, Arquitecta, Tutora, Guerrero)
- [x] Identificación de 4 segmentos de cliente:
  - Jugadores individuales (free tier)
  - Familias (Companion tier)
  - Creadores (Creator tier)
  - Escuelas/Clubes (School tier)
- [x] Modelo de precios: Free / $5 / $15 / $99 mensual
- [x] Diferenciadores clave:
  - Persistencia (nunca duerme)
  - Memoria entre sesiones
  - Bridge Telegram (reportes a padres)
  - Guardian Mode (seguridad en servidores públicos)
  - Custom SOULs (fine-tuning)

#### En Progreso 🟡
- [ ] Definir feature set específico del MVP (v0.1)
- [ ] Documentar arquitectura técnica del agente
- [ ] Definir protocolo de comunicación Minecraft ↔ Agent
- [ ] Especificar sistema de memoria (qué recuerda, por cuánto tiempo)
- [ ] Definir límites de acciones por tier
- [ ] Diseñar flujo de onboarding del usuario

#### Pendiente 🔴
- [ ] Prototipo jugable mínimo (agente que se conecta y responde)
- [ ] Sistema de reportes para padres (qué datos, cómo se presentan)
- [ ] Guardian Mode (detección de lenguaje inapropiado, escolta)
- [ ] Marketplace de SOULs (Creator tier)
- [ ] Dashboard pedagógico (School tier)
- [ ] Pruebas de usuario con 10 familias
- [ ] Pruebas de usuario con 1 escuela piloto

**Próximo milestone:** Documento de especificaciones del MVP listo para desarrollo.

---

### 3.2 AGENTE MARCA

**Objetivo:** Construir la identidad, la voz y los activos visuales de DaemonCraft.

#### Completado ✅
- [x] Nombre de marca: DaemonCraft
- [x] Tagline: "Un daemon vive en tu servidor de Minecraft"
- [x] Narrativa de marca: el daemon como espíritu guía, compañero persistente, guardián
- [x] Paleta de colores:
  - Daemon Orange: `#FF5722`
  - Cyan Glow: `#00E5FF`
  - Void Black: `#0B0C15`
  - Grass Green: `#7CAC50`
  - Sky Blue: `#7EC0EE`
- [x] Tipografía: Fredoka (display), Nunito (body), Monocraft/Press Start 2P (UI gaming)
- [x] Landing page completa con Astro:
  - Hero con cielo Minecraft pixelado
  - Sección de SOULs con 4 cards
  - Sección "Cómo funciona" (timeline)
  - Sección "Para padres" con demo de reporte Telegram
  - Pricing table
  - Sección Seed Round / crowdfunding
  - Footer
- [x] Sistema de diseño: bloques Minecraft, botones pixel, entity tags, glow effects
- [x] SEO básico: meta tags, OG, favicon, theme-color
- [x] Investigación de influencers (documento completo con 200+ perfiles)
- [x] Deck de inversores (documento markdown con 15 slides)

#### En Progreso 🟡
- [ ] Skin 3D del daemon (prompt preparado, falta generar asset)
- [ ] Sistema de contenido para redes sociales (calendario de 30 posts en draft)
- [ ] Email funnel de onboarding (5 emails en draft)
- [ ] Script de video demo (60 segundos en draft)

#### Pendiente 🔴
- [ ] Generar assets visuales finales:
  - Logo SVG optimizado
  - Skin 3D del daemon (base + variantes por SOUL)
  - Iconos para cada SOUL
  - Screenshots de producto (mockups o reales)
  - Animaciones Lottie para la web
- [ ] Video demo de 60 segundos (producir, editar, subir)
- [ ] Video de pitch de 5 minutos para inversores
- [ ] Kit de prensa (press kit con logos, screenshots, boilerplate)
- [ ] Guía de voz y tono (brand voice guide)
- [ ] Templates de redes sociales (Canva/Figma)
- [ ] Merchandising básico (stickers, camisetas para early adopters)
- [ ] Presentación en slides (Google Slides / Keynote) para pitches

**Próximo milestone:** Skin 3D generado + primera semana de contenido publicado en X.

---

### 3.3 AGENTE GROWTH

**Objetivo:** Conseguir usuarios, validar el producto, y construir tracción para el seed round.

#### Completado ✅
- [x] Definición de métricas norte:
  - M6: 500+ agentes activos
  - M9: $12K+ MRR
  - M12: 10,000+ usuarios
- [x] Investigación de 200+ influencers clasificados por relevancia
- [x] Estrategia de outreach en 4 fases:
  1. Validación técnica (AI builders + Minecraft técnicos)
  2. Validación cultural (creadores de contenido familiar)
  3. Escalamiento (newsletters, podcasts, medios)
  4. Eventos (speedruns, build battles, colaboraciones)
- [x] Definición de tier de precios
- [x] Estrategia de seed round: $450K objetivo
- [x] Lista de medios prioritarios para PR (gaming, tech, ed-tech)

#### En Progreso 🟡
- [ ] Crear cuenta de Twitter/X para DaemonCraft
- [ ] Preparar 3 demos personalizadas para outreach a influencers
- [ ] Draft de Hacker News launch post
- [ ] Product Hunt launch page preparada

#### Pendiente 🔴
- [ ] Lanzar cuenta de X + primeros 10 posts
- [ ] Enviar 10 DMs personalizados a influencers técnicos
- [ ] Publicar blog técnico en Dev.to / Indie Hackers
- [ ] Submit a newsletters de AI: Ben's Bites, The Rundown AI
- [ ] Lanzar Discord community
- [ ] Crear waitlist / early access program
- [ ] Definir funnel de conversión: visita → signup → activación → pago
- [ ] Implementar analytics (Mixpanel / Amplitude / PostHog)
- [ ] Setup de email marketing (ConvertKit / Mailchimp / Resend)
- [ ] Landing page de waitlist con captura de emails
- [ ] Partnership con 1 escuela piloto
- [ ] Partnership con 1 creador de contenido (micro-influencer)
- [ ] Aplicar a aceleradoras (Y Combinator, Techstars, etc.)
- [ ] Networking con VCs de ed-tech y gaming
- [ ] Organizar evento online ("Invoca tu Daemon" launch party)

**Próximo milestone:** 1000 emails en waitlist + 1 video de influencer publicado.

---

### 3.4 AGENTE TECH

**Objetivo:** Construir el producto que funcione.

#### Completado ✅
- [x] Elección de stack web: Astro + React + Tailwind + TypeScript
- [x] Landing page deployable

#### En Progreso 🟡
- [ ] Definir arquitectura de backend (microservicios vs monolito)
- [ ] Elegir LLM provider (OpenAI, Anthropic, local, mix)
- [ ] Definir protocolo de conexión con Minecraft (MCPI, Mineflayer, plugin propio)

#### Pendiente 🔴
- [ ] **Infraestructura:**
  - [ ] Setup de servidor cloud (AWS/GCP/Modal/Lambda)
  - [ ] CI/CD pipeline
  - [ ] Monitoring y alerting
  - [ ] Database (PostgreSQL + Redis para caché/memoria)
- [ ] **Core AI:**
  - [ ] Sistema de percepción del mundo (qué ve el agente)
  - [ ] Sistema de razonamiento (LLM + prompt engineering)
  - [ ] Sistema de acción (qué puede hacer: moverse, minar, construir, hablar)
  - [ ] Sistema de memoria (vector DB para recuerdos, PostgreSQL para estado)
  - [ ] Sistema de personalidad (SOUL engine: prompts dinámicos por personalidad)
  - [ ] Fine-tuning pipeline para SOULs custom
- [ ] **Integraciones:**
  - [ ] Conector Minecraft Java Edition
  - [ ] Conector Minecraft Bedrock Edition
  - [ ] Bridge Telegram (reportes, comandos)
  - [ ] API pública (Creator tier)
  - [ ] Webhooks
- [ ] **Seguridad:**
  - [ ] Auth y autorización (OAuth, JWT)
  - [ ] Rate limiting
  - [ ] Data isolation (multi-tenant)
  - [ ] COPPA compliance
  - [ ] GDPR compliance
  - [ ] Audit log inmutable
- [ ] **DevEx:**
  - [ ] Documentación de API
  - [ ] SDK para creadores de SOULs
  - [ ] Sandbox para probar SOULs
- [ ] **MVP v0.1:**
  - [ ] Agente que se conecta a un servidor
  - [ ] Responde a comandos de chat
  - [ ] Sigue al jugador
  - [ ] Mina bloques básicos
  - [ ] Construye estructuras simples
  - [ ] Recuerda preferencias básicas

**Próximo milestone:** Prototipo mínimo funcional (agente que se conecta y responde) en 4 semanas.

---

### 3.5 AGENTE COMUNIDAD

**Objetivo:** Construir una comunidad de usuarios apasionados que den feedback, compartan el producto y se sientan parte del proyecto.

#### Completado ✅
- [x] Definición de públicos objetivo:
  - Jugadores de Minecraft (12-25 años)
  - Padres de gamers (30-50 años)
  - Educadores (25-55 años)
  - Creadores de contenido (18-35 años)
- [x] Narrativa comunitaria: "Primera Camada" (early adopters)

#### En Progreso 🟡
- [ ] Nada activo aún

#### Pendiente 🔴
- [ ] Setup de Discord server con canales organizados:
  - #general
  - #showcase (screenshots de Daemons)
  - #soul-ideas (propuestas de personalidades)
  - #bugs
  - #feedback
  - #parents (canal privado)
  - #educators (canal privado)
- [ ] Programa de beta testers ("Founding Daemons")
  - [ ] Formulario de aplicación
  - [ ] Onboarding especial
  - [ ] Badge/rol exclusivo
  - [ ] Canal privado
- [ ] Sistema de recompensas:
  - [ ] Referral program (invita a un amigo = mes gratis)
  - [ ] Bug bounty (reporta bug = créditos)
  - [ ] Content bounty (haces video de DC = créditos)
- [ ] Eventos comunitarios:
  - [ ] Weekly build challenges con Daemon
  - [ ] Monthly AMA con el equipo
  - [ ] "Daemon of the Month" (showcase de usuarios)
- [ ] Documentación para usuarios:
  - [ ] FAQ
  - [ ] Guía de inicio rápido
  - [ ] Guía de personalización de SOULs
  - [ ] Guía para padres
  - [ ] Guía para educadores
- [ ] Sistema de soporte:
  - [ ] Email support
  - [ ] Discord tickets
  - [ ] Knowledge base (Notion / GitBook)

**Próximo milestone:** Discord server activo con 100 miembros.

---

## 4. Roadmap Temporal

### Fase 0: Fundamentos (Abril 2026) — AHORA
> *Construir la base. Sin prisa, pero sin pausa.*

| Semana | Agente Producto | Agente Marca | Agente Growth | Agente Tech | Agente Comunidad |
|--------|-----------------|--------------|---------------|-------------|------------------|
| S1 | Definir MVP | Skin 3D + assets | Cuenta X + primer posts | Arquitectura backend | Setup Discord |
| S2 | Especificaciones MVP | Video demo script | Outreach 10 influencers | Prototipo conexión MC | 50 miembros Discord |
| S3 | Review specs | Video demo producción | Blog técnico Dev.to | Agente responde chat | 100 miembros |
| S4 | Freeze features | Landing page final | Submit newsletters | MVP v0.1 interno | Beta testers selected |

**Milestone Fase 0:** MVP jugable interno + landing page completa + 100 emails waitlist.

---

### Fase 1: Primera Camada (Mayo–Junio 2026)
> *Lanzamiento cerrado con early adopters. Validar, iterar, aprender.*

| Mes | Agente Producto | Agente Marca | Agente Growth | Agente Tech | Agente Comunidad |
|-----|-----------------|--------------|---------------|-------------|------------------|
| M1 | Beta con 50 users | Contenido semanal | PR a medios gaming | Iteración MVP | Evento launch |
| M2 | Beta con 200 users | Video influencer #1 | 1er partnership creador | Reportes Telegram | Feedback loop activo |

**Milestone Fase 1:** 200 usuarios activos + 1 video de influencer + reportes de padres funcionando.

---

### Fase 2: Invocación Pública (Julio–Septiembre 2026)
> *Launch público. Escalar tracción. Cerrar seed round.*

| Mes | Agente Producto | Agente Marca | Agente Growth | Agente Tech | Agente Comunidad |
|-----|-----------------|--------------|---------------|-------------|------------------|
| M3 | Public launch v1.0 | Product Hunt + HN | PR masivo | Escalar infra | 1000 miembros |
| M4 | Guardian Mode | Video case study | Partnership escuela | Seguridad + compliance | Programa educadores |
| M5 | Creator marketplace | Brand guide final | Demo day / pitch | API pública | Creadores de SOULs |

**Milestone Fase 2:** 1000+ usuarios + seed round cerrado + Guardian Mode activo.

---

### Fase 3: El Reino de los Daemons (Octubre 2026+)
> *Crecimiento sostenido. Internacionalización. Series A.*

| Trimestre | Foco Principal |
|-----------|---------------|
| Q4 2026 | Escalar a 10K usuarios. Lanzar en español e inglés. School tier piloto. |
| Q1 2027 | Multi-agent (varios Daemons en un servidor). Interoperabilidad entre mundos. Series A. |
| Q2 2027 | VR/AR integration. Expansión a Roblox. Marketplace de SOULs maduro. |

**Milestone Fase 3:** 10K+ usuarios + Series A en camino.

---

## 5. Dependencias Críticas

```
[MVP Tech] ───────────────────────────────────────► [Public Launch]
     │                                                    ▲
     │                                                    │
     ├──► [Reportes Telegram] ───────► [Padres contentos] │
     │                                                    │
     ├──► [SOULs funcionan] ─────────► [Creadores contentos]
     │                                                    │
     └──► [Landing page] ────────────► [Waitlist] ────────┘
               ▲
               │
         [Marca + Assets]
               │
         [Video demo]
               │
         [Influencer #1]
```

**Dependencias bloqueantes:**
1. **MVP Tech → Todo lo demás.** Sin un agente que funcione, no hay producto que vender.
2. **Landing page + Marca → Growth.** Sin una web creíble, no hay conversión.
3. **Reportes Telegram → Padres.** Sin esto, el valor proposition para familias es débil.

**Dependencias paralelizables:**
- Marca y Growth pueden avanzar en paralelo con Tech.
- Comunidad puede empezar antes del producto (build in public).
- Content (video, blogs) puede producirse con mockups/screenshots.

---

## 6. Métricas y KPIs

### Métricas de Salud del Proyecto

| Métrica | Actual | Fase 0 | Fase 1 | Fase 2 | Fase 3 |
|---------|--------|--------|--------|--------|--------|
| Waitlist emails | 0 | 100 | 500 | 2000 | 10000 |
| Usuarios activos | 0 | 0 | 200 | 1000 | 10000 |
| MRR | $0 | $0 | $200 | $3000 | $20000 |
| Retención D7 | — | — | 30% | 40% | 50% |
| NPS | — | — | 20 | 40 | 50 |
| Discord members | 0 | 100 | 500 | 1000 | 5000 |
| X followers | 0 | 50 | 500 | 2000 | 10000 |
| Influencers activos | 0 | 0 | 1 | 5 | 20 |
| Artículos de prensa | 0 | 0 | 2 | 10 | 50 |

### Métricas por Agente

**Producto:**
- Features entregadas vs roadmap
- Bugs críticos abiertos
- Tiempo de onboarding (TTFH: Time To First Hello from Daemon)
- Acciones por sesión

**Marca:**
- Brand awareness (survey)
- Sentimiento de marca (social listening)
- Calidad de assets (subjetivo, review interno)

**Growth:**
- CAC (Customer Acquisition Cost)
- LTV (Lifetime Value)
- Conversion rate waitlist → free → paid
- Churn rate mensual

**Tech:**
- Uptime (target: 99.9%)
- Latencia de respuesta del agente (< 2s)
- Costo por agente activo / mes
- Coverage de tests

**Comunidad:**
- DAU/MAU de Discord
- Mensajes por día
- Tasa de respuesta del equipo (< 2h)
- Satisfaction score de soporte

---

## 7. Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| **MVP tarda más de lo esperado** | Alta | Crítico | Scope agresivo. Cortar features. Launch con "Daemon que solo habla" si es necesario. |
| **OpenAI cambia precios o políticas** | Media | Alto | Arquitectura multi-provider. Tener fallback a Anthropic/local. |
| **Minecraft EULA prohíbe agents comerciales** | Baja | Crítico | Revisar EULA de Mojang/Microsoft. Diseñar para cumplir. Tener plan B (servidores propios). |
| **Competidor grande entra al espacio** | Media | Alto | Velocidad. Community moat. Focus en educación/padres (nicho que big tech ignora). |
| **No conseguimos tracción inicial** | Media | Crítico | Pivotar segmento (ej: de familias a creadores de contenido). |
| **Seguridad: un daemon hace algo inapropiado** | Media | Crítico | Guardrails, moderation, human-in-the-loop, kill switch. |
| **Burn rate antes de seed round** | Media | Alto | Presupuesto conservador. Freelancers vs FTE. Nico full-time + devs part-time. |

---

## 8. Recursos Necesarios

### Humanos (roles a cubrir)

| Rol | Dedicación | Prioridad | Estado |
|-----|-----------|-----------|--------|
| **Founder / PM / Growth** (Nico) | Full-time | Crítica | ✅ Cubierto |
| **Lead Developer / AI Engineer** | Full-time | Crítica | 🔴 Buscando |
| **Frontend Developer** | Part-time | Alta | 🔴 Buscando (o Nico + freelancers) |
| **DevOps / Backend** | Part-time | Alta | 🔴 Buscando |
| **Community Manager** | Part-time | Media | 🔴 Buscando (Nico interim) |
| **Content Creator** | Freelance | Media | 🟡 Freelancers disponibles |
| **Designer UI/UX** | Freelance | Alta | 🟡 Freelancers disponibles |

### Financieros

| Rubro | Fase 0 | Fase 1 | Fase 2 | Total Seed |
|-------|--------|--------|--------|------------|
| Infra (cloud, APIs) | $500 | $1000 | $2000 | ~$5000 |
| Herramientas (SaaS) | $300 | $500 | $1000 | ~$3000 |
| Freelancers (design, video) | $1000 | $2000 | $3000 | ~$10000 |
| Marketing / PR | $0 | $1000 | $5000 | ~$10000 |
| Salarios (founder runway) | $3000 | $6000 | $9000 | ~$20000 |
| Buffer (15%) | $720 | $1575 | $3000 | ~$7000 |
| **TOTAL MENSUAL** | **~$5500** | **~$12K** | **~$23K** | **~$45K** |

**Runway objetivo:** 18 meses = ~$450K seed round.

---

## 9. Decisiones Pendientes

| Decisión | Opciones | Dueño | Deadline | Impacto |
|----------|----------|-------|----------|---------|
| **Stack de backend** | Node.js vs Python vs Go | Agente Tech | 1 semana | Alto |
| **LLM principal** | OpenAI vs Anthropic vs Mistral vs mix | Agente Tech | 1 semana | Crítico |
| **Proveedor cloud** | AWS vs GCP vs Vercel/Modal | Agente Tech | 2 semanas | Alto |
| **Base de datos** | PostgreSQL vs Supabase vs PlanetScale | Agente Tech | 1 semana | Medio |
| **Email marketing** | ConvertKit vs Mailchimp vs Resend | Agente Growth | 2 semanas | Medio |
| **Analytics** | Mixpanel vs Amplitude vs PostHog | Agente Growth | 2 semanas | Medio |
| **Discord vs Slack vs Circle** | Community platform | Agente Comunidad | 1 semana | Medio |
| **Incorporación legal** | Argentina vs Delaware C-Corp | Agente Orq | 1 mes | Medio |
| **Nombre alternativo (backup)** | ¿Necesitamos uno? | Agente Marca | 2 semanas | Bajo |

---

## 10. Glosario

| Término | Definición |
|---------|-----------|
| **Daemon** | Agente autónomo de IA que vive en un servidor de Minecraft |
| **SOUL** | Personalidad + skillset de un Daemon. Define cómo actúa, habla y juega |
| **Companion** | Tier de pago ($5/mes). Hasta 3 perfiles, acciones ilimitadas, reportes |
| **Creator** | Tier de pago ($15/mes). Fine-tuning de SOULs + marketplace |
| **School** | Tier de pago ($99/mes). Realm privado + 20 perfiles + dashboard docente |
| **Guardian Mode** | Sistema de seguridad que monitorea lenguaje y escolta en servidores públicos |
| **Bridge Telegram** | Conexión entre el Daemon y los padres/educadores vía Telegram |
| **Primera Camada** | Programa de early adopters. Los primeros en invocar un Daemon |
| **Agente (en este plan)** | Equipo/área de trabajo con responsabilidades definidas |

---

## 11. Historial de Cambios

| Fecha | Versión | Cambio | Autor |
|-------|---------|--------|-------|
| 22 Abr 2026 | 1.0 | Creación del plan maestro | Kimi (IA) + Nico |
| 22 Abr 2026 | 1.0 | Investigación de influencers completada | Kimi (IA) |
| 22 Abr 2026 | 1.0 | Landing page + sistema de marca completados | Kimi (IA) |

---

## 12. Notas Multi-Agente

> *Esta sección es para dejar pensamientos, ideas sueltas, y conexiones entre agentes que no encajan en otras secciones.*

- **Producto ↔ Tech:** El sistema de SOULs necesita ser lo suficientemente simple para que un creador de contenido lo entienda, pero lo suficientemente potente para que un developer lo extienda. Esto es un trade-off constante.

- **Marca ↔ Growth:** La narrativa del "daemon" como espíritu guía es única en el espacio. Ningún competidor tiene este storytelling. Debemos explotarlo en cada pieza de contenido.

- **Growth ↔ Comunidad:** Los early adopters no son solo usuarios, son evangelistas. Cada beta tester debería sentirse co-creador. El programa "Founding Daemons" no es marketing, es producto.

- **Tech ↔ Marca:** El video demo no puede mostrar un agente lento o que se trabó. La percepción de "fluidez" es crítica. Necesitamos un agente que responda en < 2s para el demo.

- **Producto ↔ Growth:** El free tier no es un trial, es un producto completo. La restricción de 100 acciones/día debe sentirse generosa, no stingy. El upgrade a Companion debe ser obvio (reportes para padres, múltiples perfiles).

- **Marca ↔ Tech:** La estética pixel art / Minecraft debe extenderse a la UI del producto, no solo a la web. El dashboard, los reportes, incluso los mensajes del agente deberían tener un toque visual de Minecraft.

- **Growth ↔ Tech:** Las métricas de analytics deben estar pensadas desde el día 1. No podemos mejorar lo que no medimos. PostHog o Mixpanel desde el MVP.

- **Comunidad ↔ Producto:** El feedback loop debe ser < 24h. Un usuario reporta un bug hoy, mañana ve una respuesta. Eso construye lealtad que no se compra con ads.

---

*Fin del documento. Actualizar al menos semanalmente. Si lees esto y algo no tiene sentido, corrígelo. Este plan no es sagrado, es una herramienta.*
