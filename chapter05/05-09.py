'''함수 애너테이션은 python3부터 지원합니다.'''

def clip(text:str, max_len:'int > 0'=80) -> str:
    """max_len 앞이나 뒤으 ㅣ마지막 공백에서 잘라낸 텍스트를 반환한다.
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is not None:
        end = len(text)

    return text[:end].rstrip()

print(clip.__annotations__)
from inspect import signature
sig = signature(clip)
print(sig.return_annotation)
