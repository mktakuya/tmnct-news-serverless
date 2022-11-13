from dataclasses import dataclass
from dataclasses_json import dataclass_json, DataClassJsonMixin

from .news import News


@dataclass_json
@dataclass
class FetchAndSaveNewsResult(DataClassJsonMixin):
    updated: bool
    news: News
