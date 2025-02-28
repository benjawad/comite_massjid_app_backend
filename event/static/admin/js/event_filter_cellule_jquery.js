(function($) {
    $(document).ready(function() {
        console.log("event_filter_cellule_jquery.js loaded.");

        // Function to load cellules based on selected branch
        function loadCellules() {
            var branchId = $("#id_branch").val();
            var $cellule = $("#id_cellule");
            $cellule.empty().append($('<option>', { value: '', text: '---------'}));

            if (branchId) {
                $.ajax({
                    url: "/admin/event/event/get_cellules_by_branch/",
                    data: { branch_id: branchId },
                    success: function(response) {
                        $.each(response.cellules, function(index, obj) {
                            $cellule.append($('<option>', {
                                value: obj.id,
                                text: obj.name
                            }));
                        });
                    }
                });
            }
        }

        // Trigger on branch change
        $(document).on("change", "#id_branch", loadCellules);

        // Trigger on initial load if branch is selected
        loadCellules();
    });
})(django.jQuery);