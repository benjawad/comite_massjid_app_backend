document.addEventListener("DOMContentLoaded", function () {
    const branchField = document.querySelector("#id_branch");
    const celluleField = document.querySelector("#id_cellule");

    function updateCelluleOptions() {
        const branchId = branchField.value;
        celluleField.innerHTML = '<option value="">---------</option>'; // Reset cellule dropdown

        if (branchId) {
            fetch(`/admin/pv_reunion/pvreunion/get_cellules_by_branch/?branch_id=${branchId}`)
                .then(response => response.json())
                .then(data => {
                    data.cellules.forEach(cellule => {
                        let option = new Option(cellule.name, cellule.id);
                        celluleField.add(option);
                    });
                })
                .catch(error => console.error("Error fetching cellules:", error));
        }
    }

    branchField.addEventListener("change", updateCelluleOptions);
});
