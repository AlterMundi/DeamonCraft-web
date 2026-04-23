#!/usr/bin/env python3
"""
Genera un video demo corto de DaemonCraft usando PIL + ffmpeg.
Formato: vertical 1080x1920 (TikTok/Reels/Shorts)
Estilo: paleta DaemonCraft (Void Black, Daemon Orange, Cyan Glow)
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
DURATION = 15  # segundos
TOTAL_FRAMES = FPS * DURATION

# Paleta
BG = (11, 12, 21)
ORANGE = (255, 87, 34)
CYAN = (0, 229, 255)
WHITE = (245, 230, 200)
GRAY = (150, 150, 160)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def get_font(size, bold=False):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except Exception:
        return ImageFont.load_default()


def ease_out(t):
    return 1 - (1 - t) ** 3


def ease_in_out(t):
    return 0.5 - 0.5 * math.cos(t * math.pi)


def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def make_frame(n):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    t = n / TOTAL_FRAMES  # 0.0 -> 1.0
    sec = n / FPS

    # Glow de fondo pulsante
    pulse = 0.5 + 0.5 * math.sin(sec * 1.5)
    r = int(255 * pulse * 0.08)
    g = int(87 * pulse * 0.08)
    b = int(34 * pulse * 0.08)
    for i in range(5):
        alpha = int(30 * (1 - i / 5) * pulse)
        rr = 400 + i * 80
        draw.ellipse([W // 2 - rr, 400 - rr, W // 2 + rr, 400 + rr], fill=(r, g, b))

    # === SECCIONES POR TIEMPO ===

    if sec < 3.5:
        # --- FRAME 0-3.5s: Logo + tagline ---
        local_t = min(sec / 3.5, 1.0)
        local_ease = ease_out(local_t)

        # Logo text
        logo_text = "DaemonCraft"
        font_logo = get_font(110, bold=True)
        bbox = draw.textbbox((0, 0), logo_text, font=font_logo)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        y_offset = int(500 * (1 - local_ease))
        x = (W - tw) // 2
        y = 600 + y_offset

        # Glow detrás del logo
        glow_intensity = int(60 * local_ease * pulse)
        for g_off in range(8, 0, -2):
            draw.text((x, y), logo_text, font=font_logo, fill=(r + glow_intensity, g + glow_intensity // 3, b + glow_intensity // 5))

        draw.text((x, y), logo_text, font=font_logo, fill=ORANGE)

        # Subtítulo
        if sec > 1.0:
            sub_t = min((sec - 1.0) / 2.0, 1.0)
            sub_ease = ease_out(sub_t)
            sub_text = "Un daemon vive en tu servidor de Minecraft"
            font_sub = get_font(42)
            bbox2 = draw.textbbox((0, 0), sub_text, font=font_sub)
            tw2 = bbox2[2] - bbox2[0]
            y2 = 780 + int(100 * (1 - sub_ease))
            draw.text(((W - tw2) // 2, y2), sub_text, font=font_sub, fill=WHITE)

    elif sec < 10.0:
        # --- FRAME 3.5-10s: Loop de arquitectura ---
        loop_t = (sec - 3.5) / 6.5

        # Título de sección
        title = "¿Cómo funciona?"
        font_title = get_font(64, bold=True)
        bbox = draw.textbbox((0, 0), title, font=font_title)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, 350), title, font=font_title, fill=WHITE)

        # 4 cajas: Percepción, Razonamiento, Acción, Memoria
        steps = [
            ("PERCEPCIÓN", "Ve el mundo\nbloque por bloque", CYAN),
            ("RAZONAMIENTO", "Kimi piensa\nqué hacer", ORANGE),
            ("ACCIÓN", "Mina, construye,\npelea, habla", CYAN),
            ("MEMORIA", "Recuerda todo\nentre sesiones", ORANGE),
        ]

        box_w = 800
        box_h = 180
        start_y = 520
        gap = 40

        for i, (label, desc, color) in enumerate(steps):
            delay = i * 0.12
            local_t = max(0, min((loop_t - delay) / 0.4, 1.0))
            local_ease = ease_out(local_t)

            if local_t <= 0:
                continue

            y = start_y + i * (box_h + gap)
            x = (W - box_w) // 2

            # Slide in desde derecha
            slide = int(200 * (1 - local_ease))

            # Box background con borde
            alpha_box = int(40 * local_ease)
            box_fill = (20 + alpha_box, 22 + alpha_box, 35 + alpha_box)
            draw_rounded_rect(draw, [x + slide, y, x + box_w + slide, y + box_h], 20, box_fill, outline=color, width=3)

            # Número
            num_text = f"0{i + 1}"
            font_num = get_font(48, bold=True)
            draw.text((x + 30 + slide, y + 55), num_text, font=font_num, fill=color)

            # Label
            font_label = get_font(38, bold=True)
            draw.text((x + 120 + slide, y + 35), label, font=font_label, fill=WHITE)

            # Desc
            font_desc = get_font(28)
            lines = desc.split("\n")
            for li, line in enumerate(lines):
                draw.text((x + 120 + slide, y + 85 + li * 38), line, font=font_desc, fill=GRAY)

            # Flecha entre cajas (excepto última)
            if i < 3 and local_t > 0.5:
                arrow_y = y + box_h + gap // 2
                arrow_alpha = int(255 * min((local_t - 0.5) * 2, 1.0))
                arrow_color = (GRAY[0], GRAY[1], GRAY[2])
                # Flecha simple ↓
                ax = W // 2
                draw.polygon([(ax, arrow_y - 10), (ax - 12, arrow_y - 25), (ax + 12, arrow_y - 25)], fill=arrow_color)

        # Loop indicator
        loop_progress = min(loop_t / 0.8, 1.0)  # Completa en 80% del tiempo
        bar_w = 600
        bar_h = 6
        bar_x = (W - bar_w) // 2
        bar_y = 1480
        draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=3, fill=(40, 42, 55))
        draw.rounded_rectangle([bar_x, bar_y, bar_x + int(bar_w * loop_progress), bar_y + bar_h], radius=3, fill=ORANGE)

    else:
        # --- FRAME 10-15s: Stats + CTA ---
        final_t = min((sec - 10.0) / 4.0, 1.0)
        final_ease = ease_out(final_t)

        stats = [
            ("500+", "agentes activos"),
            ("$0", "para empezar"),
            ("30s", "para invocar"),
        ]

        # Stats grid
        stat_y = 500
        for i, (num, label) in enumerate(stats):
            delay = i * 0.15
            local_t = max(0, min((final_t - delay) / 0.5, 1.0))
            local_ease = ease_out(local_t)
            if local_t <= 0:
                continue

            x = 140 + i * 300
            y = stat_y + int(100 * (1 - local_ease))

            font_num = get_font(72, bold=True)
            draw.text((x, y), num, font=font_num, fill=ORANGE if i % 2 == 0 else CYAN)

            font_lbl = get_font(28)
            lines = label.split(" ")
            for li, word in enumerate(lines):
                draw.text((x, y + 90 + li * 35), word, font=font_lbl, fill=GRAY)

        # CTA
        if final_t > 0.5:
            cta_ease = ease_out(min((final_t - 0.5) / 0.5, 1.0))
            cta_text = "Invocá tu daemon"
            font_cta = get_font(56, bold=True)
            bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
            tw = bbox[2] - bbox[0]
            y_cta = 1000 + int(80 * (1 - cta_ease))

            # Button bg
            btn_pad = 30
            draw_rounded_rect(draw, [(W - tw) // 2 - btn_pad, y_cta - btn_pad, (W + tw) // 2 + btn_pad, y_cta + 80 + btn_pad], 20, ORANGE)
            draw.text(((W - tw) // 2, y_cta), cta_text, font=font_cta, fill=WHITE)

            url_text = "daemoncraft.ai"
            font_url = get_font(36)
            bbox2 = draw.textbbox((0, 0), url_text, font=font_url)
            tw2 = bbox2[2] - bbox2[0]
            draw.text(((W - tw2) // 2, y_cta + 130), url_text, font=font_url, fill=GRAY)

    # Partículas flotantes (siempre presentes)
    import random
    random.seed(42)
    for p in range(20):
        px = random.randint(50, W - 50)
        py = random.randint(100, H - 100)
        phase = random.random() * 2 * math.pi
        size = random.randint(2, 5)
        intensity = int(100 + 100 * math.sin(sec * 2 + phase))
        color = ORANGE if p % 3 == 0 else CYAN if p % 3 == 1 else WHITE
        draw.ellipse([px, py, px + size, py + size], fill=(color[0], color[1], color[2]))

    return img


def main():
    out_dir = "/tmp/daemoncraft_frames"
    os.makedirs(out_dir, exist_ok=True)
    print(f"Generando {TOTAL_FRAMES} frames en {out_dir}...")

    for n in range(TOTAL_FRAMES):
        frame = make_frame(n)
        frame.save(f"{out_dir}/frame_{n:05d}.png")
        if n % 30 == 0:
            print(f"  {n}/{TOTAL_FRAMES} frames...")

    output_path = "/home/saira/web/hermescraft/public/video/daemoncraft-demo.mp4"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", f"{out_dir}/frame_%05d.png",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "23",
        "-preset", "fast",
        output_path,
    ]
    print(f"\nCompilando video: {output_path}")
    import subprocess
    subprocess.run(cmd, check=True)
    print(f"✓ Video generado: {output_path}")

    # Limpiar frames
    import shutil
    shutil.rmtree(out_dir)
    print("✓ Frames temporales limpiados")


if __name__ == "__main__":
    main()
