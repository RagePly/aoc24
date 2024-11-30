import re

__all__ = [
    "numbers",
    "regex",
    "chunks",
]
    
def chunks(f):
    def chunks_wrapper(src):
        return f(src.split("\n\n"))
    return chunks_wrapper

def numbers(f):
    pat = re.compile(r"\d+")
    def numbers_wrapper(src):
        chks = [src] if isinstance(src, str) else src
        chks_rows = []
        for chk in chks: 
            rows = []
            for line in chk.splitlines():
                if (nms := list(map(int, re.findall(pat, line)))):
                    rows.append(nms)
            chks_rows.append(rows)

        if isinstance(src, str):
            return f(chks_rows[0])
        return f(chks_rows)

    return numbers_wrapper

def regex(r):
    pat = re.compile(r)
    def regex_decorator(f):
        def regex_wrapper(src):
            chks = [src] if isinstance(src, str) else src
            chks_rows = []
            for chk in chks: 
                rows = []
                for line in chk.splitlines():
                    if (m := re.match(pat, line)) is not None:
                        rows.append(m)
                chks_rows.append(rows)

            if isinstance(src, str):
                return f(chks_rows[0])
            return f(chks_rows)
        return regex_wrapper
    return regex_decorator

