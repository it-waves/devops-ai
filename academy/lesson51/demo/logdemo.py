import logging
logging.basicConfig(level="INFO", format="%(levelname)s %(message)s")
log = logging.getLogger("deploy")
log.debug("checking disk")
log.info("starting deploy")
log.warning("disk at 85 percent")
try:
    int("eight")
except ValueError:
    log.exception("deploy failed")
