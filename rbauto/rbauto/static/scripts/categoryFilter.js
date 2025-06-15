window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const subcategoryFilter = document.getElementById("subcategory_select");
    const manufacturerFilter = document.getElementById("manufacturer_select");

    const currentPage = document.getElementById("current_page");
    const previousBtn = document.getElementById("prev_btn");
    const nextBtn = document.getElementById("next_btn");

    const applyBtn = document.getElementById("filters_apply_btn");

    function applyFilters(page) {
        const filters = {
            "subcategory": subcategoryFilter.value,
            "manufacturer": manufacturerFilter.value,
            "page": page,
        };

        for (const [key, value] of Object.entries(filters)) {
            params.set(key, value);
        }

        window.location.search = params;
    }

    applyBtn.addEventListener('click', () => {
        applyFilters(currentPage.value);
    })

    if (previousBtn) {
        previousBtn.onclick = () => {
            const prevPage = previousBtn.dataset.page;
            if (prevPage) {
                applyFilters(prevPage);
            }
        }
    }

    if (nextBtn) {
        nextBtn.onclick = () => {
            const nextPage = nextBtn.dataset.page;
            if (nextPage) {
                applyFilters(nextPage);
            }
        }
    }
})
