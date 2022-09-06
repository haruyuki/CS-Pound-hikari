import re


def multi_replace(string, replacements):
    # Taken from https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
    substrings = sorted(replacements, key=len, reverse=True)
    regexp = re.compile("|".join(map(re.escape, substrings)))
    return regexp.sub(lambda match: replacements[match.group(0)], string)
