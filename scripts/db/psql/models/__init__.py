# from typing import Optional, Union
#
# from pydantic.validators import str_validator
#
#
# def empty_to_none(v: str) -> Optional[str]:
#     if v == "":
#         return None
#     return v
#
#
# class EmptyStrToNone(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield str_validator
#         yield empty_to_none
#
#
# none_or_float = Union[None, float, EmptyStrToNone]
