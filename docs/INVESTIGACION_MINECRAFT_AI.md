# Investigación: Minecraft + AI Agents — Tendencias 2025-2026

## Fuentes y hallazgos clave

### 1. Mineflayer + LLM (stack técnico de DaemonCraft)
- Mineflayer es la librería Node.js más madura para bots de Minecraft
- En 2024-2025 explotó la combinación Mineflayer + LLM (GPT-4, Claude, local)
- Proyectos referencia: MinePal, Voyager (Microsoft Research), AutoMC
- Voyager usa "skill library" — similar a nuestro concepto de SOULs

### 2. Voyager (Microsoft Research, 2023-2024)
- Primer agente LLM autónomo en Minecraft con aprendizaje continuo
- Usa código como política de acción (code-as-policy)
- Cura habilidades en una biblioteca que reutiliza
- Limitación: requiere Minecraft con mods (Forge), no funciona en servidores vanilla
- DaemonCraft se diferencia al ser cloud-native y compatible Java/Bedrock vanilla

### 3. MinePal / Claude-Minecraft
- Integración de Claude con Mineflayer para conversación natural
- Enfoque en compañerismo más que en automatización
- Similar al SOUL "Leñador" / "Tutora" de DaemonCraft

### 4. Estado del arte: GPT-4o / Kimi / Claude visión
- Modelos multimodales pueden interpretar screenshots de Minecraft
- Esto abre "percepción visual" para agentes que antes solo usaban estado de bot
- DaemonCraft podría beneficiarse de análisis visual del mundo

### 5. Seguridad y padres (nicho desatendido)
- La mayoría de proyectos AI+Minecraft son para speedrunning o research
- Casi nadie aborda el segmento "familias con niños gamers"
- Guardian Mode es diferenciador único de DaemonCraft
- COPPA compliance es requisito raro en proyectos open-source

### 6. Tendencias de contenido 2025
- Shorts/Reels de "AI playing Minecraft" tienen alta viralidad
- TikTok: #minecraftai con 500M+ views
- YouTube: videos de 10-60 min de "AI learns Minecraft" son populares
- Oportunidad: contenido educativo para padres (nicho vacío)

### 7. Infraestructura y costos
- Mineflayer + Node.js puede correr en VPS de $5/mes
- LLM API para 1 agente activo: ~$0.50-2/día dependiendo del modelo
- Costo por agente mensual estimado: $15-60 (Kimi es más barato que OpenAI)
- Escalable con Modal/Lambda para sleep/wake de agentes

### 8. Competencia directa e indirecta
- **Directa:** Ninguna con modelo SaaS + seguridad parental
- **Indirecta:** 
  - Aternos (hosting gratuito de servidores MC, no AI)
  - Minehut (hosting + plugins, no AI)
  - Replika AI (compañero AI, no Minecraft)
  - Discord bots genéricos (no integración in-game)

## Recomendaciones para contenido de DaemonCraft

1. **Blog técnico:** "Cómo construimos un agente LLM para Minecraft con Kimi y Mineflayer"
2. **Video viral:** Time-lapse de 24h de un agente construyendo solo
3. **Padres:** "Cómo saber qué hace tu hijo en Minecraft sin espiarlo"
4. **Educación:** "Minecraft como aula: matemáticas y lógica con un tutor AI"
5. **Dev.to:** Comparativa Voyager vs DaemonCraft (arquitectura cloud-native)

