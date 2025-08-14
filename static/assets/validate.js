$("#url_form").validate({
    rules: {
        original_url: {
            required: true,
        },
    },
    messages: {
        original_url: {
            required: "Please enter the original url",
        },
    },
    errorElement: "label",
    errorPlacement: function(error, element){
        error.addClass("error");
        error.insertAfter(element);
    },
    submitHandler: function (form) {
        form.submit();
    }
});
