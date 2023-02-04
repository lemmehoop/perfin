$('#add').on("click", function () {
    $.ajax({
        url: "add_reminder",
        method: 'post',
        dataType: 'json',
        data: $('#r_form').serialize(),
        success: function (response) {
            let new_div = document.createElement("div")
            new_div.className = "card mb-2 mt-1"
            new_div.innerHTML = "<div class=\"row\">" +
                "                            <div class=\"col\">" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"card-title mt-1 mb-1 fw-normal flex-column\">" + response.title.substr(0, 27) + "</p>" +
                "                                </div>" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"m-0 time\">Только что</p>" +
                "                                </div>" +
                "                            </div>" +
                "                            <div class=\"col\">" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"m-0 mx-auto text-warning\">"+ response.amount +" ₽</p>" +
                "                                </div>" +
                "                                <div class=\"row\">" +
                "                                    <p class=\"m-0 mx-auto\">" + response.text.substr(0, 15) + "...</p>" +
                "                                </div>" +
                "                            </div>" +
                "                        </div>"
            parent_div = document.getElementById("list");
            first_child = parent_div.firstChild;
            parent_div.insertBefore(new_div, first_child);
            document.getElementById("r_form").reset();
        },
    })
})