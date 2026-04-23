"""
Herramientas para publicar posts en el blog de HermesCraft via GitHub API.
Adaptado de ilPostino (https://github.com/ilPostinob0t/ilpostino)

Uso:
    from bot-tools.github_publisher import agregar_post_blog
    url = agregar_post_blog(titulo, excerpt, contenido_html, tag="Anuncio")
"""

import base64
import json
import os
import subprocess
from datetime import datetime

import requests

GITHUB_API = "https://api.github.com"
OWNER = "AlterMundi"
REPO = "DeamonCraft-web"
BRANCH = "main"
POSTS_PATH = "src/data/blog-posts.json"
SITE_URL = "https://altermundi.github.io/DeamonCraft-web/blog/"


def _get_token() -> str:
    """Obtiene token de GitHub: primero env var, luego gh CLI."""
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    raise RuntimeError(
        "No se encontró GITHUB_TOKEN. Configuralo como env var o logueate con gh auth login."
    )


def _headers() -> dict:
    return {
        "Authorization": f"token {_get_token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _file_get(path: str) -> tuple[str | None, str | None]:
    """Lee un archivo del repo. Devuelve (contenido, sha) o (None, None)."""
    url = f"{GITHUB_API}/repos/{OWNER}/{REPO}/contents/{path}?ref={BRANCH}"
    r = requests.get(url, headers=_headers(), timeout=15)
    if r.status_code == 200:
        data = r.json()
        content = base64.b64decode(data["content"]).decode("utf-8")
        return content, data.get("sha")
    return None, None


def _file_put(path: str, content: str, message: str, sha: str | None = None) -> bool:
    """Crea o actualiza un archivo en el repo."""
    url = f"{GITHUB_API}/repos/{OWNER}/{REPO}/contents/{path}"
    payload = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode(),
        "branch": BRANCH,
    }
    if sha:
        payload["sha"] = sha
    r = requests.put(url, headers=_headers(), json=payload, timeout=15)
    return r.status_code in (200, 201)


def _generar_slug(titulo: str) -> str:
    """Genera un slug URL-friendly a partir del título."""
    import unicodedata
    slug = unicodedata.normalize("NFKD", titulo)
    slug = slug.encode("ascii", "ignore").decode("ascii")
    slug = slug.lower().strip()
    for char in "'\"":"¿\u00a1!?·.,;:":
        slug = slug.replace(char, "")
    slug = slug.replace(" ", "-")
    slug = slug.replace("--", "-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:60].strip("-")


def _generar_excerpt(texto: str, max_len: int = 160) -> str:
    """Genera un excerpt a partir del contenido."""
    # Remover tags HTML básicos
    import re
    limpio = re.sub(r"<[^>]+>", "", texto)
    limpio = limpio.replace("\n", " ").strip()
    if len(limpio) > max_len:
        return limpio[:max_len].rsplit(" ", 1)[0] + "..."
    return limpio


def agregar_post_blog(
    titulo: str,
    contenido: str,
    tag: str = "General",
    highlight: bool = False,
) -> dict:
    """Agrega un nuevo post al blog-posts.json y lo publica en GitHub.

    Args:
        titulo: Título de la entrada.
        contenido: Cuerpo del post. Puede ser HTML o texto plano (se envolverá en <p>).
        tag: Categoría (Anuncio, Demo, Técnico, etc.).
        highlight: Si debe marcarse como destacado.

    Returns:
        dict con status, url, y detalles del post.
    """
    # 1. Normalizar contenido a HTML básico
    contenido = contenido.strip()
    if not contenido.startswith("<"):
        # Texto plano: convertir párrafos a <p>
        parrafos = "\n".join(
            f"<p>{p.strip()}</p>" for p in contenido.split("\n\n") if p.strip()
        )
        contenido = parrafos

    # 2. Leer posts actuales
    posts_json, sha = _file_get(POSTS_PATH)
    if posts_json is None:
        return {"status": "error", "detail": f"No se pudo leer {POSTS_PATH} del repo"}

    try:
        posts = json.loads(posts_json)
    except json.JSONDecodeError as e:
        return {"status": "error", "detail": f"JSON inválido: {e}"}

    # 3. Crear nuevo post
    fecha = datetime.now().strftime("%Y-%m-%d")
    slug = _generar_slug(titulo)
    excerpt = _generar_excerpt(contenido)

    nuevo_post = {
        "title": titulo,
        "date": fecha,
        "tag": tag,
        "excerpt": excerpt,
        "slug": slug,
        "highlight": highlight,
        "content": contenido,
    }

    # Insertar al principio
    posts.insert(0, nuevo_post)

    # 4. Escribir de vuelta
    nuevo_json = json.dumps(posts, ensure_ascii=False, indent=2)
    ok = _file_put(
        POSTS_PATH,
        nuevo_json,
        f"blog: {titulo[:50]}",
        sha=sha,
    )

    if not ok:
        return {"status": "error", "detail": "No se pudo escribir en GitHub"}

    return {
        "status": "ok",
        "url": f"{SITE_URL}#{slug}",
        "title": titulo,
        "date": fecha,
        "slug": slug,
    }


def listar_posts() -> list[dict]:
    """Devuelve la lista actual de posts del blog."""
    posts_json, _ = _file_get(POSTS_PATH)
    if posts_json is None:
        return []
    try:
        return json.loads(posts_json)
    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    # Test manual
    print("Posts actuales:", len(listar_posts()))
