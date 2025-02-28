from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from .models import PVReunion, Cellule, Branch
from .forms import PVReunionForm

# class PVReunionForm(forms.ModelForm):
#     class Meta:
#         model = PVReunion
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["cellule"].queryset = Cellule.objects.none()  # Initially empty

#         if "branch" in self.data:  # If form is submitted with a branch
#             try:
#                 branch_id = int(self.data.get("branch"))
#                 self.fields["cellule"].queryset = Cellule.objects.filter(branch_id=branch_id)
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk:  # If editing an existing PVReunion
#             self.fields["cellule"].queryset = self.instance.branch.cellule_set.all()
# from django import forms
# from .models import PVReunion, Cellule, Branch


# Custom Admin class
@admin.register(PVReunion)
class PVReunionAdmin(admin.ModelAdmin):
    form = PVReunionForm
    list_display = ("title", "date", "created_at", "cellule")
    search_fields = ("title", "content")
    list_filter = ("date", "created_at", "cellule")
    ordering = ("-date",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("get_cellules_by_branch/", self.admin_site.admin_view(self.get_cellules_by_branch), name="get_cellules_by_branch"),
        ]
        return custom_urls + urls



    def get_cellules_by_branch(self, request):
        branch_id = request.GET.get("branch_id")
        cellules = Cellule.objects.filter(branch_id=branch_id).values("id", "name")
        return JsonResponse({"cellules": list(cellules)})

    class Media:
        js = ("admin/js/filter_celule.js",)  

admin.site.register(Cellule)
admin.site.register(Branch)
