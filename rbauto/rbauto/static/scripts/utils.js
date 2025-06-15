window.utils = {
    submitForm(form_id) {
        const form = document.getElementById(form_id);
        const formData = new FormData(form);
        formData.append("previous_url", window.location.href);

        form.submit();
    }
}