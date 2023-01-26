$('#add').on("click", function () {
    $.ajax({
        url: "add_spending",
        method: 'post',
        dataType: 'json',
        data: $('#s_form').serialize(),
        success: function (response) {
            let new_div = document.createElement("div")
            new_div.className = "card mt-2"
            new_div.innerHTML = "<div class=\"row\">" +
                "                            <div class=\"col\">" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"card-title mt-1 mb-1 fw-normal flex-column\">" + response.title + "</p>" +
                "                                </div>" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"m-0 time\">Только что</p>" +
                "                                </div>" +
                "                            </div>" +
                "                            <div class=\"col\">" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"m-0 mx-auto text-danger\">-"+ response.amount +" ₽</p>" +
                "                                </div>" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"m-0 mx-auto\">" + response.category + "</p>" +
                "                                </div>" +
                "                            </div>" +
                "                        </div>"
            parent_div = document.getElementById("list");
            first_child = parent_div.firstChild;
            parent_div.insertBefore(new_div, first_child);
            document.getElementById("s_form").reset();
        },
    })
})