$('#add').on("click", function () {
    $.ajax({
        url: "add_spending",
        method: 'post',
        dataType: 'json',
        data: $('#s_form').serialize(),
        success: function (response) {
            let new_div = document.createElement("div")
            new_div.className = "card text-center mt-2"
            new_div.innerHTML = "                        <div class=\"card-body p-0\">" +
                "                            <h5 class=\"card-title mt-1 mb-1\">" + response.title +"</h5>" +
                "                            <p class=\"card-text\">На сумму "+ response.amount +"₽ | В категории "+ response.category +"</p>" +
                "                        </div>" +
                "                        <div class=\"card-footer text-muted p-0\">\n" +
                "                            Только что" +
                "                        </div>"
            parent_div = document.getElementById("list");
            first_child = parent_div.firstChild;
            parent_div.insertBefore(new_div, first_child);
            document.getElementById("s_form").reset();
        },
    })
})