import re


def namespace(s: str) -> str:
    return f"{escape_reserved(snake_case(s))}__"


def member(s: str) -> str:
    return escape_reserved(snake_case(s))


def snake_case(s: str) -> str:
    if not re.match(r"^[A-Za-z0-9_\-\s]+$", s):
        raise ValueError(
            f"'{s}' contains invalid characters. "
            + "Only letters, numbers, spaces, hyphens, and underscores are allowed."
        )
    return s.replace("-", "_").replace(" ", "_")


def escape_reserved(s: str) -> str:
    if s in keywords:
        if s not in reserved_warned:
            print(
                f"Warning: key '{s}' will be renamed to '{s}_'."
            )
            reserved_warned.append(s)
        return f"{s}_"
    return s

reserved_warned = []

# https://en.cppreference.com/w/cpp/keywords.html
keywords = [
    "alignas",
    "alignof",
    "and",
    "and_eq",
    "asm",
    "atomic_cancel",
    "atomic_commit",
    "atomic_noexcept",
    "auto",
    "bitand",
    "bitor",
    "bool",
    "break",
    "case",
    "catch",
    "char",
    "char8_t",
    "char16_t",
    "char32_t",
    "class",
    "compl",
    "concept",
    "const",
    "consteval",
    "constexpr",
    "constinit",
    "const_cast",
    "continue",
    "contract_assert",
    "co_await",
    "co_return",
    "co_yield",
    "decltype",
    "default",
    "delete",
    "do",
    "double",
    "dynamic_cast",
    "else",
    "enum",
    "explicit",
    "export",
    "extern",
    "false",
    "float",
    "for",
    "friend",
    "goto",
    "if",
    "inline",
    "int",
    "long",
    "mutable",
    "namespace",
    "new",
    "noexcept",
    "not",
    "not_eq",
    "nullptr",
    "operator",
    "or",
    "or_eq",
    "private",
    "protected",
    "public",
    "reflexpr",
    "register",
    "reinterpret_cast",
    "requires",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "static_assert",
    "static_cast",
    "struct",
    "switch",
    "synchronized",
    "template",
    "this",
    "thread_local",
    "throw",
    "true",
    "try",
    "typedef",
    "typeid",
    "typename",
    "union",
    "unsigned",
    "using",
    "virtual",
    "void",
    "volatile",
    "wchar_t",
    "while",
    "xor",
    "xor_eq",
]
