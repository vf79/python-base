#!/usr/bin/env python3

import logging
import os
from logging import handlers

# BOILERPLATE
# TODO: Mover para um modulo de utilidades
# TODO: usar lib(loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Instancia
log = logging.Logger("PYTHON-BASE", log_level)
# Level
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", maxBytes=10**6, backupCount=10
)
fh.setLevel(log_level)

# Formatação
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "f:%(filename)s l:%(lineno)d: %(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
# Destino
# log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: sem conexao banco de dados")
"""
print("--" * 40)
try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
