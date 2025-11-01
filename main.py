# main.py
def define_env(env):
    def h5p_lumi_embed(container_id, html_path, width="100%", height="600px", base_url=None):
        # If no base_url passed, get from MkDocs extra config
        if base_url is None:
            base_url = env.config.get('extra', {}).get('base_url', '')
        full_path = f"{base_url}/{html_path.lstrip('/')}" if base_url else f"/{html_path.lstrip('/')}"
        return f'<iframe id="{container_id}" src="{full_path}" width="{width}" height="{height}" frameborder="0" allowfullscreen></iframe>'

    env.macro(h5p_lumi_embed)
