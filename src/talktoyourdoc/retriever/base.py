from dataclasses import dataclass, fields
from pathlib import Path

from talktoyourdoc.retriever.dbconn import DatabaseConnector


@dataclass
class OutputItem:
    """Dictionary-like object holding the desired attributes"""
    hash_code: str
    description: str
    image_path: Path  # Change to image: PIL.Image

    # Parsing method
    @classmethod
    def unsafe_parse(cls, **kwargs):
        valid_kwargs = [f.name for f in fields(OutputItem)]
        sanitized_kwargs = {k: v for k, v in kwargs.items() if k in valid_kwargs}
        return OutputItem(**sanitized_kwargs)


@dataclass
class PostProcessor:
    """Dataclass that receives the raw result from the Retriever and parse into the desired output"""
    database_connector: DatabaseConnector

    def __call__(self, search_results):
        return [self._post_process_single_result(item) for item in search_results]

    def _post_process_single_result(self,
                                    item):
        image_path, hash_code = item
        row = self.database_connector(hash_code)
        item = OutputItem.unsafe_parse(**row)
        return item
