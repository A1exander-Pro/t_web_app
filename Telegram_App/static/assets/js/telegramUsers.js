const table = $("#userRows");

function getFilterData(selector, url) {
    $.ajax({
        method: "GET",
        dataType: 'json',
        url: `api/${url}/`,

        success: function (data) {
            console.log(data)
            const filter_field = $(`#${selector}`);
            data.forEach(item => {

                let component = `
                    <tr>
                        <td class="text-center">${item.username}</td>
                        <td class="text-center">${item.user_id}</td>
                        <td class="text-center">${item.date}</td>
                    </tr>
            `
                filter_field.append(component)
            })
        },
        complete: function () {

        }
    })
}

$(document).ready(function () {
  getFilterData('userRows', 'telegram-users')

})