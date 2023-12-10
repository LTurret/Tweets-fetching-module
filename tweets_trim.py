from re import findall


def trim(urls: dict, upper_snowflake: int) -> list:
    regex: str = r"https\:\/\/[x|twitter]+\.com\/.+\/status\/(\d+)"
    trimmed: list[int] = []
    for url in urls:
        if int(findall(regex, url)[0]) > upper_snowflake:
            trimmed.append(url)

    return trimmed
