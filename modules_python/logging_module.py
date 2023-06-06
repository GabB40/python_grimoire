import logging

# par défaut, tous les messages ne sont pas affichés ==> default = warning et supérieur
logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s : %(message)s"
)

logging.debug("logging debug")
logging.info("logging info")
logging.warning("logging warning")
logging.error("logging error")
logging.critical("logging critical")
