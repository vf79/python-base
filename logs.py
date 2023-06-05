#!/usr/bin/env python3

import os
import logging


# BOILERPLATE
# TODO: usar função
# TODO: usar lib(loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Instancia
log = logging.Logger("PYTHON-BASE", log_level)
# Level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# Formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'f:%(filename)s l:%(lineno)d: %(message)s'
)
ch.setFormatter(fmt)
# Destino
log.addHandler(ch)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: sem conexao banco de dados")
"""
print("--" * 40)
try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))