



let table_body2 = document.querySelector("#table-body2")
let is_admin = document.querySelector("#is_admin")

document.addEventListener("DOMContentLoaded", function() {
    // Gọi hàm để lấy dữ liệu từ máy chủ nếu chưa lấy
    if (!hasFetchedData) {
        fetchDataFromServer();
        hasFetchedData = true; // Đã lấy dữ liệu, không gửi lại
    }

    add_more_rider.addEventListener("click",()=>{
        window.location.href = "add_more_rider.html"
    })

    edit_rider.addEventListener("click",()=>{
        window.location.href = "edit_rider.html"
    })

},false);

// Hàm để gửi yêu cầu đến máy chủ và xử lý dữ liệu trả về
function fetchDataFromServer() {
    // Sử dụng fetch hoặc XMLHttpRequest để gửi yêu cầu đến máy chủ
    fetch("http://localhost:8001/api/get_data")
        .then(response => response.json()) // Chuyển đổi dữ liệu trả về thành JSON
        .then(data => {
            // Xử lý dữ liệu ở đây
            // console.log( data);
            // console.log(typeof data)
            var datalist = JSON.parse(data)
            console.log(datalist)
            console.log(typeof datalist)
            for (var i = 0; i < datalist.length; i++) {
                var row = document.createElement('tr');
            
                for (var j = 0; j < datalist[i].length; j++) {
                    var cell = document.createElement('td'); // Sử dụng 'td' cho tất cả các dòng
                    cell.textContent = datalist[i][j];
                    row.appendChild(cell);
                }
            
                tableBody.appendChild(row);
            }
            // for (i in data){
            //     console.log(i)
            // }
        })
        .catch(error => {
            console.error("Lỗi khi gửi yêu cầu đến máy chủ:", error);
        });
}