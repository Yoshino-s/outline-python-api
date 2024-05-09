# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DocumentViewedParams"]


class DocumentViewedParams(TypedDict, total=False):
    direction: Literal["ASC", "DESC"]

    limit: float

    offset: float

    sort: str
