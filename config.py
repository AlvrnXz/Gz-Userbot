from os import getenv

API_ID = int(getenv("API_ID", "26653586")) #optional
API_HASH = getenv("API_HASH", "89556c81a82b5aee3666d5347adacda0") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1902442454").split()))
OWNER_ID = int(getenv("OWNER_ID", "1902442454"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://varen:varen@varenz.uxs7ib2.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "5969049243:AAHw4jSudeH64NaIaSNHkOECVCXAPumI2n8")
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/1e53a14e6a70757d1d736.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001515331381")
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/alvrnxz/Gz-Userbot")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAooImhQ46BNcfjOkcCvRWZ7O85rlQxuLSwJqiCp6wI2urih85VJjrYRb7mLUt3POghEkI6FX0YBEBDlFI3tnO9zFpDH2uD5PPtbk_ge_nZp2DBAPMRbwz4dcbl-t74pTrbkT7n4MshtC8NppQ39U9bal9GkQ0GQ3saNYF2vv-bkTuSt883o0uVZ4t9zWr8fUSDKSh7jgzzgAFgY0plVL6xde0NxrT7Rm6NLqg6ycmNeAhbcPl8VftPOWcV64ztloRHZl6OKZ52WpCF_FLrKOsgnJqmNXSft4mjOk5huG4i1PP92a12hhV-ZARqopuHK-a5i6R6xqKM16ErnE6d8FAAAAABxZPfWAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
