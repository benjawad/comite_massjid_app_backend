

from django import forms
from .models import PVReunion
from .models import Branch
from .models import Cellule

class PVReunionForm(forms.ModelForm):
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        required=False,
        label="Branch"
    )

    class Meta:
        model = PVReunion
        # Include 'branch' explicitly along with the other fields you need.
        fields = ("title", "date","branch", "cellule",  "content" , )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initially, clear cellule queryset.
        self.fields["cellule"].queryset = Cellule.objects.none()

        if self.data.get("branch"):  # when form is submitted (or AJAX call)
            try:
                branch_id = int(self.data.get("branch"))
                self.fields["cellule"].queryset = Cellule.objects.filter(branch_id=branch_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.cellule:
            # When editing an existing object: set branche according to cellule's branch.
            self.fields["branch"].initial = self.instance.cellule.branch
            self.fields["cellule"].queryset = Cellule.objects.filter(branch=self.instance.cellule.branch)
