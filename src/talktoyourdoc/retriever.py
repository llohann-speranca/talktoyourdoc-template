class Retriever:
    def similarity_search(self,
                          query: str,
                          return_k: int):
        raise NotImplementedError


class PostProcessor:

    def __call__(self, search_results):
        return [self._post_process_single_result(item) for item in search_results]

    def _post_process_single_result(self,
                                    item):
        raise NotImplementedError