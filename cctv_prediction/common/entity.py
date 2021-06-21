from dataclasses import dataclass


@dataclass
class Dataset(object):

    context: str
    fname: str
    url : object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def url(self) -> object: return self.url

    @url.setter
    def url(self, url): self._url = url


