from src.parsers.heresy import heresy
from src.parsers.killteam import killteam

KILLTEAM_ID: str = "3b7e-7dab-f79f-2e74"

HORUS_HERESY_ID: str = "ca571888-56a9-c58e-ddaf-54f4713538bc"

SUPPORTED_PARSERS = {KILLTEAM_ID: killteam, HORUS_HERESY_ID: heresy}
TEMPLATES = {KILLTEAM_ID: "killteam.html", HORUS_HERESY_ID: "heresy.html"}

WARHAMMER_40K_ID: str = ""
WARHAMMER_40K_NAME: str = ""

AGE_OF_SIGMAR_ID: str = ""
AGE_OF_SIGMAR_NAME: str = ""

SUPPORTED_BATTLESCRIBE_VERSION = "2.03"

BATTLESCRIBE_VERSION_ERROR = {
    "ERROR": "battlesrcibe version not supported please upgrade, the current supported version is {}".format(
        SUPPORTED_BATTLESCRIBE_VERSION
    )
}
