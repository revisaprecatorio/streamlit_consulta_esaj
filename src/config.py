# Configurações da aplicação Streamlit

# Configurações do e-SAJ TJSP
ESAJ_CONFIG = {
    "base_url": "https://esaj.tjsp.jus.br/cpopg/search.do",
    "referer": "https://esaj.tjsp.jus.br/cpopg/abrirConsultaDeRequisitorios.do",
    "timeout": 30,
    "delay_min": 1,
    "delay_max": 5,
    "delay_default": 2
}

# Headers para simular navegador real (baseado no n8n que funciona)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Referer": "https://esaj.tjsp.jus.br/cpopg/abrirConsultaDeRequisitorios.do",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Origin": "https://esaj.tjsp.jus.br",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1"
}

# Configurações da interface
UI_CONFIG = {
    "page_title": "Consulta CPF e-SAJ TJSP",
    "page_icon": "🏛️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Configurações de validação
VALIDATION_CONFIG = {
    "cpf_min_length": 9,
    "cpf_max_length": 11,
    "required_columns": ["nome", "cpf"]
}

# Configurações de arquivo
FILE_CONFIG = {
    "allowed_types": ["csv"],
    "max_size_mb": 10,
    "encoding": "utf-8"
}

# Configurações de log
LOG_CONFIG = {
    "log_file": "consulta_esaj.log",
    "log_format": "%(asctime)s - %(levelname)s - %(message)s",
    "log_level": "INFO"
}
