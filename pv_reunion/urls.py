from django.urls import path
from .views import BranchList, PVReunionsByCellule, CellulesByBranch, upload_pdf , CellulesList

urlpatterns = [
    path("branches/", BranchList.as_view(), name="branch-list"),
    path("pvreunions_by_cellule/", PVReunionsByCellule.as_view(), name="pvreunions-by-cellule"),
    path("cellules_by_branch/", CellulesByBranch.as_view(), name="cellules-by-branch"),
    path("cellules/", CellulesList.as_view(), name="cellules-list"),
    path("upload_pdf/", upload_pdf, name="upload_pdf"),
]