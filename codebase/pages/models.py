from auto_prefetch import ForeignKey
from django.db import models
from django.urls import reverse_lazy

from ..utils.abstracts import PageModel, SubmodulesFolder


class PagesFolder(SubmodulesFolder):
    submodule_name = "pages"


class Page(PageModel):
    """File-based page model"""

    submodule_folder_model = PagesFolder
    submodule_folder = ForeignKey(PagesFolder, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse_lazy("page-detail", kwargs={"slug": self.slug})
