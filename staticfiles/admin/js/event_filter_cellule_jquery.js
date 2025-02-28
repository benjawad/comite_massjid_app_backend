(function($) {
    $(document).ready(function() {
        console.log("event_filter_cellule_jquery.js loaded.");

        // Use delegated event binding to catch changes on the branch field.
        $(document).on("change", "#id_branch", function() {
            var branchId = $(this).val();
            console.log("[DEBUG] Branch changed. Value:", branchId);

            // Select the cellule dropdown and reset its content.
            var $cellule = $("#id_cellule");
            $cellule.empty().append($("<option>", { value: "", text: "---------" }));

            if (branchId) {
                var url = "/admin/event/event/get_cellules_by_branch/";
                console.log("[DEBUG] Making AJAX call to:", url, "with branch_id =", branchId);

                $.ajax({
                    url: url,
                    type: "GET",
                    data: { branch_id: branchId },
                    dataType: "json",
                    success: function(response) {
                        console.log("[DEBUG] AJAX success. Response:", response);
                        $.each(response.cellules, function(index, obj) {
                            $cellule.append($("<option>", {
                                value: obj.id,
                                text: obj.name
                            }));
                        });
                    },
                    error: function(xhr, status, error) {
                        console.error("[DEBUG] AJAX error:", error);
                    }
                });
            } else {
                console.log("[DEBUG] No branch selected; cellule dropdown remains reset.");
            }
        });
    });
})(window.django && window.django.jQuery ? window.django.jQuery : jQuery);