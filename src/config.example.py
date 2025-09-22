# Configurações da aplicação Streamlit - EXEMPLO
# Copie este arquivo para config.py e ajuste conforme necessário

# Configurações do e-SAJ TJSP
ESAJ_CONFIG = {
    "base_url": "https://esaj.tjsp.jus.br/cpopg/search.do",
    "referer": "https://esaj.tjsp.jus.br/cpopg/abrirConsultaDeRequisitorios.do",
    "timeout": 30,  # Timeout em segundos
    "delay_min": 1,  # Delay mínimo entre consultas
    "delay_max": 5,  # Delay máximo entre consultas
    "delay_default": 2  # Delay padrão
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
    "page_title": "Revisa Consulta CPF e-SAJ",
    "page_icon": "🏛️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Configurações de validação
VALIDATION_CONFIG = {
    "cpf_min_length": 9,  # Tamanho mínimo do CPF
    "cpf_max_length": 11,  # Tamanho máximo do CPF
    "required_columns": ["nome", "cpf"]  # Colunas obrigatórias
}

# Configurações de arquivo
FILE_CONFIG = {
    "allowed_types": ["csv"],  # Tipos de arquivo permitidos
    "max_size_mb": 10,  # Tamanho máximo em MB
    "encoding": "utf-8"  # Encoding do arquivo
}

# Configurações de log
LOG_CONFIG = {
    "log_file": "consulta_esaj.log",  # Arquivo de log
    "log_format": "%(asctime)s - %(levelname)s - %(message)s",  # Formato do log
    "log_level": "INFO"  # Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
}

# Configurações de performance
PERFORMANCE_CONFIG = {
    "max_cpfs_per_batch": 1000,  # Máximo de CPFs por lote
    "max_retries": 3,  # Máximo de tentativas em caso de erro
    "retry_delay": 5,  # Delay entre tentativas em segundos
    "memory_limit_mb": 512  # Limite de memória em MB
}

# Configurações de segurança
SECURITY_CONFIG = {
    "max_file_size_mb": 50,  # Tamanho máximo do arquivo
    "allowed_origins": ["localhost", "127.0.0.1"],  # Origens permitidas
    "rate_limit_per_minute": 30,  # Limite de requisições por minuto
    "enable_csrf": False  # Habilitar proteção CSRF
}

# Configurações de notificação
NOTIFICATION_CONFIG = {
    "enable_email": False,  # Habilitar notificações por email
    "email_smtp_server": "smtp.gmail.com",
    "email_smtp_port": 587,
    "email_username": "",
    "email_password": "",
    "email_from": "",
    "email_to": []
}

# Configurações de backup
BACKUP_CONFIG = {
    "enable_backup": True,  # Habilitar backup automático
    "backup_interval_hours": 24,  # Intervalo de backup em horas
    "backup_retention_days": 7,  # Retenção de backup em dias
    "backup_directory": "./backups"  # Diretório de backup
}

# Configurações de monitoramento
MONITORING_CONFIG = {
    "enable_metrics": True,  # Habilitar métricas
    "metrics_interval_seconds": 60,  # Intervalo de métricas
    "enable_health_check": True,  # Habilitar health check
    "health_check_endpoint": "/health"  # Endpoint de health check
}
