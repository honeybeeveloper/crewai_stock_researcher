from configs.config import Config
from configs.logging import get_logger

app_config = Config(config_file='env.yaml')
app_logger = get_logger('stock-conclusion', app_config)

