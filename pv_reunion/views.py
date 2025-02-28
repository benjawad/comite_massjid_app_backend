from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pv_reunion.models import Branch, PVReunion, Cellule
from .serializers import BranchSerializer, PVReunionSerializer, CelluleSerializer
import json

class BranchList(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(json.loads(json.dumps(serializer.data, ensure_ascii=False)))

class CellulesList(generics.ListAPIView):
    queryset = Cellule.objects.all()
    serializer_class = CelluleSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(json.loads(json.dumps(serializer.data, ensure_ascii=False)))

class PVReunionsByCellule(generics.ListAPIView):
    serializer_class = PVReunionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cellule_id = self.request.query_params.get("cellule_id")
        if cellule_id:
            return PVReunion.objects.filter(cellule_id=cellule_id)
        return PVReunion.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(json.loads(json.dumps(serializer.data, ensure_ascii=False)))

class CellulesByBranch(generics.ListAPIView):
    serializer_class = CelluleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        branch_id = self.request.query_params.get("branch_id")
        if branch_id:
            return Cellule.objects.filter(branch_id=branch_id)
        return Cellule.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(json.loads(json.dumps(serializer.data, ensure_ascii=False)))

def upload_pdf(request):
    if request.method == "POST":
        form = PVReunionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Redirect to a list of uploaded PDFs
    else:
        form = PVReunionForm()
    
    return render(request, 'upload_pdf.html', {'form': form})
