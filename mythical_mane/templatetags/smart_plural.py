from django import template

register = template.Library()


@register.filter(is_safe=True)
def smart_plural(value, count=None):
    """Return a (mostly) correct plural form of `value`.

    Usage:
      {{ "Ability"|smart_plural }} -> "Abilities"
      {{ name|smart_plural:count }} -> pluralized depending on count

    This is a pragmatic filter with common English rules and a small
    exceptions map for irregulars. It preserves capitalization.
    """
    if value is None:
        return value

    try:
        text = str(value)
    except Exception:
        return value

    # If a count is provided and equals 1, return singular
    if count is not None:
        try:
            if int(count) == 1:
                return text
        except Exception:
            pass

    exceptions = {
        "ability": "abilities",
        "diagnosis": "diagnoses",
        "person": "people",
        "child": "children",
        "mouse": "mice",
        "goose": "geese",
        "man": "men",
        "woman": "women",
    }

    def preserve_case(orig, new):
        if orig.isupper():
            return new.upper()
        if orig.istitle():
            return new.title()
        return new

    lower = text.lower()
    if lower in exceptions:
        return preserve_case(text, exceptions[lower])

    # common rules
    if lower.endswith(("s", "x", "z", "ch", "sh")):
        return preserve_case(text, text + "es")

    if lower.endswith("y") and len(lower) > 1 and lower[-2] not in "aeiou":
        return preserve_case(text, text[:-1] + "ies")

    if lower.endswith("fe"):
        return preserve_case(text, text[:-2] + "ves")

    if lower.endswith("f"):
        return preserve_case(text, text[:-1] + "ves")

    # default
    return preserve_case(text, text + "s")
