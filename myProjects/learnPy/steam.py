import re


url = input("URL: ").strip()


# username = re.sub(r"^(https?://)?(www\.)?steamcommunity\.com/id/", "", url)
# print(f"Username: {username}")


if matches := re.search(r"^https?://(?:www\.)?steamcommunity\.com/id/([a-z0-9_])$", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))