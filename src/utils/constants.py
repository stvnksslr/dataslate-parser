from src.parsers.heresy import heresy
from src.parsers.killteam import killteam
from src.parsers.w40k import w40k

KILLTEAM_ID: str = "3b7e-7dab-f79f-2e74"

HORUS_HERESY_ID: str = "28d4-bd2e-4858-ece6"

WARHAMMER_40K_ID: str = "28ec-711c-d87f-3aeb"

SUPPORTED_PARSERS = {KILLTEAM_ID: killteam, HORUS_HERESY_ID: heresy, WARHAMMER_40K_ID: w40k}
TEMPLATES = {KILLTEAM_ID: "killteam.html", HORUS_HERESY_ID: "heresy.html", WARHAMMER_40K_ID: "w40k.html"}

WARHAMMER_40K_NAME: str = ""

AGE_OF_SIGMAR_ID: str = ""
AGE_OF_SIGMAR_NAME: str = ""

SUPPORTED_BATTLESCRIBE_VERSION = "2.03"

BATTLESCRIBE_VERSION_ERROR = {
    "ERROR": f"battlescribe version not supported please upgrade, the current supported version is "
    f"{SUPPORTED_BATTLESCRIBE_VERSION}"
}
