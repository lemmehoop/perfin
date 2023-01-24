$('#add').on("click", function () {
    $.ajax({
        url: "add_spending",
        method: 'post',
        dataType: 'json',
        data: $('#s_form').serialize(),
        success: function (response) {
            let new_p = document.createElement("p")
            new_p.innerText = response.title + ", " + response.amount + ", " + response.category;
            document.getElementById("list").append(new_p);
            document.getElementById("s_form").reset();
        },
    })
})